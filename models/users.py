import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Representation of User """
    __tablename__ = 'users'
    user_id = Column(String(60), primary_key=True)
    username = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    password_hash = Column(String(128), nullable=False)
    created_at = Column(DateTime)

    searches = relationship("UserSearches", backref="user")
    favorites = relationship("UserFavorites", backref="user")
    search_results = Column(String(512), nullable=True)

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