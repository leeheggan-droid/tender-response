"""Deterministic checks for the optional submission-text counter."""

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "check_limits.py"


class LimitTests(unittest.TestCase):
    def run_counter(self, content, *args):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "answer.txt"
            source.write_bytes(content.encode("utf-8"))
            return subprocess.run(
                [sys.executable, str(SCRIPT), str(source), *args],
                capture_output=True, text=True, check=False,
            )

    def test_exact_limit_and_headings_count(self):
        result = self.run_counter("Approach\nWe act.", "--max-words", "3")
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report["words"], 3)
        self.assertTrue(report["within_limits"])

    def test_excess_fails(self):
        result = self.run_counter("one two three", "--max-words", "2")
        self.assertEqual(result.returncode, 1)
        self.assertFalse(json.loads(result.stdout)["within_limits"])

    def test_unicode_units_and_combined_caps(self):
        for unit, count in [("codepoints", 4), ("utf16", 5), ("utf8-bytes", 8)]:
            with self.subTest(unit=unit):
                result = self.run_counter(
                    "A 😀é", "--character-unit", unit,
                    "--max-characters", str(count), "--max-words", "2",
                )
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(json.loads(result.stdout)["characters"], count)

    def test_crlf_is_normalised_but_whitespace_is_not_trimmed(self):
        result = self.run_counter(" x\r\ny ", "--max-characters", "5")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["characters"], 5)

    def test_empty_zero_limit(self):
        result = self.run_counter("", "--max-words", "0", "--max-characters", "0")
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_whitespace_word_convention(self):
        result = self.run_counter("client-focused don't 24/7\tteam\nready")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["words"], 5)

    def test_negative_limit_is_usage_error(self):
        result = self.run_counter("x", "--max-words", "-1")
        self.assertEqual(result.returncode, 2)
        self.assertIn("nonnegative", result.stderr)

    def test_either_combined_cap_can_fail(self):
        for words, characters in [(1, 20), (20, 1)]:
            with self.subTest(words=words, characters=characters):
                result = self.run_counter(
                    "one two", "--max-words", str(words),
                    "--max-characters", str(characters),
                )
                self.assertEqual(result.returncode, 1)

    def test_utf8_bom_is_not_submission_content(self):
        result = self.run_counter("\ufeffanswer", "--max-characters", "6")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["characters"], 6)

    def test_unreadable_input_is_error(self):
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run(
                [sys.executable, str(SCRIPT), str(Path(directory) / "absent.txt")],
                capture_output=True, text=True, check=False,
            )
        self.assertEqual(result.returncode, 2)
        self.assertIn("cannot read input", result.stderr)


if __name__ == "__main__":
    unittest.main()
