import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer, DateTime, Text
from sqlalchemy.orm import relationship


class UserSearches(BaseModel, Base):
    """Representation of UserSearches """
    __tablename__ = 'user_searches'
    search_id = Column(String(60), primary_key=True)
    user_id = Column(String(60), ForeignKey('users.user_id'), nullable=False)
    drug_id = Column(String(60), ForeignKey('drugs.drug_id'), nullable=False)
    search_date = Column(DateTime, nullable=False)
    search_results = Column(String(512), nullable=True)

    def __init__(self, *args, **kwargs):
        """initializes UserSearches"""
        super().__init__(*args, **kwargs)