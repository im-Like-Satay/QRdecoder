import cv2
import numpy as np

from lib.ai import aiParser


def decode_qr(nama_gambar):
    file_bytes = np.asarray(bytearray(nama_gambar.read()), dtype=np.uint8)

    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    if img is not None:
        detektor = cv2.QRCodeDetector()
        data, _, _ = detektor.detectAndDecode(img)

        if data:
            return {
                "status": "Decode Success!",
                "data": data,
                "response": aiParser(data)["response"],
            }
        else:
            return {
                "status": "Warning",
                "message": "Gambar ditemukan, tapi tidak ada QR Code terbaca.",
            }

    else:
        return {
            "status": "Error",
            "message": f"File gambarbernama '{nama_gambar}' tidak ditemukan. /n Pastikan file ada di folder yang sama dengan script ini.",
        }
