from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from storage.client import redis_client
from websocket.manager import ConnectionManager
import json
import os

app = FastAPI()
manager = ConnectionManager()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health():
    return {"status": "ok", "message": "Collaborative Whiteboard API"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "redis": "connected"}

@app.websocket("/ws/{room_id}")
async def websocket_endpoint(ws: WebSocket, room_id: str):
    await ws.accept()
    manager.add(room_id, ws)
    
    try:
        while True:
            data = await ws.receive_text()
            msg = json.loads(data)
            
            # Store in Redis for persistence
            if msg.get('type') == 'draw':
                await redis_client.rpush(f"room:{room_id}:page:{msg['page']}", data)
            elif msg.get('type') == 'undo':
                await redis_client.rpop(f"room:{room_id}:page:{msg['page']}")
            elif msg.get('type') == 'clear':
                await redis_client.delete(f"room:{room_id}:page:{msg['page']}")
            elif msg.get('type') == 'delete_page':
                await redis_client.delete(f"room:{room_id}:page:{msg['page']}")
            
            # Broadcast to all clients including sender
            await manager.broadcast(room_id, data)
    except WebSocketDisconnect:
        manager.remove(room_id, ws)