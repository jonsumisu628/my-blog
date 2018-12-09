import os

from dotenv import load_dotenv
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *

dotenv_path = join(os.path.dirname(__file__), '../.env')
load_dotenv(dotenv_path)

DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8' % (
    os.environ.get("MYSQL_USER"),
    os.environ.get("MYSQL_PASSWORD"),
    "my-blog-db",
    "my-blog",
)

ENGINE = create_engine(
    DATABASE,
    encoding = "utf-8",
    echo=True
)

session = scoped_session(
    sessionmaker(
        autocommit = False,
        autoflush = False,
        bind = ENGINE
    )
)

Base = declarative_base()
Base.query = session.query_property()
