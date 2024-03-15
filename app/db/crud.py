from db.models import Mytable
from db.engine import Session


def insert_message(message):
    try:
        with Session() as session:
            mytable_obj = Mytable(**message)
            session.add(mytable_obj)
            session.commit()
    except Exception as e:
        print(e)
