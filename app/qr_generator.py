import qrcode
import os

def generate_qr(product_id):
    # The link that the QR will point to
    url = f"http://192.168.68.114:5000/verify/{product_id}"

    # Create the QR code
    qr = qrcode.make(url)

    # Save it into static/qrcodes/
    folder = "static/qrcodes"
    if not os.path.exists(folder):
        os.makedirs(folder)

    file_path = os.path.join(folder, f"{product_id}.png")
    qr.save(file_path)
    print(f"✅ QR code saved to {file_path}")
