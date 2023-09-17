#!/usr/bin/python
""" holds class DrugStoreInventory"""

from os import getenv
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey,\
    MetaData, Table, Index
from sqlalchemy.orm import relationship, backref

storage_t = getenv("PHARMACY_Storage")


class DrugStoreInventory(BaseModel, Base):
    """Representation of DrugStoreInventory """
    __tablename__ = 'drug_store_inventory'
    if models.storage_t == "db":
        inventory_id = Column(String(60), primary_key=True, nullable=False)
        store_id = Column(String(60), ForeignKey('pharmacy_stores.store_id'), nullable=False)
        drug_id = Column(String(60), ForeignKey('drugs.drug_id'), nullable=False)
        stock_quantity = Column(Integer, nullable=False)
        created_at = Column(DateTime, nullable=False)
        updated_at = Column(DateTime)
        __table_args__ = (Index('idx_drugs_drug_id', 'drug_id'),)
    else:
        inventory_id = None
        store_id = None
        drug_id = None
        stock_quantity = None

    def __init__(self, *args, **kwargs):
        """initializes DrugStoreInventory"""
        super().__init__(*args, **kwargs)
