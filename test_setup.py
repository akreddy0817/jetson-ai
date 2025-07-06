import torch
import cv2

print("🚀 Cursor + Jetson setup test")
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"OpenCV version: {cv2.__version__}")
print("✅ Everything working!")