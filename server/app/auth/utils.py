from ..model import *


def is_account_available(username, tag):
    username = username.lower()

    data = db.session.execute(db.select(Users).filter(Users.username == username, Users.tag == tag)).scalar()

    if data:
        return False

    return True
