"""Command-line interface for MEMOGEN."""

import argparse
import sys
from pathlib import Path

from memogen import __version__


def main() -> int:
    """Main CLI entry point.

    Returns:
        Exit code (0 for success, non-zero for errors)
    """
    parser = argparse.ArgumentParser(
        description="MEMOGEN - Master IELTS Vocabulary with 3D Interactive Flashcards",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"MEMOGEN {__version__}",
    )

    parser.add_argument(
        "--serve",
        action="store_true",
        help="Start the web server",
    )

    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port to run the server on (default: 8000)",
    )

    parser.add_argument(
        "--host",
        type=str,
        default="127.0.0.1",
        help="Host to bind the server to (default: 127.0.0.1)",
    )

    args = parser.parse_args()

    if args.serve:
        from memogen.server import start_server

        start_server(host=args.host, port=args.port)
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
