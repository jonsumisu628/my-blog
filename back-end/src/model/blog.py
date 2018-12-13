from sqlalchemy import Column, DateTime, ForeignKey, text
from sqlalchemy.dialects.mysql import INTEGER, TEXT, TINYINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, validates

from src.model.session import ENGINE, Base, Session
from src.model.base import BaseModel


class Blog(Base, BaseModel):
    __tablename__ = 'blog'

    id = Column(INTEGER(11), primary_key=True)
    title = Column(VARCHAR(255), nullable=False)
    publish_user_id = Column(INTEGER(11), ForeignKey('users.id', ondelete='CASCADE', onupdate='CASCADE'),nullable=False, index=True)
    description = Column(VARCHAR(255))
    content = Column(TEXT, nullable=False)
    main_image = Column(VARCHAR(255))
    is_public = Column(TINYINT(4), nullable=False, server_default=text("'1'"))
    created_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))

    publish_user = relationship('User')

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
