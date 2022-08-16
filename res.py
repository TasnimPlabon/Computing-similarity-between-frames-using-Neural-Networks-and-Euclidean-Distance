from PIL import Image
import torchvision.transforms as transforms
import torch
import json
import cv2
import glob
from resnet_pytorch import ResNet
model = ResNet.from_pretrained("resnet18")


# Open image

input_image = Image.open("img.jpg")

# Preprocess image
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225]),
])
input_tensor = preprocess(input_image)
# create a mini-batch as expected by the model
input_batch = input_tensor.unsqueeze(0)
# Load class names
labels_map = json.load(open("labels_map.txt"))
labels_map = [labels_map[str(i)] for i in range(1000)]

# Classify with ResNet18
model = ResNet.from_pretrained("resnet18")
model.eval()

# move the input and model to GPU for speed if available
if torch.cuda.is_available():
    input_batch = input_batch.to("cuda")
    model.to("cuda")

with torch.no_grad():
    logits = model(input_batch)
preds = torch.topk(logits, k=5).indices.squeeze(0).tolist()

print("-----")
for idx in preds:
    label = labels_map[idx]
    prob = torch.softmax(logits, dim=1)[0, idx].item()
    print(f"{label:<75} ({prob * 100:.2f}%)")
model = ResNet.from_pretrained('resnet18')

# ... image preprocessing as in the classification example ...
inputs = torch.randn(1, 3, 224, 224)
print(inputs.shape)  # torch.Size([1, 3, 224, 224])

features = model.extract_features(inputs)
print(features.shape)  # torch.Size([1, 512, 1, 1])
