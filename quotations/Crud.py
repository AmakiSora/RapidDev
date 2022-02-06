from typing import List

from sqlalchemy import and_
from sqlalchemy.orm import Session

from Setting import SingleSession
from quotations import Models
from utils import ThreadUtil


# 增
def add_ChatRecord(db: Session, cr: Models.ChatRecord):
    if cr.name is None or cr.content is None:
        print('无name!')
        return cr
    db.add(cr)
    db.commit()
    return cr


# 批量增
def batch_add_ChatRecord(db: Session, crList: List[Models.ChatRecord]):
    crList = check_ChatRecord(crList)
    for cr in crList:
        db.add(cr)
    db.commit()
    return len(crList)


# 获取条数(name)
def get_ChatRecord_name_count(db: Session, name: str):
    return db.query(Models.ChatRecord).filter(Models.ChatRecord.name == name).count()


# 随机查询(name)
def get_ChatRecord_random(db: Session, name: str, NO: int):
    return db.query(Models.ChatRecord).filter(Models.ChatRecord.name == name).offset(NO).first()


# 模糊查询(name,content)
def fuzzy_search(name, content, db: Session):
    if name:
        return db.query(Models.ChatRecord).filter(
            and_(Models.ChatRecord.name == name, Models.ChatRecord.content.like(content))).all()
    else:
        return db.query(Models.ChatRecord).filter(Models.ChatRecord.content.like(content)).all()


# 校验
def check_ChatRecord(crList: List[Models.ChatRecord]):
    print('------------------------------校验中------------------------------')
    newList = []
    ThreadUtil.multithreading_list(crList, multithreadingProcessing, (newList,))
    return newList


# 校验查询(name,content)
def get_ChatRecord_check(db: Session, cr: Models.ChatRecord):
    return db.query(Models.ChatRecord).filter(
        and_(Models.ChatRecord.name == cr.name, Models.ChatRecord.content == cr.content)).first()


# 校验多线程处理
def multithreadingProcessing(cr, newList):
    if cr.name is None or \
            cr.name == '' or \
            cr.content is None or \
            cr.content == '' or \
            cr.content == '[图片]':
        print('无效记录!')
        return '无效记录', None
    # 用session工厂创建
    db = SingleSession()
    # 查询
    sss = get_ChatRecord_check(db, cr)
    # 关闭连接
    db.close()
    if sss is not None:
        print('已存在,name:' + sss.name + ' content:' + sss.content)
        return '已存在', None
    else:
        newList.append(cr)
        return '成功', None
