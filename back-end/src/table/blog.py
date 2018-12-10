import sys
from datetime import datetime

from sqlalchemy import (Boolean, Column, DateTime, Float, ForeignKey, Integer,
                        String, Text)
from sqlalchemy.ext.declarative import declarative_base

from src.setting import ENGINE, Base


class User(Base):
    """
    User Model
    users table
    """
    __tablename__ = 'blog'
    id = Column('id', Integer, primary_key = True, nullable=False)
    title = Column('title', String(255), nullable=False)
    publish_user_id = Column('publish_user_id', Integer, ForeignKey('user.id'), nullable=False)
    description = Column('description', String(255))
    content = Column('content', Text, nullable=False)
    main_image = Column('avatar_url', String(255), nullable=False)
    is_public = Column('is_public', Boolean, default=True, nullable=False)
    created_at = Column('created_at', DateTime, default=datetime.now, nullable=False)
    updated_at = Column('updated_at', DateTime, default=datetime.now, nullable=False)

def main(args):
    """
    main funct
    """

    # create database
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main(sys.argv)
