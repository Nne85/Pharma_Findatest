#!/usr/bin/python3
""" UserFavorites Class Module """

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, backref


class UserFavorites(BaseModel, Base):
    """Representation of UserFavorites """
    if models.storage_t == ("db"):
        __tablename__ = 'user_favorites'
        favorite_id = Column(Integer, primary_key=True, autoincrement=True)
        user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
        store_id = Column(Integer,  ForeignKey('pharmacy_stores.store_id'), nullable=False)
        created_at = Column(DateTime)
        favorite_reason = Column(String(256), nullable=True)
    else:
        favorite_id = ""
        user_id = ""
        store_id = ""
        favorite_reason = ""

    def __init__(self, *args, **kwargs):
        """initializes UserFavorites"""
        super().__init__(*args, **kwargs)
