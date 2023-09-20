"""User Class Module"""

from os import getenv
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime, Integer,\
    MetaData, Table, ForeignKey
import hashlib
from sqlalchemy.orm import relationship, backref

storage_t = getenv("PHARMACY_Storage")


class User(BaseModel, Base):
    """Representation of User """
    __tablename__ = 'users'
    if models.storage_t == ("db"):
        name = Column(String(128), nullable=False)
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        searches = relationship("UserSearches", backref="user")
        favorites = relationship("UserFavorites", backref="user")
        search_results = Column(String(512), nullable=True)
        #__table_args__ = (Index('idx_users_user_id', 'user_id'),)

    else:
        name = None
        email = None
        password = None
        searches = ""
        favorites = ""
        search_results = ""

    def __init__(self, *args, **kwargs):
        """initializes User"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, key, value):
        """sets user pasword"""
        if key == "password":
            value = hashlib.md5(value.encode()).hexdigest()
        super().__setattr__(key, value)
