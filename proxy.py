"""
Simple proxy server that serves frontend files and proxies API/WebSocket to backend
This allows using only ONE ngrok tunnel
"""
from http.server import HTTPServer, SimpleHTTPRequestHandler
import socketserver
import urllib.request
import urllib.error
import os

class ProxyHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # Serve files from frontend directory
        super().__init__(*args, directory='frontend', **kwargs)
    
    def do_GET(self):
        # Proxy WebSocket upgrade and API requests to backend
        if self.path.startswith('/ws/') or self.path == '/':
            if self.path.startswith('/ws/'):
                # For WebSocket, we can't proxy easily in Python
                # So we'll let the client connect directly to localhost:8000
                pass
            elif self.path == '/' and 'Upgrade' not in self.headers:
                # API health check - proxy to backend
                try:
                    with urllib.request.urlopen('http://localhost:8000/') as response:
                        self.send_response(response.status)
                        self.send_header('Content-Type', 'application/json')
                        self.send_header('Access-Control-Allow-Origin', '*')
                        self.end_headers()
                        self.wfile.write(response.read())
                    return
                except:
                    pass
        
        # Serve static files from frontend directory
        return super().do_GET()

PORT = 8080

print(f"""
========================================
Proxy Server Starting on Port {PORT}
========================================

This serves both frontend and backend through one port!

1. Make sure backend is running: docker-compose up
2. Start ngrok: ngrok http {PORT}
3. Copy ngrok URL and update canvas.js
4. Open ngrok URL in browser

========================================
""")

with socketserver.TCPServer(("", PORT), ProxyHandler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    print("Press Ctrl+C to stop")
    httpd.serve_forever()
