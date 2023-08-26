import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class UserFavorites(BaseModel, Base):
    """Representation of UserFavorites """
    __tablename__ = 'user_favorites'
    favorite_id = Column(String(60), primary_key=True)
    user_id = Column(String(60), ForeignKey('users.user_id'), nullable=False)
    store_id = Column(String(60), ForeignKey('pharmacy_stores.store_id'), nullable=False)
    created_at = Column(DateTime)

    favorite_reason = Column(String(256), nullable=True)

    def __init__(self, *args, **kwargs):
        """initializes UserFavorites"""
        super().__init__(*args, **kwargs)