# import pytest
# from unittest.mock import AsyncMock
# from aiogram import types 
# from unittest.mock import patch

# @pytest.mark.asyncio
# async def test_start_handler():
#     # Создаем фейковое сообщение от пользователя
#     message = types.Message(
#         message_id=1,
#         date="2024-01-01",
#         chat=types.Chat(id=1, type="private"),
#         text="/start",
#     )

#     # Мокаем метод reply с использованием patch
#     with patch.object(message, 'reply', new_callable=AsyncMock, return_value="Test reply"):
#         # Проверяем, что метод reply возвращает ожидаемое значение
#         result = await message.reply("Test reply")
        
#         # Проверка правильности результата
#         assert result == "Test reply"
#         # Убедитесь, что reply был вызван с правильным аргументом
#         message.reply.assert_called_with("Test reply")




# import pytest
# from aiogram import Bot, Dispatcher, types
# from aiogram.types import Message
# from aiogram.contrib.middlewares.logging import LoggingMiddleware
# from unittest.mock import AsyncMock, patch

# from config import BOT_TOKEN

# # Импорт вашего обработчика (предположим, он находится в файле handlers/start.py)
# from bot.handlers.start import start_handler

# @pytest.fixture
# def bot():
#     # Создаем объект бота
#     return Bot(token=BOT_TOKEN)

# @pytest.fixture
# def dp(bot):
#     # Создаем диспетчер
#     dp = Dispatcher(bot)
#     dp.middleware.setup(LoggingMiddleware())
#     return dp

# @pytest.mark.asyncio
# async def test_start_handler(bot, dp):
#     # Создаем фейковое сообщение от пользователя
#     message = types.Message(
#         message_id=1,
#         date="2024-01-01",
#         chat=types.Chat(id=1, type="private"),
#         from_user=types.User(id=1, is_bot=False, first_name="Test", last_name="User", username="testuser"),
#         text="/start"
#     )

#     # Мокаем метод reply с использованием patch
#     with patch.object(message, 'reply', new_callable=AsyncMock, return_value="Test reply"):
#         # Вызываем обработчик
#         await start_handler(message)

#         # Проверяем, что метод reply возвращает ожидаемое значение
#         message.reply.assert_called_with("Test reply")
