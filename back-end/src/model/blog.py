from sqlalchemy import Column, DateTime, ForeignKey, text
from sqlalchemy.dialects.mysql import INTEGER, TEXT, TINYINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, validates

from src.model.base import BaseModel
from src.model.session import ENGINE, Base, Session


class Blog(Base, BaseModel):
    __tablename__ = 'blog'

    id = Column(INTEGER(11), primary_key=True)
    title = Column(VARCHAR(255), nullable=False)
    publish_user_id = Column(INTEGER(11), ForeignKey(
        'users.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    description = Column(VARCHAR(255))
    content = Column(TEXT, nullable=False)
    main_image = Column(VARCHAR(255))
    is_public = Column(TINYINT(4), nullable=False, server_default=text("'1'"))
    created_at = Column(DateTime, nullable=False,
                        server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, nullable=False, server_default=text(
        "CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))

    publish_user = relationship('User')

    def __init__(
        self,
        *,
        id=None,
        title=None,
        publish_user_id=None,
        description=None,
        content=None,
        main_image=None,
        is_public=None,
        created_at=None,
        updated_at=None
    ):
        self.id = id
        self.title = title
        self.publish_user_id = publish_user_id
        self.description = description
        self.content = content
        self.main_image = main_image
        self.is_public = is_public
        self.created_at = created_at
        self.updated_at = updated_at

    @validates('title', 'description', 'content')
    def validate_blank_character(self, key, value):
        assert value != ''
        return value

    def to_dict(self):
        return ({
            'id': self.id,
            'title': self.title,
            'publish_user_id': self.publish_user_id,
            'description': self.description,
            'content': self.content,
            'main_image': self.main_image,
            'is_public': self.is_public,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        })


if __name__ == "__main__":
    Base.metadata.create_all(bind=ENGINE)
