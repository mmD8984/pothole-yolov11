import cv2
import os
import random
import numpy as np
from glob import glob

INPUT_DIR = "images/"
OUTPUT_DIR = "aug_images/"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 1. Xoay ảnh
def rotate_image(image, angle):
    h, w = image.shape[:2]
    M = cv2.getRotationMatrix2D((w//2, h//2), angle, 1)
    return cv2.warpAffine(image, M, (w, h))

# 2. Chỉnh sáng
def adjust_brightness(image, value=30):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    v = np.clip(v + value, 0, 255)
    hsv = cv2.merge((h, s, v))

    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

# 3. Chỉnh độ tương phản
def adjust_contrast(image, alpha=1.4):
    # alpha > 1 tăng tương phản, alpha < 1 giảm tương phản
    return cv2.convertScaleAbs(image, alpha=alpha, beta=0)

# 4. Lật ảnh
def flip_image(image):
    return cv2.flip(image, 1)   # lật ngang

# Xử lý từng ảnh
for img_path in glob(INPUT_DIR + "/*.jpg"):
    img = cv2.imread(img_path)
    name = os.path.basename(img_path).split('.')[0]

    # Tăng cường 1: xoay
    rotated = rotate_image(img, angle=random.randint(-25, 25))
    cv2.imwrite(f"{OUTPUT_DIR}/{name}_rotate.jpg", rotated)

    # Tăng cường 2: sáng
    bright = adjust_brightness(img, value=random.randint(20, 60))
    cv2.imwrite(f"{OUTPUT_DIR}/{name}_bright.jpg", bright)

    # Tăng cường 3: tương phản
    contrast = adjust_contrast(img, alpha=random.uniform(1.2, 1.6))
    cv2.imwrite(f"{OUTPUT_DIR}/{name}_contrast.jpg", contrast)

    # Tăng cường 4: lật ngang
    flipped = flip_image(img)
    cv2.imwrite(f"{OUTPUT_DIR}/{name}_flip.jpg", flipped)

print("✔ Tăng cường dữ liệu hoàn tất!")
