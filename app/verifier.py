from ecdsa import VerifyingKey, SECP256k1
import hashlib

def verify_signature(data, public_key_hex, signature_hex):
    try:
        # Convert hex to bytes
        public_key_bytes = bytes.fromhex(public_key_hex)
        signature_bytes = bytes.fromhex(signature_hex)

        # Hash the original data
        digest = hashlib.sha256(data.encode()).digest()

        # Load the verifying key
        vk = VerifyingKey.from_string(public_key_bytes, curve=SECP256k1)

        # Verify the signature
        return vk.verify(signature_bytes, digest)

    except Exception as e:
        print("❌ Verification failed:", e)
        return False
