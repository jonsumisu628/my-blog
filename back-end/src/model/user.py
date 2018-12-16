from sqlalchemy import Column, DateTime, ForeignKey, text
from sqlalchemy.dialects.mysql import INTEGER, TEXT, TINYINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, validates

from src.model.base import BaseModel
from src.model.blog import Blog
from src.model.session import ENGINE, Base, Session


class User(Base, BaseModel):

    __tablename__ = 'users'

    id = Column(INTEGER(11), primary_key=True)
    password = Column(VARCHAR(255), nullable=False)
    salt = Column(VARCHAR(255), nullable=False)
    name = Column(VARCHAR(45), nullable=False)
    display_name = Column(VARCHAR(45), nullable=False)
    avatar_url = Column(VARCHAR(255))
    created_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))

    blog = None

    @validates('name', 'display_name')
    def validate_blank_character(self, key, value):
        assert value != ''
        return value

    def to_dict(self):
        return ({
            'id': self.id,
            'name': self.name,
            'display_name': self.display_name,
            'avatar_url': self.avatar_url,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            "blog": None if self.blog == None else list(map(lambda x: x.to_dict(), self.blog))
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

if __name__ == "__main__":
    Base.metadata.create_all(bind=ENGINE)
