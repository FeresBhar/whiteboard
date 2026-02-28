#!/usr/bin/env python3
"""
Health check script for the collaborative whiteboard
"""

import requests
import json
import sys
import time

def check_backend_health(url):
    """Check if backend is healthy"""
    try:
        # Remove protocol if present
        if url.startswith('http://') or url.startswith('https://'):
            clean_url = url
        else:
            clean_url = f"https://{url}" if 'railway' in url or 'render' in url else f"http://{url}"
        
        print(f"🔍 Checking backend health: {clean_url}")
        
        # Check main endpoint
        response = requests.get(f"{clean_url}/", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Main endpoint: {data}")
        else:
            print(f"❌ Main endpoint failed: {response.status_code}")
            return False
        
        # Check health endpoint
        try:
            response = requests.get(f"{clean_url}/health", timeout=10)
            if response.status_code == 200:
                data = response.json()
                print(f"✅ Health endpoint: {data}")
            else:
                print(f"⚠️ Health endpoint: {response.status_code}")
        except:
            print("⚠️ Health endpoint not available (this is OK)")
        
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Backend health check failed: {e}")
        return False

def check_websocket_connection(url):
    """Check if WebSocket connection works"""
    try:
        import websocket
        
        # Determine protocol
        if 'railway' in url or 'render' in url or 'fly' in url:
            ws_url = f"wss://{url}/ws/test"
        else:
            ws_url = f"ws://{url}/ws/test"
        
        print(f"🔌 Testing WebSocket: {ws_url}")
        
        def on_open(ws):
            print("✅ WebSocket connection opened")
            ws.send(json.dumps({"type": "test", "message": "health check"}))
            
        def on_message(ws, message):
            print(f"✅ WebSocket message received: {message}")
            ws.close()
            
        def on_error(ws, error):
            print(f"❌ WebSocket error: {error}")
            
        def on_close(ws, close_status_code, close_msg):
            print("🔌 WebSocket connection closed")
        
        ws = websocket.WebSocketApp(ws_url,
                                  on_open=on_open,
                                  on_message=on_message,
                                  on_error=on_error,
                                  on_close=on_close)
        
        ws.run_forever(timeout=10)
        return True
        
    except ImportError:
        print("⚠️ websocket-client not installed, skipping WebSocket test")
        print("   Install with: pip install websocket-client")
        return True
    except Exception as e:
        print(f"❌ WebSocket test failed: {e}")
        return False

def main():
    """Main health check function"""
    print("🏥 Collaborative Whiteboard Health Check")
    print("=" * 40)
    
    if len(sys.argv) < 2:
        print("Usage: python health_check.py <backend_url>")
        print("Example: python health_check.py your-app.railway.app")
        print("Example: python health_check.py localhost:8000")
        sys.exit(1)
    
    backend_url = sys.argv[1]
    
    # Remove protocol if present for consistency
    if backend_url.startswith('http://') or backend_url.startswith('https://'):
        backend_url = backend_url.split('://', 1)[1]
    
    print(f"🎯 Target: {backend_url}")
    print()
    
    # Check backend health
    backend_ok = check_backend_health(backend_url)
    print()
    
    # Check WebSocket (optional)
    websocket_ok = check_websocket_connection(backend_url)
    print()
    
    # Summary
    print("=" * 40)
    if backend_ok:
        print("🎉 Backend is healthy!")
        if websocket_ok:
            print("🎉 WebSocket is working!")
        print()
        print("🚀 Your whiteboard should be working!")
        print(f"   Backend: https://{backend_url}")
        print("   Update BACKEND_URL in canvas.js to this URL")
    else:
        print("❌ Backend health check failed")
        print("   Check your deployment and try again")
        sys.exit(1)

if __name__ == "__main__":
    main()