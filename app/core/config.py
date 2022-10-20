import os
from dotenv import load_dotenv


class DBSettings:
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    def __init__(self, mode: str) -> None:
        load_dotenv()

        if mode == "local":

            self.POSTGRES_SERVER = os.getenv("LOCAL_DATABASE_URL")
            self.POSTGRES_USER = os.getenv("LOCAL_DB_USER")
            self.POSTGRES_PASSWORD = os.getenv("LOCAL_DB_PASSWORD")
            self.POSTGRES_DB = os.getenv("LOCAL_DB_NAME")

        elif mode == "prod":
            self.POSTGRES_SERVER = os.getenv("PROD_DATABASE_URL")
            self.POSTGRES_USER = os.getenv("PROD_DB_USER")
            self.POSTGRES_PASSWORD = os.getenv("PROD_DB_PASSWORD")
            self.POSTGRES_DB = os.getenv("PROD_DB_NAME")

        else:
            raise ValueError("mode should be local or prod")


db_settings = DBSettings(mode="local")
