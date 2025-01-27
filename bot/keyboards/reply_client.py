# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# # Главное меню
# main_menu = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="Кнопка 1"), KeyboardButton(text="Кнопка 2")],
#         [KeyboardButton(text="Помощь")]
#     ],
#     resize_keyboard=True
# )


import json
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Загрузка файла схемы
with open("menu_scheme.json", "r", encoding="utf-8") as file:
    menu_scheme = json.load(file)


# Функция для генерации меню на основе языка
def create_main_client_menu(language: str) -> ReplyKeyboardMarkup:
    
    buttons = menu_scheme[language]["main_menu"]["buttons_client"]
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=buttons["courses"]),
                KeyboardButton(text=buttons["intensives"]),
                KeyboardButton(text=buttons["free_lesson"]),
            ],
            [
                KeyboardButton(text=buttons["contact_manager"]),
                KeyboardButton(text=buttons["change_language"]),
                KeyboardButton(text=buttons["help"]),
             ],
        ],
        resize_keyboard=True,
    )


# Пример использования
# user_language = "ru"  # Определите язык пользователя динамически
# main_menu = create_main_menu(user_language)
