# import torch
#
# # Kiểm tra phiên bản PyTorch
# print("PyTorch version:", torch.__version__)
#
# # Kiểm tra CUDA
# if torch.cuda.is_available():
#     print("CUDA is available!")
#     print("GPU name:", torch.cuda.get_device_name(0))
#     print("Number of GPUs:", torch.cuda.device_count())
#     # Tạo tensor trên GPU để test
#     x = torch.randn(3, 3).cuda()
#     print("Tensor on GPU:\n", x)
# else:
#     print("CUDA is not available. PyTorch đang chạy trên CPU.")
# import torch
#
# print("PyTorch version:", torch.__version__)
# print("CUDA available:", torch.cuda.is_available())
# if torch.cuda.is_available():
#     print("CUDA version:", torch.version.cuda)
#     print("GPU name:", torch.cuda.get_device_name(0))
#-----------------------------------------
import torch
from ultralytics import YOLO

print("CUDA available:", torch.cuda.is_available())
print("GPU:", torch.cuda.get_device_name(0))

# Load model YOLOv11 nhỏ nhất để test
model = YOLO("yolo11n.pt")

# Chạy thử inference
results = model("test.jpg", device=0)   # device=0 = GPU
print("Done!")
