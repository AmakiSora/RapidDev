from datetime import datetime
from typing import Optional

from fastapi import APIRouter
from pydantic import BaseModel

"""
    语录
"""
app_quotation = APIRouter()


# 获取一条语录
@app_quotation.get('/{name}')
def get_quotation(name):
    return name


# 语录类
class Quotation(BaseModel):
    id: str
    name: str
    time: Optional[datetime] = None
    content: str
