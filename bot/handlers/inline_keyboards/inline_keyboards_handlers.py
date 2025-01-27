from aiogram import Router, types, F


def inline_handlers(router: Router):

    # Обработчик для инлайн-кнопки 1.1
    @router.callback_query(F.data == "inline_button_1_1")
    async def handle_inline_button_1_1(query: types.CallbackQuery):
        await query.message.edit_text("Вы нажали на инлайн-кнопку 1.1!")

    # Обработчик для инлайн-кнопки 1.2
    @router.callback_query(F.data == "inline_button_1_2")
    async def handle_inline_button_1_2(query: types.CallbackQuery):
        await query.message.edit_text("Вы нажали на инлайн-кнопку 1.2!")

    # Обработчик для инлайн-кнопки 2.1
    @router.callback_query(F.data == "inline_button_2_1")
    async def handle_inline_button_2_1(query: types.CallbackQuery):
        await query.message.edit_text("Вы нажали на инлайн-кнопку 2.1!")

    # Обработчик для инлайн-кнопки 2.2
    @router.callback_query(F.data == "inline_button_2_2")
    async def handle_inline_button_2_2(query: types.CallbackQuery):
        await query.message.edit_text("Вы нажали на инлайн-кнопку 2.2!")
