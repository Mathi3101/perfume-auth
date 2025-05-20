from flask import Flask
from flask import Flask, render_template
from app.db import get_connection


app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Flask is working! Your perfume authentication system is running."

# 🔽 PASTE THIS BELOW 👇
@app.route("/verify/<int:product_id>")
def verify(product_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT brand, serial, mfg_date, signature, public_key FROM products WHERE id = %s", (product_id,))
    result = cursor.fetchone()
    conn.close()

    if result:
        brand, serial, mfg_date, signature, public_key = result
        data = f"{brand}|{serial}|{mfg_date}"

        is_valid = verify_signature(data, public_key, signature)

        if is_valid:
            return render_template("verify.html", brand=brand, serial=serial, mfg_date=mfg_date)
        else:
            return "❌ Invalid digital signature. This product may be fake."
    else:
        return "❌ Product not found or invalid QR code."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)