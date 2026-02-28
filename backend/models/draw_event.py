from pydantic import BaseModel

class DrawEvent(BaseModel):
    room_id: str
    stroke_id: str
    x: float
    y: float
    color: str
    thickness: int
    timestamp: float