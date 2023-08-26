#!/usr/bin/python
""" holds class PharmacyStore"""
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Float, DateTime
from sqlalchemy.orm import relationship


class PharmacyStore(BaseModel, Base):
    """Representation of PharmacyStore """
    __tablename__ = 'pharmacy_stores'
    store_id = Column(String(60), primary_key=True)
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

    drugs = relationship("Drug", backref="pharmacy_stores")

    def __init__(self, *args, **kwargs):
        """initializes PharmacyStore"""
        super().__init__(*args, **kwargs)