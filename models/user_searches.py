#!/usr/bin/pthon3
""" UserSearches Module """

from os import getenv
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, DateTime, Text,\
    MetaData, Table
from sqlalchemy.orm import relationship, backref


class UserSearches(BaseModel, Base):
    """Representation of UserSearches """
    if models.storage_t == ("db"):
        __tablename__ = 'user_searches'
        search_id = Column(Integer, primary_key=True, autoincrement=True)
        user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
        drug_id = Column(Integer, ForeignKey('drugs.drug_id'), nullable=False)
        search_date = Column(DateTime, nullable=False)
        search_results = Column(String(512), nullable=True)
    else:
        search_id = ""
        user_id = ""
        drug_id = ""
        search_date = ""
        search_results = ""

    def __init__(self, *args, **kwargs):
        """initializes UserSearches"""
        super().__init__(*args, **kwargs)
