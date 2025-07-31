import torch
import torch.nn.functional as F
from PIL import Image
import numpy as np

from model import model, transform
from schemas.PixelData import PixelData


def predict(data: PixelData):
    arr = np.array(data.pixels, dtype=np.uint8)

    img = Image.fromarray(arr, mode="L")
    
    tensor = transform(img).unsqueeze(0)

    with torch.no_grad():
        output = model(tensor)
        output = F.softmax(output)
        
        digit = torch.argmax(output, dim=1).item()
        probability = round(100 * output[0, digit].item(), 0)

        return probability, digit 