import pytest

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'bot')))

from db.database import init_db, engine, async_session
from db.models import Chat
from db.crud.chat_operations import add_chat, update_chat, delete_chat

@pytest.mark.asyncio
async def test_init_db():
    try:
        # Инициализация базы данных
        await init_db()
    except Exception as e:
        pytest.fail(f"Database initialization failed: {e}")
    finally:
        # Убедиться, что подключение к базе данных закрывается
        await engine.dispose()


@pytest.mark.asyncio
async def test_update_chat():
    async with async_session() as session:
        # Добавление новой записи для удаления
        new_chat = await add_chat(session, id_chat=123456, name="Test Chat", username="testuser", phone="1234567890", is_admin=True)

        # Обновление записи
        updated_chat = await update_chat(session, chat_id=new_chat.id, name="Updated Chat", phone="0987654321")
        
        # Проверка обновления записи
        assert updated_chat.id == new_chat.id
        assert updated_chat.decrypted_name == "Updated Chat"
        assert updated_chat.decrypted_phone == "0987654321"
        assert updated_chat.decrypted_username == "testuser"  # Поле не изменялось
        assert updated_chat.is_admin is True  # Поле не изменялось
        
        # Удаление записи
        deleted_chat = await delete_chat(session, chat_id=new_chat.id)
        
        # Проверка удаления записи
        assert deleted_chat.id == new_chat.id
        
        # Попытка получить удаленную запись
        chat = await session.get(Chat, new_chat.id)
        assert chat is None

