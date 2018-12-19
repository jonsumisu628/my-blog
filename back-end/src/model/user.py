import logging
from logging import getLogger

import bcrypt
from sqlalchemy import Column, DateTime, ForeignKey, text
from sqlalchemy.dialects.mysql import (INTEGER, TEXT, TINYINT, VARBINARY,
                                       VARCHAR)
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, validates

from src.model.base import BaseModel
from src.model.blog import Blog
from src.model.session import ENGINE, Base, Session

logger = getLogger("my-blog").getChild("sub")

class User(Base, BaseModel):

    __tablename__ = 'users'

    id           = Column(INTEGER(11), primary_key=True)
    email        = Column(VARCHAR(255), nullable=False)
    password     = Column(VARBINARY(255), nullable=False)
    name         = Column(VARCHAR(45), nullable=False)
    display_name = Column(VARCHAR(45), nullable=False)
    avatar_url   = Column(VARCHAR(255))
    created_at   = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at   = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))

    blog = None

    def __init__(
        self,
        *,
        id=None,
        email=None,
        password=None,
        name=None,
        display_name=None,
        avatar_url=None,
        created_at=None,
        updated_at=None
    ):
        self.id           = id
        self.email        = email
        self.password     = password
        self.name         = name
        self.display_name = display_name
        self.avatar_url   = avatar_url
        self.created_at   = created_at
        self.updated_at   = updated_at

    @validates('email', 'password', 'name', 'display_name')
    def validate_blank_character(self, key, value):
        assert value != ''
        return value

    def to_dict(self):
        return ({
            'id'          : self.id,
            'email'       : self.email,
            'name'        : self.name,
            'display_name': self.display_name,
            'avatar_url'  : self.avatar_url,
            'created_at'  : self.created_at.isoformat(),
            'updated_at'  : self.updated_at.isoformat(),
            "blog"        : None if self.blog == None else list(map(lambda x: x.to_dict(), self.blog))
        })

    @classmethod
    def find_by_id(cls, id, session, included_blog=True):
        result = None
        if included_blog == True:
            data = session.query(cls, Blog).filter(cls.id == id).join(Blog, User.id == Blog.publish_user_id).all()
            result = User.to_nested_obj(data, ['blog'])
        else:
            result = session.query(cls).filter(cls.id == id).all()

        return result

    @classmethod
    def find_all(cls, session, included_blog=True):
        result = None
        if included_blog == True:
            data = session.query(cls, Blog).join(Blog, User.id == Blog.publish_user_id).all()
            result = User.to_nested_obj(data, ['blog'])
        else:
            result = session.query(cls).all()

        return result

    @staticmethod
    def register(model, new_password, session):
        if (new_password):
            model.password = bcrypt.hashpw(
                new_password.encode(encoding='utf-8'),
                bcrypt.gensalt(rounds=12, prefix=b'2a')
            )

        session.add(model)
        session.commit()

        return model

if __name__ == "__main__":
    Base.metadata.create_all(bind=ENGINE)
