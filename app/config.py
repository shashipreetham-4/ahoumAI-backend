# app/config.py
import os
from dotenv import load_dotenv

print("📄 Looking for .env at:", os.path.abspath(".env"))

# Safe in both dev and prod — .env won't exist in production, and it won't overwrite prod values
load_dotenv()


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

    print("🔎 Raw env:", os.environ.get("DATABASE_URL"))
    print("🟢 Loaded DATABASE_URL:", SQLALCHEMY_DATABASE_URI)

    if not SQLALCHEMY_DATABASE_URI or not JWT_SECRET_KEY:
        raise ValueError(
            "Missing required environment variables. Check DATABASE_URL and JWT_SECRET_KEY."
        )
