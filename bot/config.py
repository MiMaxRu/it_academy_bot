import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://user:password@db:5432/database")
ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY")
SUPER_ADMIN_ID = os.getenv("SUPER_ADMIN_ID")