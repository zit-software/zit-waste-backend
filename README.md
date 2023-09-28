# ZIT WASTE API

## Hướng dẫn cài đặt

### Sử dụng Docker

- Cài đặt Docker (https://docs.docker.com/get-docker/)
- Cài đặt Docker Compose (https://docs.docker.com/compose/install/)
- Chạy lệnh `docker-compose up -d` để khởi động các container

Server của bạn sẽ chạy ở địa chỉ `http://localhost:8080`

### Thủ công

#### Môi trường

- Python3 (https://www.python.org/downloads/)
- Pip3

#### Cài đặt

- Tạo môi trường ảo (https://docs.python.org/3/tutorial/venv.html)

  ```sh
  python3 -m venv venv
  ```

- Kích hoạt môi trường ảo

  ```sh
    source venv/bin/activate
  ```

- Cài đặt các thư viện cần thiết

  ```sh
    pip3 install -r requirements.txt
  ```

- Tải file model.keras vào thư mục gốc của dự án
  ```sh
  wget https://huggingface.co/thangved/zitwaste/resolve/main/model.keras -O model.keras
  ```
- Chạy server
  ```sh
    uvicorn main:app --host 127.0.0.1 --port 8080
  ```

Server của bạn sẽ chạy ở địa chỉ `http://localhost:8080`

## API Docs

Xem API Docs tại địa chỉ `http://localhost:8080/docs` hoặc `http://localhost:8080/redoc`
