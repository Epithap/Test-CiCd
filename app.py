# pyrefly: ignore [missing-import]
from flask import Flask, jsonify
import pymysql
import os
import boto3

app = Flask(__name__)

# Konfigurasi Database RDS dari Environment Variable
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_USER = os.environ.get("DB_USER", "admin")
DB_PASS = os.environ.get("DB_PASS", "LksPassword123!")
DB_NAME = os.environ.get("DB_NAME", "lksapp")

@app.route('/')
def home():
    try:
        conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME)
        conn.close()
        return jsonify({"status": "sukses", "pesan": "Berhasil terkoneksi ke Database RDS AWS!"}), 200
    except Exception as e:
        return jsonify({"status": "gagal", "pesan": str(e)}), 500

@app.route('/s3-data')
def get_s3_data():
    try:
        s3 = boto3.client('s3', region_name='us-east-1')
        bucket_name = 'ks-storage-app-epithap'
        file_key = 'pesan.txt.txt'
        
        response = s3.get_object(Bucket=bucket_name, Key=file_key)
        content = response['Body'].read().decode('utf-8')
        
        return jsonify({"status": "sukses", "pesan_dari_s3": content}), 200
    except Exception as e:
        return jsonify({"status": "gagal", "pesan": str(e)}), 500
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)