#!/usr/bin/python
""" holds class DrugStoreInventory"""

from os import getenv
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey,\
    MetaData, Table
from sqlalchemy.orm import relationship, backref


class DrugStoreInventory(BaseModel, Base):
    """Representation of DrugStoreInventory """
    if models.storage_t == "db":
        __tablename__ = 'drug_store_inventory'
        inventory_id = Column(Integer, primary_key=True, autoincrement=True,
                              nullable=False)
        store_id = Column(Integer, ForeignKey('pharmacy_stores.store_id'), nullable=False)
        drug_id = Column(Integer, ForeignKey('drugs.drug_id'), nullable=False)
        stock_quantity = Column(Integer, nullable=False)
        created_at = Column(DateTime, nullable=False)
        updated_at = Column(DateTime)
    else:
        inventory_id = ""
        store_id = ""
        drug_id = ""
        stock_quantity = ""

    def __init__(self, *args, **kwargs):
        """initializes DrugStoreInventory"""
        super().__init__(*args, **kwargs)
