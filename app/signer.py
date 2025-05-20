from ecdsa import SigningKey, SECP256k1
import hashlib

def sign_product(data: str):
    sk = SigningKey.generate(curve=SECP256k1)
    vk = sk.get_verifying_key()
    digest = hashlib.sha256(data.encode()).digest()
    signature = sk.sign(digest)
    return (
        sk.to_string().hex(),
        vk.to_string().hex(),
        signature.hex()
    )

