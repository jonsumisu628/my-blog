import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

dotenv_path = "".join([os.path.dirname(__file__), '/../../.env'])
load_dotenv(dotenv_path)

DATABASE = 'mysql+pymysql://%s:%s@%s/%s?charset=utf8mb4' % (
    os.environ.get("MYSQL_USER"),
    os.environ.get("MYSQL_PASSWORD"),
    "db",
    "my-blog",
)

ENGINE = create_engine(
    DATABASE,
    encoding = "utf-8",
    echo=True,
    pool_size=20,
    max_overflow=0
)

Session = sessionmaker(
    autocommit = False,
    autoflush = False,
    expire_on_commit=False,
    bind = ENGINE
)


Base = declarative_base()
# Base.query = session.query_property()

def session(func):
    def wrapper(*args, **kwargs):
        session = Session()
        kwargs["session"] = session
        result = func(*args, **kwargs)
        session.close()
        return result
    return wrapper
