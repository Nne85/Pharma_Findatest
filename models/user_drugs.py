#!/usr/bin/python
""" holds class UserDrug"""
from os import getenv 
from models.base_model import BaseModel, Base
import models
import sqlalchemy
from sqlalchemy import Column, String, DateTime, Text, MetaData, Table,\
    ForeignKey, Integer
from sqlalchemy.orm import relationship, backref
from sqlalchemy.types import Boolean


class UserDrug(BaseModel, Base):
    """Representation of UserDrug """
    if models.storage_t == ("db"):
        __tablename__ = 'user_drugs'
        user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
        drug_id = Column(Integer, ForeignKey('drugs.drug_id'), nullable=False)

    else:
        user_id = ""
        drug_id = ""

    def __init__(self, *args, **kwargs):
        """initializes UserDrug"""
        super().__init__(*args, **kwargs)
