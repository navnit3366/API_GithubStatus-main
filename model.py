from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, String, BLOB

__DB_NAME = 'github_status.db'
engine = create_engine('sqlite:///' + __DB_NAME, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

defaut_value: str = 'default'

'''
class Status(Base):

    __tablename__ = 'status'
    id = Column(BLOB, primary_key=True)
    actor = Column(BLOB, default=defaut_value)
    org = Column(BLOB, default=defaut_value)
    created_at = Column(BLOB, default=defaut_value)
    payload = Column(BLOB, default=defaut_value)
    public = Column(BLOB, default=defaut_value)
    repo = Column(BLOB, default=defaut_value)
    type = Column(BLOB, default=defaut_value)
'''


class Status(Base):

    __tablename__ = 'status'
    id = Column(String, primary_key=True)
    actor = Column(String, default=defaut_value)
    org = Column(String, default=defaut_value)
    created_at = Column(String, default=defaut_value)
    payload = Column(String, default=defaut_value)
    public = Column(String, default=defaut_value)
    repo = Column(String, default=defaut_value)
    type = Column(String, default=defaut_value)


class Client(Base):
    __tablename__ = 'client'
    id = Column(String, primary_key=True)
    name = Column(String)
    mail = Column(String)


Base.metadata.create_all(engine)
