#!/usr/bin/python
""" holds class PharmacyStore"""

import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship, backref


class PharmacyStore(BaseModel, Base):
    """Representation of PharmacyStore """
    if models.storage_t == ("db"):
        __tablename__ = 'pharmacy_stores'
        store_id = Column(Integer, primary_key=True,
                          autoincrement=True, nullable=False)
        name = Column(String(128), nullable=False)
        address = Column(String(1024), nullable=True)
        city = Column(String(60), nullable=False)
        state = Column(String(60), nullable=False)
        postal_code = Column(String(20), nullable=False)
        country = Column(String(128), nullable=False)
        latitude = Column(Float, nullable=False)
        longitude = Column(Float, nullable=False)
        created_at = Column(DateTime)
        updated_at = Column(DateTime)
        drugs = relationship("Drug", back_populates="pharmacy_stores", primaryjoin="Drug.store_id==PharmacyStore.store_id")

    else:
        store_id = ""
        name = ""
        address = ""
        city = ""
        state = ""
        postal_code = ""
        country = ""
        latitude = 0.0

        longitude = 0.0

    def __init__(self, *args, **kwargs):
        """initializes PharmacyStore"""
        super().__init__(*args, **kwargs)
