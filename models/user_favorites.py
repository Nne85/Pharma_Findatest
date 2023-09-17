#!/usr/bin/python3
""" UserFavorites Class Module """

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, backref

storage_t = getenv("PHARMACY_Storage")


class UserFavorites(BaseModel, Base):
    """Representation of UserFavorites """
    __tablename__ = 'user_favorites'
    if models.storage_t == ("db"):
        favorite_id = Column(String(60), primary_key=True)
        user_id = Column(String(60), ForeignKey('users.user_id'), nullable=False)
        store_id = Column(String(60),  ForeignKey('pharmacy_stores.store_id'), nullable=False)
        created_at = Column(DateTime)
        favorite_reason = Column(String(256), nullable=True)
    else:
        favorite_id = None
        user_id = None
        store_id = None
        favorite_reason = ""

    def __init__(self, *args, **kwargs):
        """initializes UserFavorites"""
        super().__init__(*args, **kwargs)
