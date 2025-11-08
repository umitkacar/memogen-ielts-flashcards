"""Tests for MEMOGEN CLI."""

from unittest.mock import patch

from memogen.cli import main


class TestCLI:
    """Tests for command-line interface."""

    def test_version_flag(self, capsys) -> None:
        """Test --version flag."""
        with patch("sys.argv", ["memogen", "--version"]):
            try:
                main()
            except SystemExit:
                pass

            captured = capsys.readouterr()
            assert "MEMOGEN" in captured.out

    def test_help_output(self, capsys) -> None:
        """Test help output."""
        with patch("sys.argv", ["memogen", "--help"]):
            try:
                main()
            except SystemExit:
                pass

            captured = capsys.readouterr()
            assert "Master IELTS Vocabulary" in captured.out
