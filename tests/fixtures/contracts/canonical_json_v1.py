#!/usr/bin/env python3
"""Normative CanonicalJsonV1 and uppercase-percent codecs from AD-24."""

from __future__ import annotations

import json
import unicodedata
from typing import Any


UNRESERVED_BYTES = frozenset(
    b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~"
)
MIN_CANONICAL_INTEGER = -(1 << 63)
MAX_CANONICAL_INTEGER = (1 << 64) - 1


class CanonicalJsonError(ValueError):
    """Raised when bytes or values are not CanonicalJsonV1."""


class CanonicalPercentError(ValueError):
    """Raised when text is not the sole AD-24 uppercase-percent spelling."""


def _reject_float(token: str) -> Any:
    raise CanonicalJsonError(f"floating-point value is forbidden: {token}")


def _reject_constant(token: str) -> Any:
    raise CanonicalJsonError(f"non-finite numeric value is forbidden: {token}")


def _pairs_no_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise CanonicalJsonError(f"duplicate object key: {key!r}")
        result[key] = value
    return result


def _canonical_string(value: str) -> bytes:
    if unicodedata.normalize("NFC", value) != value:
        raise CanonicalJsonError("string is not NFC")
    output: list[str] = ['"']
    for character in value:
        codepoint = ord(character)
        if 0xD800 <= codepoint <= 0xDFFF:
            raise CanonicalJsonError("surrogate code point is forbidden")
        if character == '"':
            output.append('\\"')
        elif character == "\\":
            output.append("\\\\")
        elif codepoint <= 0x1F:
            output.append(f"\\u00{codepoint:02X}")
        else:
            output.append(character)
    output.append('"')
    return "".join(output).encode("utf-8")


def canonical_json_bytes(value: Any) -> bytes:
    """Serialize one value using the exact AD-24 representation."""
    if value is None:
        raise CanonicalJsonError("null is forbidden; use a declared tagged union")
    if value is True:
        return b"true"
    if value is False:
        return b"false"
    if type(value) is int:
        if not MIN_CANONICAL_INTEGER <= value <= MAX_CANONICAL_INTEGER:
            raise CanonicalJsonError(
                "integer is outside the CanonicalJsonV1 i64/u64 union"
            )
        return str(value).encode("ascii")
    if isinstance(value, float):
        raise CanonicalJsonError("floating-point values are forbidden")
    if isinstance(value, str):
        return _canonical_string(value)
    if isinstance(value, list):
        return b"[" + b",".join(canonical_json_bytes(item) for item in value) + b"]"
    if isinstance(value, dict):
        fields: list[bytes] = []
        for key, child in value.items():
            if not isinstance(key, str):
                raise CanonicalJsonError("object key is not a string")
            fields.append(_canonical_string(key) + b":" + canonical_json_bytes(child))
        return b"{" + b",".join(fields) + b"}"
    raise CanonicalJsonError(f"unsupported JSON value type: {type(value).__name__}")


def parse_canonical_json(data: bytes) -> Any:
    """Parse bytes and reject every representation alias."""
    if data.startswith(b"\xef\xbb\xbf"):
        raise CanonicalJsonError("UTF-8 BOM is forbidden")
    try:
        text = data.decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        raise CanonicalJsonError(f"invalid UTF-8: {exc}") from exc
    try:
        value = json.loads(
            text,
            object_pairs_hook=_pairs_no_duplicates,
            parse_float=_reject_float,
            parse_constant=_reject_constant,
        )
    except json.JSONDecodeError as exc:
        raise CanonicalJsonError(f"invalid JSON: {exc}") from exc
    canonical = canonical_json_bytes(value)
    if canonical != data:
        raise CanonicalJsonError("bytes are not the sole CanonicalJsonV1 spelling")
    return value


def require_key_order(value: dict[str, Any], expected: list[str], context: str) -> None:
    """Enforce the schema-declared order that CanonicalJsonV1 preserves."""
    if list(value) != expected:
        raise CanonicalJsonError(f"{context}: schema key order mismatch")


def percent_encode(data: bytes) -> str:
    """Encode bytes with only RFC 3986 unreserved bytes left literal."""
    return "".join(
        chr(byte) if byte in UNRESERVED_BYTES else f"%{byte:02X}" for byte in data
    )


def percent_decode(value: Any) -> bytes:
    """Decode only the unique uppercase-percent representation from AD-24."""
    if not isinstance(value, str):
        raise CanonicalPercentError("encoded value is not text")
    output = bytearray()
    index = 0
    while index < len(value):
        character = value[index]
        if character == "%":
            if index + 2 >= len(value):
                raise CanonicalPercentError("truncated percent escape")
            token = value[index + 1 : index + 3]
            if len(token) != 2 or any(
                child not in "0123456789ABCDEF" for child in token
            ):
                raise CanonicalPercentError("percent escape is not uppercase hexadecimal")
            byte = int(token, 16)
            if byte in UNRESERVED_BYTES:
                raise CanonicalPercentError("unreserved byte is over-escaped")
            output.append(byte)
            index += 3
            continue
        codepoint = ord(character)
        if codepoint > 0x7F or codepoint not in UNRESERVED_BYTES:
            raise CanonicalPercentError("non-unreserved byte is not percent-escaped")
        output.append(codepoint)
        index += 1
    decoded = bytes(output)
    if percent_encode(decoded) != value:
        raise CanonicalPercentError("encoded value is not canonical")
    return decoded


def normalize_linux_path(raw: bytes) -> bytes:
    """Return the sole AD-24 absolute Linux path spelling or reject it.

    Paths remain arbitrary raw bytes, but their structural spelling is closed:
    no NUL, no parent traversal, no repeated slash or dot component, and no
    non-root trailing slash.
    """
    if not raw.startswith(b"/"):
        raise CanonicalPercentError("Linux path is not absolute")
    if b"\0" in raw:
        raise CanonicalPercentError("Linux path contains NUL")
    components: list[bytes] = []
    for component in raw.split(b"/"):
        if component in {b"", b"."}:
            continue
        if component == b"..":
            raise CanonicalPercentError("Linux path contains parent traversal")
        components.append(component)
    normalized = b"/" + b"/".join(components)
    if raw != normalized:
        raise CanonicalPercentError("Linux path is not normalized")
    return normalized


def percent_decode_linux_path(value: Any) -> bytes:
    """Decode the unique uppercase-percent spelling of a normalized path."""
    return normalize_linux_path(percent_decode(value))


def validate_negative_vectors() -> None:
    """Prove aliases forbidden by AD-24 are rejected by this implementation."""
    rejected = [
        b'{"x":"\\b"}',
        b'{"x":"\\t"}',
        b'{"x":"\\n"}',
        b'{"x":"\\f"}',
        b'{"x":"\\r"}',
        b'{"x":"\\/"}',
        b'{"x":1.5}',
        b'{"x":1e2}',
        b'{"x":NaN}',
        b'{"x":Infinity}',
        b'{"x":-Infinity}',
        '{"x":"e\u0301"}'.encode("utf-8"),
        b'{"x":"\\u001f"}',
        b'{"x":"\\u00E9"}',
        b'{"x":"\\ud800"}',
        b'{"x":"\\ud800\\udc00"}',
        b'{"x":-0}',
        b'{"x":18446744073709551616}',
        b'{"x":-9223372036854775809}',
        b'{"x":null}',
        b'{"x":1,"x":2}',
        b' {"x":1}',
        b'{"x":1} ',
        b'{"x":1}\n',
        b'\xef\xbb\xbf{"x":1}',
    ]
    for raw in rejected:
        try:
            parse_canonical_json(raw)
        except CanonicalJsonError:
            continue
        raise CanonicalJsonError(f"negative CanonicalJsonV1 vector accepted: {raw!r}")
    expected = b'{"control":"\\u000A","quote":"\\\"","slash":"/","integer":0}'
    actual = canonical_json_bytes(
        {"control": "\n", "quote": '"', "slash": "/", "integer": 0}
    )
    if actual != expected or parse_canonical_json(expected) != {
        "control": "\n",
        "quote": '"',
        "slash": "/",
        "integer": 0,
    }:
        raise CanonicalJsonError("positive CanonicalJsonV1 control vector drift")
    for boundary in (MIN_CANONICAL_INTEGER, MAX_CANONICAL_INTEGER):
        raw = str(boundary).encode("ascii")
        if canonical_json_bytes(boundary) != raw or parse_canonical_json(raw) != boundary:
            raise CanonicalJsonError("CanonicalJsonV1 integer boundary drift")
    try:
        require_key_order({"second": 2, "first": 1}, ["first", "second"], "negative")
    except CanonicalJsonError:
        pass
    else:
        raise CanonicalJsonError("alternate schema key order was accepted")
    for raw in ("/home", "%2fhome", "%68ome", "café"):
        try:
            percent_decode(raw)
        except CanonicalPercentError:
            continue
        raise CanonicalPercentError(f"negative percent vector accepted: {raw!r}")
    canonical_path = "%2Fhome%2Ftest%2Fstate.sqlite3"
    if percent_encode(percent_decode(canonical_path)) != canonical_path:
        raise CanonicalPercentError("positive percent round trip drift")
    if percent_decode_linux_path(canonical_path) != b"/home/test/state.sqlite3":
        raise CanonicalPercentError("positive normalized path drift")
    for raw in (
        "%2Fhome%2F%2Ftest",
        "%2Fhome%2F.%2Ftest",
        "%2Fhome%2F..%2Ftest",
        "%2Fhome%2Ftest%2F",
        "%2Fhome%00test",
        "relative",
        "",
    ):
        try:
            percent_decode_linux_path(raw)
        except CanonicalPercentError:
            continue
        raise CanonicalPercentError(f"negative Linux path vector accepted: {raw!r}")
