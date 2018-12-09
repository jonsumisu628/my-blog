import sys
from datetime import datetime

from sqlalchemy import Column, DateTime, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from setting import ENGINE, Base


class User(Base):
    """
    User Model
    users table
    """
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key = True, nullable=False)
    password = Column('password', String(255), nullable=False)
    solt = Column('solt', String(255), nullable=False)
    name = Column('name', String(45), nullable=False)
    displayName = Column('display_name', String(45), nullable=False)
    avatar_url = Column('avatar_url', String(255), default=None)
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
