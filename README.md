**Mô hình sử dụng là mô hình gì?**

* **Mô hình sử dụng** là **YOLOv8**, một phiên bản mới của dòng mô hình **You Only Look Once** (YOLO), chuyên dùng cho bài toán **object detection** và **semantic segmentation**. YOLOv8 kết hợp giữa tốc độ và độ chính xác cao, phù hợp cho các ứng dụng nhận diện ổ gà trong ảnh hoặc video thời gian thực.

---

 **Bài toán áp dụng là gì?**

* **Bài toán áp dụng** là **phát hiện và phân đoạn ổ gà** (pothole detection and segmentation) trên mặt đường. Mục tiêu là nhận diện vị trí và phân vùng chính xác các ổ gà trong ảnh, hỗ trợ công tác bảo trì và giám sát hạ tầng giao thông.

---

**Ứng dụng demo là gì?**

* **Ứng dụng demo** là một hệ thống nhận diện ổ gà tự động, cho phép người dùng:  
  * **Tải ảnh lên**: Người dùng có thể tải ảnh mặt đường lên hệ thống.  
  * **Nhận diện ổ gà**: Hệ thống sử dụng mô hình YOLOv8 để phát hiện và phân đoạn các ổ gà trong ảnh.  
  * **Hiển thị kết quả**: Kết quả nhận diện được hiển thị trực quan trên ảnh, với các ổ gà được đánh dấu rõ ràng.

---

**Chức năng của ứng dụng?**

* **Phát hiện ổ gà**: Xác định vị trí và kích thước của các ổ gà trong ảnh.  
* **Phân đoạn ổ gà**: Tạo mặt nạ phân vùng (segmentation mask) cho các ổ gà, giúp phân biệt rõ ràng với phần còn lại của mặt đường.  
* **Cảnh báo và lưu trữ**: Gửi cảnh báo khi phát hiện ổ gà và lưu trữ thông tin để theo dõi và xử lý sau này.

---

**Đơn vị đo hiệu suất mô hình? Quy trình tiền xử lý?**

* **Đơn vị đo hiệu suất mô hình**:  
  * **IoU (Intersection over Union)**: Đo lường mức độ trùng khớp giữa bounding box dự đoán và thực tế.  
  * **mAP (mean Average Precision)**: Đo lường độ chính xác trung bình trên các lớp và các ngưỡng IoU khác nhau.  
  * **Precision và Recall**: Đánh giá khả năng phát hiện đúng ổ gà và tỷ lệ phát hiện ổ gà thực tế.  
* **Quy trình tiền xử lý**:

  0. **Chuẩn hóa ảnh**: Resize ảnh về kích thước đồng nhất (ví dụ: 416x416 pixels) và chuẩn hóa giá trị pixel về phạm vi \[0, 1\].  
  1. **Tăng cường dữ liệu**: Áp dụng các kỹ thuật như xoay, thay đổi độ sáng, độ tương phản để tăng tính đa dạng của dữ liệu huấn luyện.  
  2. **Chuyển đổi nhãn**: Chuyển đổi nhãn từ định dạng ban đầu sang định dạng YOLOv8, bao gồm thông tin về lớp, tọa độ trung tâm, chiều rộng và chiều cao của bounding box.

---

**Thuật toán gộp cụm và giảm chiều dữ liệu?**

* **Thuật toán gộp cụm (Clustering)**: Có thể sử dụng **K-means** để phân nhóm các ảnh theo đặc trưng, giúp phân loại các loại ổ gà hoặc các mức độ hư hỏng khác nhau.  
* **Giảm chiều dữ liệu**: Áp dụng **PCA (Principal Component Analysis)** để giảm số chiều của dữ liệu đặc trưng, giúp tăng tốc độ huấn luyện và giảm overfitting.

---

**Link dataset**

* **Pothole Image Segmentation Dataset**: [https://www.kaggle.com/datasets/farzadnekouei/pothole-image-segmentation-dataset](https://www.kaggle.com/datasets/farzadnekouei/pothole-image-segmentation-dataset?utm_source=chatgpt.com)

Bộ dữ liệu này bao gồm 780 ảnh được chú thích theo định dạng YOLOv8, phù hợp cho bài toán nhận diện và phân đoạn ổ gà.

