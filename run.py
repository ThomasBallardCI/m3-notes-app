"""
QuickNote Application Entry Point

Description:
    This module serves as the entry point for the QuickNote application. It launches
    the Flask application using the Flask development server when executed directly.
    The server configuration is based on environment variables defined in the 'os'
    module, specifying the host, port, and debug mode.

Dependencies:
    - os: Provides access to the operating system environment.
    - quicknote.app: The Flask application instance for QuickNote.
"""
import os
from quicknote import app


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )
