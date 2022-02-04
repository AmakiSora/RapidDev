import random
import re
from datetime import datetime

from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session

from Setting import SessionLocal
from quotations import Models, Crud
from quotations.Models import RandomOutChatRecord

"""
    语录
"""
app_quotation = APIRouter()


# 获取数据库连接(单例)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 随机获取一条语录
@app_quotation.get('/getOne/{name}')
def get_quotation_random(name, db: Session = Depends(get_db)):
    count = Crud.get_ChatRecord_name_count(db, name)
    NO = random.randint(1, count)
    cr = Crud.get_ChatRecord_random(db, name, NO)
    out = RandomOutChatRecord()
    out.name = cr.name
    out.time = cr.time
    out.content = cr.content
    print(out.__dict__)
    return out


# 上传qq聊天记录(txt)
@app_quotation.post('/upload')
async def upload_quotation(file: UploadFile = File(...), db: Session = Depends(get_db)):
    content = await file.read()
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
    result = Crud.batch_add_ChatRecord(db, crList)
    print('成功添加 ' + str(result) + ' 条聊天记录!')
    return '成功添加 ' + str(result) + ' 条聊天记录!'
