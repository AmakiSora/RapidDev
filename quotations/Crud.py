from typing import List

from sqlalchemy import and_
from sqlalchemy.orm import Session

from quotations import Models


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
    crList = check_ChatRecord(db, crList)
    for cr in crList:
        if cr.name is None or cr.content is None:
            continue
        db.add(cr)
    db.commit()
    return 'ok'


# 查
def get_ChatRecord(db: Session, cr: Models.ChatRecord):
    return db.query(Models.ChatRecord).filter(
        and_(Models.ChatRecord.name == cr.name, Models.ChatRecord.content == cr.content)).first()


# 校验
def check_ChatRecord(db: Session, crList: List[Models.ChatRecord]):
    print('------------------------------校验中------------------------------')
    newList = []
    for cr in crList:
        sss = get_ChatRecord(db, cr)
        if cr.name is None or\
                cr.name == '' or\
                cr.content is None or\
                cr.content == '':
            print('name或者content为空!')
        elif sss is not None:
            print('已存在:' + sss.name + sss.content)
        else:
            newList.append(cr)
    return newList
