docker-compose run --rm bot pytest
docker-compose up --build
docker exec -it project_bot-bot-1 /bin/bash

docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' project_bot-db-1

<!-- psql -h <IP-адрес> -p 5432 -U user -d bot_db -->
psql -h 172.22.0.2 -p 5432 -U user -d bot_db



python3 -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"




.
├── Dockerfile
├── README.md
├── bot
│   ├── __init__.py
│   ├── config.py
│   ├── db
│   │   ├── __init__.py
│   │   ├── database.py
│   │   ├── models.py
│   │   └── utils.py
│   ├── handlers
│   │   ├── __init__.py
│   │   └── start.py
│   └── main.py
├── docker-compose.yml
├── pyproject.toml
├── requirements.txt
└── tests
    ├── __init__.py
    ├── test_database.py
    └── test_handlers.py












Теперь нужно исправить обработчик /start для записи данных пользователя для телеграмма. Если пользователь уже есть, то добавлять не нужно, а если данные изменились, то нужно отредактировать: 

commands.py: from aiogram import Router, types, F
from keyboards.reply import main_menu
from keyboards.inline import inline_menu_1, inline_menu_2
from handlers.reply_keyboards.reply_keyboards_handlers import reply_handlers
from handlers.inline_keyboards.inline_keyboards_handlers import inline_handlers

from db.database import async_session
from db.models import Chat
from db.crud.chat_operations import add_chat, update_chat

def register_commands(router: Router):
    # Обработчик для команды /start
    @router.message(F.text == "/start")
    async def start_command(message: types.Message):
        user = message.from_user
        id_chat = user.id
        name = user.first_name or None
        username = user.username or None

        async with async_session() as session:
            # Проверяем, есть ли пользователь в БД
            existing_chat = await session.get(Chat, id_chat)
            if existing_chat:
                await message.answer(
                    "Вы зарегистрированы в системе."
                )
                return
            else:
                # Добавляем пользователя в базу данных
                await add_chat(
                    session,
                    id_chat=id_chat,
                    name=name,
                    username=username,
                    phone=None,
                    is_admin=False,
                )

                await message.answer(
                        "Вы успешно зарегистрированы в системе."
                    )

        await message.answer(
            "Привет! Это главное меню.",
            reply_markup=main_menu
        )

    reply_handlers(router)
    inline_handlers(router)            
    
Так выглядит файл chat_operations.py: import asyncio
from ..database import async_session
from sqlalchemy.ext.asyncio import AsyncSession


from ..models import Chat
from ..utils import encrypt


async def add_chat(
    session: AsyncSession,
    id_chat: int,
    name: str = None,
    username: str = None,
    phone: str = None,
    is_admin: bool = False,
):
    new_chat = Chat(
        id_chat=id_chat,
        name=encrypt(name) if name else None,  # Шифрование
        username=encrypt(username) if username else None,  # Шифрование
        phone=encrypt(phone) if phone else None,  # Шифрование
        is_admin=is_admin,
    )
    session.add(new_chat)
    await session.commit()
    await session.refresh(new_chat)
    return new_chat


async def update_chat(
    session: AsyncSession,
    chat_id: int,
    name: str = None,
    username: str = None,
    phone: str = None,
    is_admin: bool = None,
):
    try:
        chat = await session.get(Chat, chat_id)
        if not chat:
            return None

        if name is not None:
            chat.name = encrypt(name)  # Шифрование
        if username is not None:
            chat.username = encrypt(username)  # Шифрование
        if phone is not None:
            chat.phone = encrypt(phone)  # Шифрование
        if is_admin is not None:
            chat.is_admin = is_admin

        await session.commit()
        await session.refresh(chat)
        return chat
    except Exception as e:
        # Логирование ошибки или обработка
        print(f"Error updating chat: {e}")
        return None


async def delete_chat(session: AsyncSession, chat_id: int):
    chat = await session.get(Chat, chat_id)
    if not chat:
        return None

    await session.delete(chat)
    await session.commit()
    return chat


async def main():
    async with async_session() as session:
        # Добавление новой записи
        new_chat = await add_chat(session, id_chat=123456, name="Test Chat", username="testuser", phone="1234567890", is_admin=True)
        print(new_chat)

        # Изменение существующей записи
        updated_chat = await update_chat(session, chat_id=new_chat.id, name="Updated Chat")
        print(updated_chat)

        # Удаление записи
        deleted_chat = await delete_chat(session, chat_id=new_chat.id)
        print(deleted_chat)



if __name__ == "__main__":
    # Запуск примеров
    asyncio.run(main())

Представленные скрипты выше, были реализованы для старой версии схемы БД. Переделай для новой версии БД