# Gunakan image Python yang ringan
FROM python:3.9-slim

# Set direktori kerja di dalam kontainer
WORKDIR /app

# Copy file requirements dan install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy seluruh kode aplikasi
COPY . .

# Ekspos port 80 (Sesuai dengan Security Group ALB-SG dan EC2-SG yang kita buat)
EXPOSE 80

# Jalankan aplikasi
CMD ["python", "app.py"]
