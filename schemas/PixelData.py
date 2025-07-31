from pydantic import BaseModel

class PixelData(BaseModel):
    pixels: list[list[int]]