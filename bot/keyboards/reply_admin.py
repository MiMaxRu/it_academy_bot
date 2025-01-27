
import json
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Загрузка файла схемы
with open("menu_scheme.json", "r", encoding="utf-8") as file:
    menu_scheme = json.load(file)


# Функция для генерации меню на основе языка
def create_main_admin_menu(language: str) -> ReplyKeyboardMarkup:
    
    buttons = menu_scheme[language]["main_menu"]["buttons_admin"]
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=buttons["courses"]),
                KeyboardButton(text=buttons["intensives"]),
                KeyboardButton(text=buttons["free_lesson"]),
            ],
            [
                KeyboardButton(text=buttons["directions_editor"]),
                KeyboardButton(text=buttons["mailing_list"]),
                KeyboardButton(text=buttons["change_language"]),
             ],
                         [
                KeyboardButton(text=buttons["admins"]),
                KeyboardButton(text=buttons["bd"]),
                KeyboardButton(text=buttons["help"]),
             ],
        ],
        resize_keyboard=True,
    )
