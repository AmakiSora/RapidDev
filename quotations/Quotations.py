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
async def upload_quotation(file: UploadFile = File(...)):
    content = await file.read()
    two = re.finditer(r"[^\n]*", content.decode('utf-8'))
    c = ''
    for i in two:
        strr = i.group()
        header = re.match(r"(?P<time>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (?P<name>[^\n]*)", strr)
        print('for里的' + c)
        if header is not None:
            print('if里的' + c)
            c = ''
            print(datetime.strptime(header.group('time'), '%Y-%m-%d %H:%M:%S'))
            print(header.group('name'))
        else:
            c += strr
    return ''


# 语录类
class Quotation(BaseModel):
    id: str
    name: str
    time: Optional[datetime] = None
    content: str
