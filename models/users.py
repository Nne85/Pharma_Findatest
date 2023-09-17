"""User Class Module"""

from os import getenv
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime, Integer,\
    MetaData, Table, ForeignKey, Index
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship, backref

storage_t = getenv("PHARMACY_Storage")


class User(BaseModel, Base):
    """Representation of User """
    __tablename__ = 'users'
    if models.storage_t == ("db"):
        user_id = Column(String(60), primary_key=True)
        username = Column(String(128), nullable=False)
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        created_at = Column(DateTime)
        searches = relationship("UserSearches", backref="user")
        favorites = relationship("UserFavorites", backref="user")
        search_results = Column(String(512), nullable=True)
        __table_args__ = (Index('idx_users_user_id', 'user_id'),)

    else:
        user_id = None
        username = None
        email = None
        password = None
        searches = ""
        favorites = ""
        search_results = ""

    def __init__(self, *args, **kwargs):
        """initializes User"""
        super().__init__(*args, **kwargs)
        if 'password' in kwargs:
            self.set_password(kwargs['password'])

    def set_password(self, password):
        """Set user's password hash"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check if provided password matches user's password"""
        return check_password_hash(self.password_hash, password)
