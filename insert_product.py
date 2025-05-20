from app.signer import sign_product
from app.db import get_connection

def insert_product(brand, serial, mfg_date):
    # 1. Combine product info into one string
    data = f"{brand}|{serial}|{mfg_date}"

    # 2. Sign the product data using SECP256k1
    private_key, public_key, signature = sign_product(data)

    # 3. Connect to MySQL and insert into the database
    conn = get_connection()
    cursor = conn.cursor()
    sql = """
        INSERT INTO products (brand, serial, mfg_date, signature, public_key)
        VALUES (%s, %s, %s, %s, %s)
    """
    values = (brand, serial, mfg_date, signature, public_key)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()

    print("✅ Product inserted and signed successfully.")

# Test it with sample data
if __name__ == "__main__":
    insert_product("Dior", "D123456", "2025-05-15")

