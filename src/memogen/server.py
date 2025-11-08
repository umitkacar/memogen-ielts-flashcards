"""Web server for MEMOGEN flashcard application."""

import http.server
import socketserver
from pathlib import Path


def start_server(host: str = "127.0.0.1", port: int = 8000) -> None:
    """Start the MEMOGEN web server.

    Args:
        host: Host address to bind to
        port: Port number to listen on
    """
    # Get the project root directory
    project_root = Path(__file__).parent.parent.parent

    # Change to project root directory
    import os

    os.chdir(project_root)

    class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
        """Custom HTTP request handler with better logging."""

        def log_message(self, format: str, *args: object) -> None:
            """Log HTTP requests with custom formatting."""
            print(f"[MEMOGEN] {self.address_string()} - {format % args}")

    with socketserver.TCPServer((host, port), CustomHTTPRequestHandler) as httpd:
        print("🎴 MEMOGEN Server Starting...")
        print(f"📂 Serving from: {project_root}")
        print(f"🌐 Access at: http://{host}:{port}")
        print("🎯 Press Ctrl+C to stop")
        print()

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n🛑 Server stopped.")
