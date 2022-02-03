import re
from datetime import datetime

from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session

from Setting import SessionLocal
from quotations import Models, Crud

"""
    语录
"""
app_quotation = APIRouter()


# 获取数据库连接
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 获取一条语录
@app_quotation.get('/{name}')
def get_quotation(name):
    return name


# 上传qq聊天记录(txt)
@app_quotation.post('/upload')
async def upload_quotation(file: UploadFile = File(...), db: Session = Depends(get_db)):
    content = await file.read()
    print(content)
    line = re.finditer(r"[^\n]*", content.decode('utf-8'))
    text = ''
    cr = Models.ChatRecord()
    crList = []
    # 以换行符为间隔进行数据处理
    for i in line:
        data = i.group()
        header = re.match(r"(?P<time>\d{4}-\d{2}-\d{2} \d*:\d{2}:\d{2}) (?P<name>[^\n]*)", data)
        if header is not None:
            text = re.sub(r'[\r]', '', text)
            print(text)
            cr.content = text
            crList.append(cr)
            print()
            # 重置
            cr = Models.ChatRecord()
            text = ''
            time = datetime.strptime(header.group('time'), '%Y-%m-%d %H:%M:%S')
            print(time)
            cr.time = time
            name = header.group('name')
            name = re.sub(r'[\r]', '', name)
            print(name)
            cr.name = name
        else:
            text += data
    # 保存
    Crud.batch_add_ChatRecord(db, crList)
    return '完成!'

