from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from markdownify import markdownify

def decrypt(hex_text: str, key: str) -> str:
    """AES-256-CBC : clé = les 32 caractères de keyN, IV = ses 16 premiers."""
    k = key.encode()
    decryptor = Cipher(algorithms.AES(k), modes.CBC(k[:16])).decryptor()
    raw = decryptor.update(bytes.fromhex(hex_text)) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    return (unpadder.update(raw) + unpadder.finalize()).decode()

def html_to_markdown(html: str) -> str:
    return markdownify(html, heading_style="ATX", code_language="text").strip()
