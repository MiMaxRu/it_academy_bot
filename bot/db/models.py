from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.dialects.postgresql import BIGINT
from sqlalchemy.ext.declarative import declarative_base

import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "bot"))
)

from .utils import encrypt, decrypt

Base = declarative_base()


class Chat(Base):
    __tablename__ = "chats"

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    id_chat = Column(BIGINT, nullable=False, unique=True)
    name = Column(String, nullable=True)
    username = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    is_admin = Column(Boolean, default=False)  # По умолчанию клиент
    language = Column(String, default="ua")

    @property
    def encrypted_id_chat(self):
        """Возвращает зашифрованный id чата."""
        return encrypt(str(self.id_chat))

    @encrypted_id_chat.setter
    def encrypted_id_chat(self, value: str):
        """Дешифрует и сохраняет id чата."""
        self.id_chat = decrypt(value)

    @property
    def decrypted_name(self):
        """Дешифрует имя."""
        return decrypt(self.name) if self.name else None

    @decrypted_name.setter
    def decrypted_name(self, value: str):
        """Шифрует имя перед сохранением в БД."""
        self.name = encrypt(value) if value else None

    @property
    def decrypted_username(self):
        """Дешифрует имя пользователя."""
        return decrypt(self.username) if self.username else None

    @decrypted_username.setter
    def decrypted_username(self, value: str):
        """Шифрует имя пользователя перед сохранением в БД."""
        self.username = encrypt(value) if value else None

    @property
    def decrypted_phone(self):
        """Дешифрует номер телефона."""
        return decrypt(self.phone) if self.phone else None

    @decrypted_phone.setter
    def decrypted_phone(self, value: str):
        """Шифрует номер телефона перед сохранением в БД."""
        self.phone = encrypt(value) if value else None

    def __repr__(self):
        return f"Chat(id={self.id}, id_chat={self.id_chat}, name={self.name}, username={self.username}, phone={self.phone}, is_admin={self.is_admin}), language={self.language})"


# class Courses(Base):
#     __tablename__ = 'courses'

#     id = Column(BIGINT, primary_key=True, autoincrement=True)
#     name = Column(String, nullable=True)
#     description = Column(String, nullable=True)
#     phone = Column(String, nullable=True)
#     is_admin = Column(Boolean, default=False)  # По умолчанию клиент
