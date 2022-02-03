from sqlalchemy.orm import Session

from quotations import Models


# 增
def add_ChatRecord(db: Session, cr: Models.ChatRecord):
    if cr.name is None or cr.content is None:
        print('无name!')
        return cr
    db.add(cr)
    db.commit()
    db.refresh(cr)
    return cr
