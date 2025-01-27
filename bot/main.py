import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers.routers import router as start_router

from db.database import init_db

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start_router)

    await init_db()

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
