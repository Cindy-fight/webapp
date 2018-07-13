# !/usr/bin/env python
# ! -*- coding:UTF-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

class Config():
    Base = declarative_base()
    engine = create_engine('mysql+mysqlconnector://root:Wtt2018@localhost:3306/webapp')
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
