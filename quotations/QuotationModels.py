from sqlalchemy import Column, Integer, String, DateTime

from mysql.Database import Base


class User(Base):
    __tablename__ = "quotations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    content = Column(String(2048))
    time = Column(DateTime, default=None)
