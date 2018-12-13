from sqlalchemy import Column, DateTime, ForeignKey, text
from sqlalchemy.dialects.mysql import INTEGER, TEXT, TINYINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from src.model.session import Base


class BaseModel(Base):
    @classmethod
    def find_by_id(cls, id, session):
        obj = session.query(cls).filter(cls.id == id).one()
        return obj

    @classmethod
    def find_all(cls, session):
        obj = session.query(cls).all()
        return obj

    def register(self, session):
        session.add(self)
        session.commit()
