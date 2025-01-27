import asyncio
from ..database import async_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from ..models import Chat
from ..utils import encrypt


async def add_chat(
    session: AsyncSession,
    id_chat: int,
    name: str = None,
    username: str = None,
    phone: str = None,
    is_admin: bool = False,
    language: str = "ua",
):
    new_chat = Chat(
        id_chat=id_chat,
        name=encrypt(name) if name else None,  # Шифрование
        username=encrypt(username) if username else None,  # Шифрование
        phone=encrypt(phone) if phone else None,  # Шифрование
        is_admin=is_admin,
        language=language,
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
    language: str = None,
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
        if language is not None:
            chat.language = language 

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

async def get_chats(
    session: AsyncSession,
    id_chat: int = None,
    is_admin: bool = None,
    language: str = None
):
    """
    Получение данных из таблицы chats с возможностью фильтрации.

    :param session: Асинхронная сессия базы данных
    :param id_chat: ID чата для фильтрации (опционально)
    :param is_admin: Флаг администратора для фильтрации (опционально)
    :param language: Язык для фильтрации (опционально)
    :return: Список объектов Chat
    """
    query = select(Chat)

    # Добавляем фильтры, если они указаны
    if id_chat is not None:
        query = query.where(Chat.id_chat == id_chat)
    if is_admin is not None:
        query = query.where(Chat.is_admin == is_admin)
    if language is not None:
        query = query.where(Chat.language == language)

    result = await session.execute(query)
    return result.scalars().all()


async def get_admin_status(session: AsyncSession, id_chat: int):
    """
    Получение статуса администратора для указанного чата.
    :param session: Асинхронная сессия базы данных
    :param id_chat: ID чата для проверки
    :return: True, если пользователь является администратором, иначе False
    """
    chat = await session.get(Chat, id_chat)
    if chat:
        return chat.is_admin
    return False



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

        # Получение всех чатов
        all_chats = await get_chats(session)
        print("All chats:", all_chats)

        # Получение чатов с фильтрацией
        admin_chats = await get_chats(session, is_admin=True)
        print("Admin chats:", admin_chats)



if __name__ == "__main__":
    # Запуск примеров
    asyncio.run(main())
