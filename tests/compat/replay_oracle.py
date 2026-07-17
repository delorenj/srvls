#!/usr/bin/env python3
"""Render and validate the frozen srvls Python compatibility oracle.

This harness executes the immutable Git blob named below.  It never imports the
working-tree ``srvls`` file and it never invokes a replacement implementation.
Goldens are captured assertion inputs, not products of the encoder under test.
"""

from __future__ import annotations

import argparse
import builtins
import contextlib
import copy
import datetime as datetime_module
import hashlib
import io
import json
import os
import posixpath
import subprocess as host_subprocess
import sys
import types
from pathlib import Path, PurePosixPath
from typing import Any


COMPAT_ROOT = Path(__file__).resolve().parent
REPO_ROOT = COMPAT_ROOT.parents[1]
FROZEN_PARENT = "598eb0ccd0ad37a9432a2132a14d75aeea0f9f47"
FROZEN_PATH = "srvls"
FROZEN_BLOB_SHA1 = "aebb996d1341fc44afe513126ca6553815faa904"
FROZEN_SHA256 = "06a7e312fba5f2ca03e99181cc208d7abd9ac4688f26ea0f8c89ee19eb9e8b62"
FROZEN_SIZE = 13_388
FIXED_SOURCE_PATH = "/opt/srvls/srvls"

VOLATILE_SUBSTITUTIONS = [
    {
        "id": "clock.utc-now",
        "rule": "datetime.now() is fixture-owned UTC instead of capture wall time",
    },
    {
        "id": "clock.timer-local-rendering",
        "rule": "datetime.fromtimestamp() renders in UTC instead of host local time",
    },
    {
        "id": "host.load-average",
        "rule": "os.getloadavg() is the fixture triple [1.25, 2.5, 3.75] unless overridden",
    },
    {
        "id": "host.identity-and-paths",
        "rule": "HOME, USER, PATH lookup, virtual /etc files, and tool presence are fixture-owned",
    },
    {
        "id": "source.absolute-path",
        "rule": "the frozen source __file__ and os.path.abspath(__file__) are /opt/srvls/srvls",
    },
    {
        "id": "host.subprocess-results",
        "rule": "stdout, stderr, exit, missing, denied, and timeout outcomes are fixture-owned",
    },
    {
        "id": "python.traceback",
        "rule": "unhandled tracebacks normalize to exception type and message; version, frame path, and line rendering are excluded",
    },
]

EXPECTED_CASE_IDS = {
    "providers": {
        "cron.success",
        "cron.malformed",
        "cron.unavailable",
        "cron.denied",
        "cron.timeout",
        "cron.system-file-denied",
        "systemd-system.success",
        "systemd-user.success",
        "systemd.malformed",
        "systemd.unavailable",
        "systemd.denied",
        "systemd.timeout",
        "systemd.wrong-shaped",
        "docker.success",
        "docker.malformed",
        "docker.unavailable",
        "docker.denied",
        "docker.timeout",
        "pm2.success",
        "pm2.malformed",
        "pm2.absent",
        "pm2.command-unavailable",
        "pm2.denied",
        "pm2.timeout",
        "pm2.wrong-shaped",
    },
    "outputs": {
        "output.table",
        "output.json",
        "output.prometheus",
        "output.markdown",
        "output.fzf-lines",
    },
    "cli": {
        "flags.all-known-json-wins",
        "flags.json-wins-reversed",
        "flags.prom-wins",
        "flags.markdown-wins",
        "flags.fzf-lines-wins",
        "flags.help-is-table",
        "flags.help-plus-json",
        "flags.unknown-is-table",
        "flags.fzf-absent",
        "flags.fzf-present-bindings",
        "arity.inspect-one",
        "arity.inspect-two",
        "arity.inspect-four",
        "arity.stop-two",
        "arity.restart-two",
        "arity.start-two",
        "arity.disable-two",
        "inspect.unknown-success-empty",
        "action.cron-refusal-stdout",
        "action.unknown-refusal-stdout",
        "action.child-channel-placement",
    },
    "inspection": {
        "inspect.docker-hostile-and-merged-logs",
        "inspect.user-service-hostile",
        "inspect.user-timer-hostile",
        "inspect.system-service-hostile",
        "inspect.system-timer-hostile",
        "inspect.pm2-hostile",
        "inspect.cron-hostile",
        "inspect.unknown-success-empty",
        "inspect.docker-unavailable-still-separator",
        "inspect.pm2-absent-success-empty",
        "inspect.system-timeout-success-empty",
    },
    "actions": {
        f"action.{verb}.{provider_type}"
        for verb in ("stop", "restart", "start", "disable")
        for provider_type in (
            "usr-svc",
            "usr-timer",
            "sys-svc",
            "sys-timer",
            "docker",
            "pm2",
            "cron",
            "mystery",
        )
    },
}

REQUIRED_COVERAGE_KEYS = {
    "provider_success",
    "provider_malformed",
    "provider_unavailable",
    "provider_denied",
    "provider_timeout",
    "wrong_shaped_structured_data",
    "output_surfaces",
    "ordering_and_escaping",
    "flag_precedence_help_unknown_arity",
    "empty_and_channel_placement",
    "missing_optional_tools",
    "inspection",
    "action_argv",
    "hostile_identifiers",
}

EXPECTED_APPROVED_DEVIATIONS = {
    "flags.help-is-table": {
        "selected_profile": "help",
        "collection_started": False,
        "stdout_bytes": "Usage%3A%20srvls%20%5BOPTIONS%5D%20%5BCOMMAND%5D%0A%0AOptions%3A%0A%20%20--json%20%20%20Emit%20legacy%20JSON%20inventory%0A%20%20--prom%20%20%20Emit%20Prometheus%20metrics%0A%20%20--md%20%20%20%20%20Emit%20Markdown%20inventory%0A%20%20--table%20%20Emit%20table%20inventory%0A%20%20--tui%20%20%20%20Open%20the%20terminal%20UI%0A%20%20--fzf%20%20%20%20Deprecated%20alias%20for%20--tui%0A%20%20-h%2C%20--help%20%20Print%20help%0A",
        "stderr_bytes": "",
        "exit_status": 0,
    },
    "flags.help-plus-json": {
        "selected_profile": "help",
        "collection_started": False,
        "stdout_bytes": "Usage%3A%20srvls%20%5BOPTIONS%5D%20%5BCOMMAND%5D%0A%0AOptions%3A%0A%20%20--json%20%20%20Emit%20legacy%20JSON%20inventory%0A%20%20--prom%20%20%20Emit%20Prometheus%20metrics%0A%20%20--md%20%20%20%20%20Emit%20Markdown%20inventory%0A%20%20--table%20%20Emit%20table%20inventory%0A%20%20--tui%20%20%20%20Open%20the%20terminal%20UI%0A%20%20--fzf%20%20%20%20Deprecated%20alias%20for%20--tui%0A%20%20-h%2C%20--help%20%20Print%20help%0A",
        "stderr_bytes": "",
        "exit_status": 0,
    },
    "flags.unknown-is-table": {
        "selected_profile": "argument-error",
        "collection_started": False,
        "stdout_bytes": "",
        "stderr_bytes": "error%3A%20unexpected%20argument%20%27--definitely-unknown%27%0A",
        "exit_status": 2,
    },
    "flags.fzf-lines-wins": {
        "selected_profile": "argument-error",
        "collection_started": False,
        "stdout_bytes": "",
        "stderr_bytes": "error%3A%20retired%20option%20%27--fzf-lines%27%3B%20use%20%27--fzf%27%20or%20%27--json%27%0A",
        "exit_status": 2,
        "replacement_argv": ["srvls --fzf", "srvls --json"],
    },
}

EXPECTED_AFFECTED_CONSUMERS = {
    "human CLI users",
    "legacy fzf preview and action bindings",
    "script consumers",
}


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _canonical_bytes(value: Any) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode()


def _git(*args: str) -> bytes:
    result = host_subprocess.run(
        ["git", "-C", str(REPO_ROOT), *args],
        check=True,
        stdout=host_subprocess.PIPE,
        stderr=host_subprocess.PIPE,
    )
    return result.stdout


def frozen_source_bytes() -> bytes:
    resolved = _git("rev-parse", f"{FROZEN_PARENT}:{FROZEN_PATH}").decode().strip()
    if resolved != FROZEN_BLOB_SHA1:
        raise RuntimeError(
            f"frozen path resolved to {resolved}, expected {FROZEN_BLOB_SHA1}"
        )
    source = _git("cat-file", "blob", FROZEN_BLOB_SHA1)
    if len(source) != FROZEN_SIZE:
        raise RuntimeError(f"frozen source size {len(source)} != {FROZEN_SIZE}")
    digest = _sha256(source)
    if digest != FROZEN_SHA256:
        raise RuntimeError(f"frozen source SHA-256 {digest} != {FROZEN_SHA256}")
    return source


def _deep_merge(base: dict[str, Any], overlay: dict[str, Any]) -> dict[str, Any]:
    merged = copy.deepcopy(base)
    for key, value in overlay.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = _deep_merge(merged[key], value)
        else:
            merged[key] = copy.deepcopy(value)
    return merged


class FrozenSys:
    def __init__(self, argv: list[str]) -> None:
        self.argv = ["srvls", *argv]

    @staticmethod
    def exit(code: object = None) -> None:
        raise SystemExit(code)


class VirtualPath:
    def __init__(self, host: "VirtualOs") -> None:
        self.host = host

    def expanduser(self, path: str) -> str:
        if path == "~":
            return self.host.home
        if path.startswith("~/"):
            return self.host.home + path[1:]
        return path

    def isfile(self, path: str) -> bool:
        value = self.host.files.get(path)
        return value is not None and not (
            isinstance(value, dict) and value.get("kind") == "directory"
        )

    def isdir(self, path: str) -> bool:
        prefix = path.rstrip("/") + "/"
        return path in self.host.directories or any(
            candidate.startswith(prefix) for candidate in self.host.files
        )

    @staticmethod
    def join(*parts: str) -> str:
        return posixpath.join(*parts)

    @staticmethod
    def abspath(path: str) -> str:
        if path == FIXED_SOURCE_PATH:
            return FIXED_SOURCE_PATH
        return posixpath.abspath(path)


class VirtualOs:
    def __init__(self, config: dict[str, Any]) -> None:
        self.home = config.get("home", "/home/test")
        self.environ = dict(config.get("env", {}))
        self.files = dict(config.get("files", {}))
        self.directories = set(config.get("directories", []))
        self.loadavg = tuple(config.get("loadavg", [1.25, 2.5, 3.75]))
        self.path = VirtualPath(self)

    def listdir(self, path: str) -> list[str]:
        prefix = path.rstrip("/") + "/"
        children = {
            candidate[len(prefix) :].split("/", 1)[0]
            for candidate in self.files
            if candidate.startswith(prefix) and candidate != path
        }
        return sorted(children)

    def getloadavg(self) -> tuple[float, float, float]:
        return self.loadavg  # type: ignore[return-value]

    def open(self, path: str, mode: str = "r", *args: object, **kwargs: object) -> io.StringIO:
        del args, kwargs
        if mode not in ("r", "rt"):
            raise AssertionError(f"virtual oracle filesystem is read-only: {mode}")
        if path not in self.files:
            raise FileNotFoundError(f"[Errno 2] fixture missing: '{path}'")
        value = self.files[path]
        if isinstance(value, dict):
            error = value.get("error")
            message = value.get("message", f"fixture {error}: {path}")
            if error == "permission-denied":
                raise PermissionError(message)
            if error == "file-not-found":
                raise FileNotFoundError(message)
            raise OSError(message)
        return io.StringIO(str(value))


class VirtualShutil:
    def __init__(self, configured: dict[str, Any], calls: list[dict[str, Any]]) -> None:
        self.configured = configured
        self.calls = calls

    def which(self, name: str) -> str | None:
        value = self.configured.get(name)
        resolved = value if isinstance(value, str) and value else None
        self.calls.append({"name": name, "result": resolved})
        return resolved


class VirtualCompletedProcess:
    def __init__(self, stdout: str, stderr: str, returncode: int) -> None:
        self.stdout = stdout
        self.stderr = stderr
        self.returncode = returncode


class VirtualSubprocess:
    def __init__(self, config: dict[str, Any], calls: list[dict[str, Any]]) -> None:
        self.rules = list(config.get("commands", []))
        self.default = dict(
            config.get(
                "default_command",
                {
                    "error": "file-not-found",
                    "message": "[Errno 2] fixture command not found",
                },
            )
        )
        self.calls = calls

    def _response(self, argv: list[str]) -> dict[str, Any]:
        for rule in self.rules:
            if rule.get("argv") == argv:
                return rule
        return self.default

    def run(
        self,
        cmd: list[object],
        capture_output: bool = False,
        text: bool = False,
        timeout: int | None = None,
        input: str | None = None,
        **kwargs: object,
    ) -> VirtualCompletedProcess:
        if kwargs:
            raise AssertionError(f"unsupported subprocess kwargs: {sorted(kwargs)}")
        argv = [str(part) for part in cmd]
        response = self._response(argv)
        call: dict[str, Any] = {
            "argv": argv,
            "capture_output": capture_output,
            "input": input,
            "text": text,
            "timeout": timeout,
        }
        error = response.get("error")
        if error:
            message = response.get("message", f"fixture {error}: {argv[0]}")
            call["outcome"] = {"kind": "error", "error": error, "message": message}
            self.calls.append(call)
            if error == "file-not-found":
                raise FileNotFoundError(message)
            if error == "permission-denied":
                raise PermissionError(message)
            if error == "timeout":
                raise TimeoutError(message)
            raise OSError(message)

        stdout = str(response.get("stdout", ""))
        stderr = str(response.get("stderr", ""))
        returncode = int(response.get("returncode", 0))
        call["outcome"] = {
            "kind": "completed",
            "returncode": returncode,
            "stderr": stderr,
            "stdout": stdout,
        }
        self.calls.append(call)
        if not capture_output:
            if stdout:
                print(stdout, end="")
            if stderr:
                print(stderr, end="", file=sys.stderr)
        return VirtualCompletedProcess(stdout, stderr, returncode)


def _frozen_datetime(fixed_now: str) -> type:
    parsed = datetime_module.datetime.fromisoformat(fixed_now)
    if parsed.tzinfo is None:
        raise ValueError("fixed_now must include an explicit UTC offset")

    class FrozenDateTime:
        @classmethod
        def now(cls, tz: datetime_module.tzinfo | None = None) -> datetime_module.datetime:
            if tz is None:
                return parsed.replace(tzinfo=None)
            return parsed.astimezone(tz)

        @classmethod
        def fromtimestamp(cls, value: float) -> datetime_module.datetime:
            return datetime_module.datetime.fromtimestamp(
                value, datetime_module.timezone.utc
            ).replace(tzinfo=None)

    return FrozenDateTime


def _load_module(source: bytes, config: dict[str, Any], argv: list[str]) -> tuple[types.ModuleType, list[dict[str, Any]], list[dict[str, Any]]]:
    module = types.ModuleType("srvls_frozen_oracle")
    module.__file__ = FIXED_SOURCE_PATH
    exec(compile(source, FIXED_SOURCE_PATH, "exec"), module.__dict__)

    external_calls: list[dict[str, Any]] = []
    which_calls: list[dict[str, Any]] = []
    virtual_os = VirtualOs(config)
    module.os = virtual_os
    module.open = virtual_os.open
    module.subprocess = VirtualSubprocess(config, external_calls)
    module.shutil = VirtualShutil(dict(config.get("which", {})), which_calls)
    module.datetime = _frozen_datetime(
        config.get("fixed_now", "2026-07-17T12:34:56+00:00")
    )
    module.sys = FrozenSys(argv)
    module.HOME = virtual_os.home
    return module, external_calls, which_calls


def _expand_cases(fixture: dict[str, Any]) -> list[dict[str, Any]]:
    expanded: list[dict[str, Any]] = []
    for case in fixture["cases"]:
        operation = case["operation"]
        if operation["kind"] != "action-cross-product":
            expanded.append(case)
            continue
        for verb in operation["verbs"]:
            for provider_type in operation["types"]:
                concrete = copy.deepcopy(case)
                concrete["id"] = f"{case['id']}.{verb}.{provider_type}"
                concrete["operation"] = {
                    "kind": "action",
                    "verb": verb,
                    "type": provider_type,
                    "name": operation["name"],
                }
                expanded.append(concrete)
    return expanded


def _invoke(module: types.ModuleType, operation: dict[str, Any]) -> Any:
    kind = operation["kind"]
    if kind == "main":
        return module.main()
    if kind == "collector":
        provider = operation["provider"]
        if provider == "cron":
            return module.collect_cron()
        if provider == "systemd-system":
            return module._systemd("system")
        if provider == "systemd-user":
            return module._systemd("user")
        if provider == "docker":
            return module.collect_docker()
        if provider == "pm2":
            return module.collect_pm2()
        raise ValueError(f"unknown collector {provider}")
    if kind == "action":
        return module.action(operation["verb"], operation["type"], operation["name"])
    if kind == "inspect":
        return module.inspect(operation["type"], operation["name"])
    raise ValueError(f"unknown operation kind {kind}")


def _run_case(source: bytes, fixture: dict[str, Any], case: dict[str, Any]) -> dict[str, Any]:
    config = copy.deepcopy(fixture.get("defaults", {}))
    environment_name = case.get("environment")
    if environment_name:
        config = _deep_merge(config, fixture.get("environments", {})[environment_name])
    config = _deep_merge(config, case.get("overrides", {}))
    operation = case["operation"]
    argv = operation.get("argv", [])
    module, external_calls, which_calls = _load_module(source, config, argv)

    stdout = io.StringIO()
    stderr = io.StringIO()
    return_value: Any = None
    has_return_value = operation["kind"] != "main"
    with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
        try:
            return_value = _invoke(module, operation)
            termination: dict[str, Any] = {"kind": "return"}
        except SystemExit as exc:
            if isinstance(exc.code, str):
                print(exc.code, file=sys.stderr)
                termination = {"kind": "exit", "code": 1}
            elif exc.code is None:
                termination = {"kind": "exit", "code": 0}
            else:
                termination = {"kind": "exit", "code": int(exc.code)}
        except Exception as exc:  # Frozen legacy crashes are assertion evidence.
            termination = {
                "kind": "exception",
                "message": str(exc),
                "type": type(exc).__name__,
            }

    result: dict[str, Any] = {
        "case_id": case["id"],
        "external_calls": external_calls,
        "operation": operation,
        "stderr": stderr.getvalue(),
        "stdout": stdout.getvalue(),
        "termination": termination,
        "which_calls": which_calls,
    }
    if has_return_value and termination["kind"] == "return":
        result["return_value"] = return_value
    return result


def render_fixture(path: Path) -> bytes:
    raw = path.read_bytes()
    fixture = json.loads(raw)
    if fixture.get("schema") != "srvls-legacy-fixture-v1":
        raise ValueError(f"unsupported fixture schema in {path}")
    source = frozen_source_bytes()
    relative = path.resolve().relative_to(COMPAT_ROOT).as_posix()
    result = {
        "cases": [
            _run_case(source, fixture, case) for case in _expand_cases(fixture)
        ],
        "fixture": {
            "matrix_id": fixture["matrix_id"],
            "path": relative,
            "sha256": _sha256(raw),
        },
        "schema": "srvls-legacy-oracle-result-v1",
        "source": {
            "frozen_parent": FROZEN_PARENT,
            "git_blob_sha1": FROZEN_BLOB_SHA1,
            "path": FROZEN_PATH,
            "sha256": FROZEN_SHA256,
            "size": FROZEN_SIZE,
        },
        "volatile_substitutions": VOLATILE_SUBSTITUTIONS,
    }
    return _canonical_bytes(result)


def _load_manifest() -> dict[str, Any]:
    return json.loads((COMPAT_ROOT / "manifest.json").read_bytes())


def _verify_hash_manifest() -> None:
    hash_path = COMPAT_ROOT / "SHA256SUMS"
    seen: set[str] = set()
    for line_number, line in enumerate(hash_path.read_text().splitlines(), 1):
        if not line or line.startswith("#"):
            continue
        try:
            expected, relative = line.split("  ", 1)
        except ValueError as exc:
            raise RuntimeError(f"SHA256SUMS:{line_number}: malformed line") from exc
        pure = PurePosixPath(relative)
        if pure.is_absolute() or ".." in pure.parts:
            raise RuntimeError(f"SHA256SUMS:{line_number}: unsafe path {relative}")
        if relative in seen:
            raise RuntimeError(f"SHA256SUMS:{line_number}: duplicate path {relative}")
        seen.add(relative)
        actual = _sha256((COMPAT_ROOT / relative).read_bytes())
        if actual != expected:
            raise RuntimeError(f"hash mismatch for {relative}: {actual} != {expected}")

    corpus_files = {
        path.relative_to(COMPAT_ROOT).as_posix()
        for directory in (COMPAT_ROOT / "fixtures", COMPAT_ROOT / "golden")
        for path in directory.rglob("*")
        if path.is_file()
    }
    if not corpus_files.issubset(seen):
        missing = sorted(corpus_files - seen)
        raise RuntimeError(f"unhashed corpus files: {missing}")

    required = {
        "README.md",
        "capture-baseline.sh",
        "compatibility-ledger.md",
        "manifest.json",
        "replay_oracle.py",
        "validate.sh",
    }
    if not required.issubset(seen):
        raise RuntimeError(f"unhashed required files: {sorted(required - seen)}")


def _validate_compatibility_disposition(
    manifest: dict[str, Any], all_case_keys: set[tuple[str, str]]
) -> None:
    disposition = manifest.get("compatibility_disposition", {})
    if disposition.get("schema") != "srvls-compatibility-disposition-v1":
        raise RuntimeError("compatibility disposition schema is missing or wrong")
    if disposition.get("default") != "inherited":
        raise RuntimeError("compatibility disposition default must be inherited")

    deviations = disposition.get("approved_deviations")
    if not isinstance(deviations, list):
        raise RuntimeError("approved deviations must be a list")
    case_keys = [(row.get("matrix_id"), row.get("case_id")) for row in deviations]
    if len(case_keys) != len(set(case_keys)):
        raise RuntimeError("a compatibility case has multiple dispositions")
    expected_keys = {("cli", case_id) for case_id in EXPECTED_APPROVED_DEVIATIONS}
    if set(case_keys) != expected_keys:
        difference = sorted(set(case_keys) ^ expected_keys)
        raise RuntimeError(f"approved-deviation case set mismatch: {difference}")
    if not set(case_keys).issubset(all_case_keys):
        raise RuntimeError("an approved deviation names an unknown frozen case")

    required_row_keys = {
        "matrix_id",
        "case_id",
        "ledger_entry",
        "old_behavior_version",
        "new_behavior_version",
        "migration_window",
        "replacement_assertion",
        "consumer_dispositions",
    }
    for row in deviations:
        case_id = row["case_id"]
        if set(row) != required_row_keys:
            raise RuntimeError(f"{case_id}: deviation fields are not exhaustive")
        if row["ledger_entry"] != "COMPAT-0002":
            raise RuntimeError(f"{case_id}: wrong compatibility-ledger entry")
        if row["matrix_id"] != "cli":
            raise RuntimeError(f"{case_id}: wrong compatibility matrix")
        if row["old_behavior_version"] != "Python baseline v1":
            raise RuntimeError(f"{case_id}: wrong old behavior version")
        if row["new_behavior_version"] != "Rust CLI v1":
            raise RuntimeError(f"{case_id}: wrong new behavior version")
        if row["migration_window"] != (
            "The Python baseline v1 golden remains immutable historical evidence; "
            "Rust CLI v1 and later apply this replacement assertion."
        ):
            raise RuntimeError(f"{case_id}: migration window is not frozen")
        if row["replacement_assertion"] != EXPECTED_APPROVED_DEVIATIONS[case_id]:
            raise RuntimeError(f"{case_id}: replacement assertion differs")
        consumers = row["consumer_dispositions"]
        if set(consumers) != EXPECTED_AFFECTED_CONSUMERS:
            raise RuntimeError(f"{case_id}: consumer disposition set differs")
        if not all(isinstance(value, str) and value for value in consumers.values()):
            raise RuntimeError(f"{case_id}: empty consumer disposition")

    inherited = all_case_keys - set(case_keys)
    if len(all_case_keys) != 94 or len(inherited) != 90:
        raise RuntimeError(
            f"compatibility partition must be 90 inherited plus 4 deviations, "
            f"found {len(inherited)} plus {len(case_keys)}"
        )


def validate() -> None:
    manifest = _load_manifest()
    source = manifest["source"]
    expected_source = {
        "frozen_parent": FROZEN_PARENT,
        "git_blob_sha1": FROZEN_BLOB_SHA1,
        "path": FROZEN_PATH,
        "sha256": FROZEN_SHA256,
        "size": FROZEN_SIZE,
    }
    if source != expected_source:
        raise RuntimeError("manifest source pin differs from validator source pin")
    if manifest.get("volatile_substitutions") != VOLATILE_SUBSTITUTIONS:
        raise RuntimeError("manifest volatile substitutions differ from renderer")
    frozen_source_bytes()
    _verify_hash_manifest()

    if set(manifest.get("coverage", {})) != REQUIRED_COVERAGE_KEYS:
        raise RuntimeError("manifest AD-9 coverage-key set is incomplete or expanded")
    if manifest.get("unsupported_legacy_provider", {}).get("provider") != "direct-process":
        raise RuntimeError("direct-process legacy exclusion is not explicit")
    expected_consumers = [
        {
            "name": "srvls-metrics.service",
            "surface": "--prom",
            "oracle": "output.prometheus",
            "definition_authority": "host-managed-user-systemd",
            "release_oracle": (
                "release-transaction-v1/brownfield-consumer-pairs.json#metrics"
            ),
        },
        {
            "name": "srvls-snapshot.service",
            "surface": "--md",
            "oracle": "output.markdown",
            "definition_authority": "host-managed-user-systemd",
            "release_oracle": (
                "release-transaction-v1/brownfield-consumer-pairs.json#snapshot"
            ),
        },
        {
            "name": "legacy fzf preview and action bindings",
            "surface": "--fzf, inspect, stop, restart, disable",
            "oracle": (
                "flags.fzf-present-bindings plus inspection and action matrices"
            ),
        },
    ]
    if manifest.get("deployed_consumers") != expected_consumers:
        raise RuntimeError("named deployed-consumer inventory/authority drift")

    fixture_paths: set[str] = set()
    golden_paths: set[str] = set()
    all_case_keys: set[tuple[str, str]] = set()
    rendered_case_count = 0
    for case in manifest["matrices"]:
        fixture_relative = case["fixture"]
        golden_relative = case["golden"]
        fixture_paths.add(fixture_relative)
        golden_paths.add(golden_relative)
        actual = render_fixture(COMPAT_ROOT / fixture_relative)
        expected = (COMPAT_ROOT / golden_relative).read_bytes()
        if actual != expected:
            raise RuntimeError(
                f"oracle mismatch for {fixture_relative} -> {golden_relative}"
            )
        rendered = json.loads(actual)
        actual_case_ids = [row["case_id"] for row in rendered["cases"]]
        if len(actual_case_ids) != len(set(actual_case_ids)):
            raise RuntimeError(f"duplicate case ID inside matrix {case['id']}")
        if set(actual_case_ids) != EXPECTED_CASE_IDS[case["id"]]:
            difference = sorted(set(actual_case_ids) ^ EXPECTED_CASE_IDS[case["id"]])
            raise RuntimeError(f"case coverage mismatch for {case['id']}: {difference}")
        matrix_case_keys = {(case["id"], case_id) for case_id in actual_case_ids}
        if all_case_keys.intersection(matrix_case_keys):
            raise RuntimeError(f"case identity repeated within matrix: {case['id']}")
        all_case_keys.update(matrix_case_keys)
        rendered_case_count += len(actual_case_ids)
        print(f"  replay: {case['id']}: ok")

    actual_fixtures = {
        path.relative_to(COMPAT_ROOT).as_posix()
        for path in (COMPAT_ROOT / "fixtures").glob("*.json")
    }
    actual_goldens = {
        path.relative_to(COMPAT_ROOT).as_posix()
        for path in (COMPAT_ROOT / "golden").glob("*.json")
    }
    if fixture_paths != actual_fixtures:
        raise RuntimeError(
            f"manifest fixture set mismatch: {sorted(fixture_paths ^ actual_fixtures)}"
        )
    if golden_paths != actual_goldens:
        raise RuntimeError(
            f"manifest golden set mismatch: {sorted(golden_paths ^ actual_goldens)}"
        )
    if rendered_case_count != 94:
        raise RuntimeError(f"expected 94 frozen cases, found {rendered_case_count}")
    _validate_compatibility_disposition(manifest, all_case_keys)
    print("  source pin: ok")
    print("  immutable hashes: ok")
    print("  AD-9 coverage: 90 inherited + 4 approved deviations: ok")
    print("PASS: frozen srvls compatibility oracle")


def capture(output: Path) -> None:
    resolved = output.resolve()
    try:
        resolved.relative_to(REPO_ROOT)
    except ValueError:
        pass
    else:
        raise RuntimeError("capture output must be outside the repository")
    if resolved.exists():
        raise RuntimeError(f"capture output already exists: {resolved}")
    resolved.mkdir(parents=True)
    manifest = _load_manifest()
    frozen_source_bytes()
    for matrix in manifest["matrices"]:
        destination = resolved / Path(matrix["golden"]).name
        destination.write_bytes(render_fixture(COMPAT_ROOT / matrix["fixture"]))
        print(destination)


def main() -> None:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    render_parser = subparsers.add_parser("render")
    render_parser.add_argument("fixture", type=Path)
    capture_parser = subparsers.add_parser("capture")
    capture_parser.add_argument("--output", required=True, type=Path)
    subparsers.add_parser("validate")
    subparsers.add_parser("verify-source")
    args = parser.parse_args()

    if args.command == "render":
        sys.stdout.buffer.write(render_fixture(args.fixture))
    elif args.command == "capture":
        capture(args.output)
    elif args.command == "validate":
        validate()
    elif args.command == "verify-source":
        frozen_source_bytes()
        print(
            f"{FROZEN_PARENT}:{FROZEN_PATH} {FROZEN_BLOB_SHA1} {FROZEN_SHA256} {FROZEN_SIZE}"
        )


if __name__ == "__main__":
    main()
