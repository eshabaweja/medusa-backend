from typing import Generator


from app.db.session import SessionLocal

from dotenv import load_dotenv

load_dotenv()


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db

    except Exception as e:
        print(e)

    finally:
        db.close()
