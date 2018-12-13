
from sqlalchemy import Column, DateTime, ForeignKey, text
from sqlalchemy.dialects.mysql import INTEGER, TEXT, TINYINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from src.model.session import ENGINE, Base, session
from src.model.base import BaseModel

Base = declarative_base()
metadata = Base.metadata

class User(BaseModel):

    __tablename__ = 'users'

    id = Column(INTEGER(11), primary_key=True)
    password = Column(VARCHAR(255), nullable=False)
    salt = Column(VARCHAR(255), nullable=False)
    name = Column(VARCHAR(45), nullable=False)
    display_name = Column(VARCHAR(45), nullable=False)
    avatar_url = Column(VARCHAR(255))
    created_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))

if __name__ == "__main__":
    Base.metadata.create_all(bind=ENGINE)
    User.find_by_id
