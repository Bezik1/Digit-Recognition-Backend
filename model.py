import torch
import torch.nn as nn
from torchvision import models, transforms


PATH = './parameters/digit_recognition.pth'
num_class = 10

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.Grayscale(num_output_channels=3),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5]*3, std=[0.5]*3)
])

device = torch.device("cpu")
model = models.resnet18(pretrained=True)
for param in model.parameters():
    param.requires_grad = False

num_fc_inputs = model.fc.in_features
model.fc = nn.Linear(num_fc_inputs, num_class)
model.to(device)
model.load_state_dict(torch.load(PATH, map_location=device))
model.eval()