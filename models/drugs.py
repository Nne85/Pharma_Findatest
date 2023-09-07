#!/usr/bin/python
""" holds class Drug"""
from os import getenv 
from models.base_model import BaseModel, Base
import models
import sqlalchemy
from sqlalchemy import Column, String, DateTime, Text, MetaData, Table,\
    ForeignKey, Integer
from sqlalchemy.orm import relationship, backref
from sqlalchemy.types import Boolean


class Drug(BaseModel, Base):
    """Representation of Drug """
    if models.storage_t == "db":
        __tablename__ = 'drugs'
        drug_id = Column(Integer, primary_key=True, autoincrement=True,
                        nullable=False)
        name = Column(String(128), nullable=False)
        price = Column(Float, nullable=False)
        description = Column(Text, nullable=True)
        category = Column(String(128), nullable=True)
        store_id = Column(Integer, ForeignKey('pharmacy_stores.store_id'))
        in_stock = Column(Boolean, default=True)
        created_at = Column(DateTime)
        updated_at = Column(DateTime)
        
        pharmacy_stores = relationship("PharmacyStore", back_populates="drugs", primaryjoin="Drug.store_id==PharmacyStore.store_id")
    else:

        drug_id = ""
        name = ""
        price = 0
        store_id = ""
        description = ""
        category = ""
        in_stock = "True"

    def __init__(self, *args, **kwargs):
        """initializes Drug"""
        super().__init__(*args, **kwargs)

    if models.storage_t != 'db':
        @property
        def pharmacy_stores(self):
            """getter attribute returns the list of PharmacyStore instances"""
            pharmacy_stores_list = []
            all_stores = models.storage.all(models.PharmacyStore)
            for store in all_stores.values():
                if self in store.drugs:
                    pharmacy_stores_list.append(store)
            return pharmacy_stores_list
        
    def is_in_stock(self):
        """Checks if the drug is in stock"""
        pharmacy_stores = self.pharmacy_stores
        for store in pharmacy_stores:
            if store.stock_quantity > 0:
                return True
            return False
