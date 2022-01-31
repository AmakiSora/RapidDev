import re
from datetime import datetime
from typing import Optional

from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel

"""
    语录
"""
app_quotation = APIRouter()


# 获取一条语录
@app_quotation.get('/{name}')
def get_quotation(name):
    return name


# 上传语录
@app_quotation.post('/upload')
async def upload_quotation(file:UploadFile = File(...)):
    content = await file.read()
    one = re.finditer(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} [^\n]*", content.decode('utf-8'))
    for i in one:
        print(i.group())
    return ''


# 语录类
class Quotation(BaseModel):
    id: str
    name: str
    time: Optional[datetime] = None
    content: str
