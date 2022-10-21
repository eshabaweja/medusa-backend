from datetime import datetime
from email.policy import default
from sqlalchemy import Date, Integer, DateTime
from sqlalchemy import ForeignKey, Column, Index, text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ARRAY

from app.db.base_class import Base
from app.db.session import engine


class Cycles(Base):

    __tablename__ = "cycles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    start = Column(DateTime, default=datetime.utcnow)


Cycles.__table__.create(bind=engine, checkfirst=True)
