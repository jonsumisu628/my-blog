from sqlalchemy import Column
from sqlalchemy.dialects.mysql import INTEGER

class BaseModel():
    id = Column(INTEGER(11), primary_key=True)
    @classmethod
    def find_by_id(cls, id, session):
        obj = session.query(cls).filter(cls.id == id).one()
        return obj

    @classmethod
    def find_all(cls, session):
        obj = session.query(cls).all()
        return obj

    @classmethod
    def register(cls, session):
        session.add(cls)
        session.commit()
