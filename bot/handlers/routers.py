from aiogram import Router
from handlers.commands import register_commands

router = Router()

# Регистрация всех обработчиков
register_commands(router)
