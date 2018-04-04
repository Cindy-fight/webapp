# !/usr/bin/env python
# ! -*- coding:UTF-8 -*-
from sqlalchemy import Integer, String, Column
from config import Config

class Users(Config.Base):
    __tablename__ = 'users'
    id      = Column(Integer, primary_key=True)
    email   = Column(String(45))
    passwd  = Column(String(45))
    admin   = Column(Integer)
    name    = Column(String(45))
    image   = Column(String(500))
    created_at = Column(String(45))