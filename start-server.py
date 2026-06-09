"""
DataLens - Local Server Launcher
Double-click start-server.bat to run this automatically.
Or run: python start-server.py
"""
import http.server
import socketserver
import webbrowser
import os
import sys
import threading
import time

PORT = 8000
FILE = "data-analysis-tool.html"

# Change to the folder where this script lives
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        # Suppress noisy request logs
        pass

def open_browser():
    time.sleep(1.2)
    url = f"http://localhost:{PORT}/{FILE}"
    print(f"  Opening: {url}")
    webbrowser.open(url)

print("=" * 50)
print("  DataLens — Local Server")
print("=" * 50)
print(f"  Serving on: http://localhost:{PORT}")
print(f"  Opening:    {FILE}")
print()
print("  Keep this window open while using the tool.")
print("  Press Ctrl+C to stop the server.")
print("=" * 50)

# Try port 8000, fall back to 8080, then 3000
for port in [8000, 8080, 3000, 5000]:
    try:
        httpd = socketserver.TCPServer(("", port), Handler)
        PORT = port
        break
    except OSError:
        print(f"  Port {port} busy, trying next...")
        continue
else:
    print("\n  ERROR: Could not find a free port (tried 8000, 8080, 3000, 5000).")
    print("  Close other applications and try again.")
    input("  Press Enter to exit...")
    sys.exit(1)

# Open browser in background thread
threading.Thread(target=open_browser, daemon=True).start()

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\n\n  Server stopped. Goodbye!")
    httpd.shutdown()
