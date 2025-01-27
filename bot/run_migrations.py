import asyncio
from db.database import init_db

async def run_migrations():
    await init_db()

if __name__ == "__main__":
    asyncio.run(run_migrations())
