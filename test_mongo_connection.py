import asyncio
from config.database import ping_db

if __name__ == "__main__":
    asyncio.run(ping_db())
