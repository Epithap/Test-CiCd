# pyrefly: ignore [missing-import]
from flask import Flask, jsonify
import pymysql
import os

app = Flask(__name__)

# Mengambil konfigurasi DB dari Environment Variable OS
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_USER = os.environ.get("DB_USER", "admin")
DB_PASS = os.environ.get("DB_PASS", "LksPassword123!")
DB_NAME = os.environ.get("DB_NAME", "lksapp")

@app.route('/')
def home():
    try:
        # Test koneksi ke RDS
        conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME)
        conn.close()
        return jsonify({"status": "sukses", "pesan": "Berhasil terkoneksi ke Database RDS AWS!"}), 200
    except Exception as e:
        return jsonify({"status": "gagal", "pesan": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
