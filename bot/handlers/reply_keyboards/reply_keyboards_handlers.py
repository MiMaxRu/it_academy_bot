from aiogram import Router, types, F
from keyboards.inline import inline_menu_1, inline_menu_2


def reply_handlers(router: Router):
    # Обработчик для кнопки "Кнопка 1"
    @router.message(F.text == "Кнопка 1")
    async def handle_button_1(message: types.Message):
        await message.answer(
            "Вы выбрали 'Кнопка 1'. Вот инлайн-кнопки:",
            reply_markup=inline_menu_1,
        )

    # Обработчик для кнопки "Кнопка 2"
    @router.message(F.text == "Кнопка 2")
    async def handle_button_2(message: types.Message):
        await message.answer(
            "Вы выбрали 'Кнопка 2'. Вот инлайн-кнопки:",
            reply_markup=inline_menu_2,
        )
