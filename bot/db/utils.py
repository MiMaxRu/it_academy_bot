
from cryptography.fernet import Fernet
from config import ENCRYPTION_KEY

# Загрузка ключа для шифрования
cipher = Fernet(ENCRYPTION_KEY.encode())

def encrypt(data: str) -> str:
    """Шифрование данных с помощью Fernet."""
    return cipher.encrypt(data.encode()).decode()

def decrypt(data: str) -> str:
    """Дешифрование данных с помощью Fernet."""
    return cipher.decrypt(data.encode()).decode()

