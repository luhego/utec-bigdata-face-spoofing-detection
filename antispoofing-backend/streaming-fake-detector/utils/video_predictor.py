import numpy as np

import torch
import torch.nn as nn
import numpy as np

NUM_CLASSES = 4
BATCH_SIZE = 64
MODEL_PATH = "files/cnn_model_params_casia.pt"
device = torch.device("cpu")


class CNN(nn.Module):
    def __init__(self, num_classes=0):
        super(CNN, self).__init__()
        self.layer1 = nn.Sequential(
            nn.Conv2d(
                in_channels=1, out_channels=16, kernel_size=3, stride=1, padding=2
            ),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
        )
        self.layer2 = nn.Sequential(
            nn.Conv2d(16, 32, kernel_size=5, stride=1, padding=2),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
        )
        self.fc = nn.Linear(64 * 64 * 32, num_classes)

    def forward(self, x):
        out = self.layer1(x)
        out = self.layer2(out)
        out = out.reshape(out.size(0), -1)
        out = self.fc(out)
        return out


class VideoPredictor:
    def __init__(self):
        self.model = CNN(num_classes=NUM_CLASSES)
        self.model.load_state_dict(torch.load(MODEL_PATH, map_location=device))
        self.model.eval()

    def predict(self, loader):
        with torch.no_grad():
            for images in loader:
                images = images.to(device)
                outputs = self.model(images)
                _, predicted = torch.max(outputs.data, 1)

                return predicted

    def process(self, loader):
        print("Predicting video")
        predicted = self.predict(loader)
        return np.bincount(predicted).argmax()
