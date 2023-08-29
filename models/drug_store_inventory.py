#!/usr/bin/python
""" holds class DrugStoreInventory"""
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class DrugStoreInventory(BaseModel, Base):
    """Representation of DrugStoreInventory """
    __tablename__ = 'drug_store_inventory'
    inventory_id = Column(String(60), primary_key=True)
    store_id = Column(String(60), ForeignKey('pharmacy_stores.store_id'), nullable=False)
    drug_id = Column(String(60), ForeignKey('drugs.drug_id'), nullable=False)
    stock_quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime)

    def __init__(self, *args, **kwargs):
        """initializes DrugStoreInventory"""
        super().__init__(*args, **kwargs)