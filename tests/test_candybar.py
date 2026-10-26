#!/usr/bin/env python3
"""Collector contract: Candybar jobs remain in srvls after their native timer retires."""

import io
import json
import runpy
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

SRVLS = runpy.run_path(str(Path(__file__).resolve().parents[1] / "srvls"), run_name="srvls_test")


class Response(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.close()


class CandybarCollectorTest(unittest.TestCase):
    def test_live_registry_items_in_every_output(self):
        bars = [
            {"id": "id-a", "name": "cache-prune-daily", "description": "prune", "schedule": "23 5 * * *", "timezone": "America/New_York", "enabled": True},
            {"id": "id-b", "name": "paused-job", "description": "pause", "schedule": "*/5 * * * *", "timezone": "UTC", "enabled": False},
        ]
        with patch("urllib.request.urlopen", return_value=Response(json.dumps(bars).encode())) as fetch:
            items = SRVLS["collect_candybar"]()
        self.assertEqual([i["name"] for i in items], ["cache-prune-daily", "paused-job"])
        self.assertEqual([i["state"] for i in items], ["enabled", "disabled"])
        self.assertIn("America/New_York", items[0]["schedule"])
        self.assertEqual(items[1]["schedule"], "*/5 * * * *")
        self.assertEqual(items[0]["source"], "candybar")
        self.assertEqual(fetch.call_args.kwargs["timeout"], 5)
        with patch("builtins.print") as out:
            SRVLS["out_prom"](items)
        self.assertTrue(any("srvls_items{type=\"candybar\",state=\"enabled\"}" in str(c) for c in out.call_args_list))
        with patch("builtins.print") as out:
            SRVLS["out_md"](items)
        self.assertTrue(any("## candybar (2)" in str(c) for c in out.call_args_list))

    def test_unreachable_api_does_not_break_inventory(self):
        with patch("urllib.request.urlopen", side_effect=OSError("unreachable")):
            self.assertEqual(SRVLS["collect_candybar"](), [])


if __name__ == "__main__":
    unittest.main()
