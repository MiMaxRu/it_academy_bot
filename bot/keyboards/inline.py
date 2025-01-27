from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Инлайн-кнопки для "Кнопка 1"
inline_menu_1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Инлайн 1.1", callback_data="inline_button_1_1")],
        [InlineKeyboardButton(text="Инлайн 1.2", callback_data="inline_button_1_2")]
    ]
)

# Инлайн-кнопки для "Кнопка 2"
inline_menu_2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Инлайн 2.1", callback_data="inline_button_2_1")],
        [InlineKeyboardButton(text="Инлайн 2.2", callback_data="inline_button_2_2")]
    ]
)
