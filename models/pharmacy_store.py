#!/usr/bin/python
""" holds class PharmacyStore"""

import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, Float, ForeignKey, DateTime, Index
from sqlalchemy.orm import relationship, backref

storage_t = getenv("PHARMACY_Storage")


class PharmacyStore(BaseModel, Base):
    """Representation of PharmacyStore """
    __tablename__ = 'pharmacy_stores'
    if models.storage_t == ("db"):
        store_id = Column(String(60), primary_key=True)
        name = Column(String(128), nullable=True)
        address = Column(String(1024), nullable=True)
        city = Column(String(60), nullable=False)
        state = Column(String(60), nullable=False)
        postal_code = Column(String(20), nullable=False)
        country = Column(String(128), nullable=False)
        latitude = Column(Float, nullable=False)
        longitude = Column(Float, nullable=False)
        created_at = Column(DateTime)
        updated_at = Column(DateTime)
        drugs = relationship("Drug", back_populates="pharmacy_stores",
                             secondary="pharmacy_stores_drugs")
        __table_args__ = (
            Index('idx_store_id', 'store_id'),)
    else:
        store_id = None
        name = None
        address = None
        city = None
        state = None
        postal_code = None
        country = None
        latitude = None

        longitude = None

    def __init__(self, *args, **kwargs):
        """initializes PharmacyStore"""
        super().__init__(*args, **kwargs)
