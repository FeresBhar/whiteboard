#!/usr/bin/env python3
"""
Quick test to check if the drawing issue is frontend or backend
"""

import asyncio
import websockets
import json

async def test_websocket():
    uri = "wss://whiteboard-fs5m.onrender.com/ws/room1"
    
    try:
        print(f"🔗 Connecting to: {uri}")
        async with websockets.connect(uri) as websocket:
            print("✅ Connected successfully!")
            
            # Send a test draw message
            test_message = {
                "type": "draw",
                "page": 1,
                "stroke_id": "test123",
                "x": 100,
                "y": 100,
                "color": "#ff0000",
                "thickness": 5
            }
            
            print(f"📤 Sending test message: {test_message}")
            await websocket.send(json.dumps(test_message))
            
            # Wait for response
            try:
                response = await asyncio.wait_for(websocket.recv(), timeout=5.0)
                print(f"📨 Received response: {response}")
            except asyncio.TimeoutError:
                print("⏰ No response received (this might be normal)")
            
            print("✅ WebSocket test completed successfully!")
            
    except Exception as e:
        print(f"❌ WebSocket test failed: {e}")

if __name__ == "__main__":
    asyncio.run(test_websocket())