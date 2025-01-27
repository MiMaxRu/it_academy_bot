
from aiogram import Router, types, F
from keyboards.reply_client import create_main_client_menu
from keyboards.reply_admin import create_main_admin_menu
from handlers.reply_keyboards.reply_keyboards_handlers import reply_handlers
from handlers.inline_keyboards.inline_keyboards_handlers import inline_handlers

from db.database import async_session
from db.crud.chat_operations import add_chat, update_chat, get_chats, get_admin_status

import json
# Загрузка файла схемы
with open("/app/menu_scheme.json", "r", encoding="utf-8") as file:
    menu_scheme = json.load(file)


def register_commands(router: Router):
    # Обработчик для команды /start
    @router.message(F.text == "/start")
    async def start_command(message: types.Message):
        user = message.from_user
        
        language = user.language_code or "uk"  # Язык пользователя
        if language not in menu_scheme:
            language = "uk"
        welcome_message = menu_scheme[language]["welcome"]


        user = message.from_user
        id_chat = user.id
        name = user.first_name or None
        username = user.username or None
        # language = user.language_code or "uk"

        async with async_session() as session:
            # Проверяем, есть ли пользователь в БД
            existing_chats = await get_chats(session, id_chat=id_chat)
            existing_chat = existing_chats[0] if existing_chats else None

            if existing_chat:
                # Обновляем данные пользователя
                await update_chat(
                    session,
                    chat_id=existing_chat.id,
                    name=name,
                    username=username,
                    language=language
                )
            else:
                # Добавляем нового пользователя
                await add_chat(
                    session,
                    id_chat=id_chat,
                    name=name,
                    username=username,
                    is_admin=False,
                    language=language,
                )
                await message.answer("Вы успешно зарегистрированы в системе.")

            await message.answer(
                    await get_admin_status(session, id_chat)
                )

            if get_admin_status(session, id_chat) == True:
                await message.answer(
                    welcome_message,
                    reply_markup=create_main_admin_menu(language)
                )
            else:
                await message.answer(
                    welcome_message,
                    reply_markup=create_main_client_menu(language)
                )

    reply_handlers(router)
    inline_handlers(router)
