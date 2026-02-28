class ConnectionManager:
    def __init__(self):
        self.rooms = {}

    def add(self, room, ws):
        self.rooms.setdefault(room, set()).add(ws)

    def remove(self, room, ws):
        if room in self.rooms:
            self.rooms[room].discard(ws)
            if not self.rooms[room]:
                del self.rooms[room]
    
    async def broadcast(self, room, message):
        if room in self.rooms:
            for ws in self.rooms[room]:
                await ws.send_text(message)