from sqlalchemy import Column, Integer, String, DateTime, func

from Setting import Base


class ChatRecord(Base):
    # 数据库表名
    __tablename__ = "chat_record"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), index=True, comment='名字')
    content = Column(String(2048), comment='内容')
    time = Column(DateTime, default=None, comment='时间')
    created_time = Column(DateTime, server_default=func.now(), comment='入库时间')
