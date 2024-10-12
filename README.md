# Kafka Consumer and Producer 

## Mô tả

Dự án này là một ứng dụng Python sử dụng `confluent_kafka` để produce và consume dữ liệu từ và vào Kafka. Ứng dụng này đọc dữ liệu từ topic Kafka `product_view` và produce dữ liệu vào một topic mới có tên `new_product_view`. Sau đó dùng python để đọc dữ liệu từ `new_product_view` và lưu trữ vào cơ sở dữ liệu MongoDB.


## Yêu cầu

- Python 3.x
- Kafka
- MongoDB

## Cài đặt

1. **Clone dự án về máy của bạn**:
   ```bash
   git clone https://github.com/Khatran05082003/kafka_project.git
2. **Cài đặt các gói cần thiết**:
   ```bash
   pip install -r requirements.txt

3. **Chạy ứng dụng**:

   Đầu tiên, mở một terminal và chạy produce.py đọc dữ liệu từ nguồn Kafka được cung cấp trước và produce vào 1 topic trong Kafka bạn đã dựng :
   ```bash
   python produce.py
   ```
   Sau đó, mở một terminal khác và chạy producer để thực hiện việc đọc dữ liệu từ topic mà bạn tạo ở bước trên và lưu trữ dữ liệu xuống MongoDB:
   ```bash  
   python consumer_and_load_to_mongo.py
   ```
## Ghi chú
- Đảm bảo rằng bạn đã cấu hình đúng các thông số kết nối đến Kafka và MongoDB.
- Nếu gặp bất kỳ vấn đề nào trong quá trình sử dụng, hãy kiểm tra log để biết thêm thông tin.

## Demo
![mongo](https://github.com/user-attachments/assets/a3ac229e-eabe-460c-a4cf-78f11597515b)



