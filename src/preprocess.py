import os
import cv2
import numpy as np
from pathlib import Path
from tqdm import tqdm  # Để hiển thị thanh tiến trình

# ================== CẤU HÌNH ==================
# INPUT_DIR = "dataset/pothole_dataset/train/images"      # Thư mục ảnh gốc
# OUTPUT_DIR = "dataset/pothole_dataset/train/images_preprocessed_416"  # Thư mục lưu ảnh đã xử lý
INPUT_DIR = "test"
OUTPUT_DIR = "test_rs"

# Tạo thư mục đầu ra
Path(INPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
# ===============================================
def preprocess_and_save(image_path, save_path):
    """
    Đọc ảnh → Resize về 416x416 → Chuẩn hóa [0,1] → Lưu lại
    """
    IMG_SIZE = 416  # Resize về 416x416
    img = cv2.imread(image_path)
    if img is None:
        print(f"Không đọc được: {image_path}")
        return

    # Resize về 416x416
    img_resized = cv2.resize(img, (IMG_SIZE, IMG_SIZE), interpolation=cv2.INTER_LINEAR)

    # Chuẩn hóa về [0, 1]
    img_normalized = img_resized.astype(np.float32) / 255.0

    # Chuyển lại về uint8 để lưu file
    img_to_save = (img_normalized * 255).astype(np.uint8)

    # Lưu ảnh
    cv2.imwrite(save_path, img_to_save)

# =============== XỬ LÝ TOÀN BỘ ẢNH ===============
def main():
    # Lấy danh sách tất cả ảnh
    extensions = (".jpg", ".jpeg", ".png", ".bmp", ".tiff")
    image_files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(extensions)]

    for filename in tqdm(image_files, desc="Đang tiền xử lý 1"):
        input_path = os.path.join(INPUT_DIR, filename)
        output_path = os.path.join(OUTPUT_DIR, filename)
        preprocess_and_save(input_path, output_path)

    print(f"\nHoàn tất! Kết quả đã được lưu tại:\n{OUTPUT_DIR}")

if __name__ == "__main__":
    main()