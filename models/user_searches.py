#!/usr/bin/pthon3
""" UserSearches Module """

from os import getenv
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, DateTime, Text,\
    MetaData, Table
from sqlalchemy.orm import relationship, backref

storage_t = getenv("PHARMACY_Storage")


class UserSearches(BaseModel, Base):
    """Representation of UserSearches """
    __tablename__ = 'user_searches'
    if models.storage_t == ("db"):
        search_id = Column(String(60), primary_key=True)
        user_id = Column(String(60), ForeignKey('users.user_id'), nullable=False)
        drug_id = Column(String(60), ForeignKey('drugs.drug_id'), nullable=False)
        search_date = Column(DateTime, nullable=False)
        search_results = Column(String(512), nullable=True)
    else:
        search_id = None
        user_id = None
        drug_id = None
        search_date = ""
        search_results = ""

    def __init__(self, *args, **kwargs):
        """initializes UserSearches"""
        super().__init__(*args, **kwargs)
