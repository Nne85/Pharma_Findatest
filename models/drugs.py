#!/usr/bin/python
""" holds class Drug"""
from os import getenv 
from models.base_model import BaseModel, Base
import models
import sqlalchemy
from sqlalchemy import Column, String, DateTime, Text, MetaData, Table,\
    ForeignKey, Integer, Float
from sqlalchemy.orm import relationship, backref
from sqlalchemy.types import Boolean

# Define the secondary association table for the many-to-many relationship
pharmacy_stores_drugs = Table(
    'pharmacy_stores_drugs',
    Base.metadata,
    Column('store_id', String(60), ForeignKey('pharmacy_stores.store_id')),
    Column('drug_id', String(60), ForeignKey('drugs.drug_id'))
)


class Drug(BaseModel, Base):
    """Representation of Drug """
    __tablename__ = 'drugs'
    if models.storage_t == "db":
        drug_id = Column(String(60), primary_key=True)
        name = Column(String(128), nullable=True)
        price = Column(Float, nullable=False)
        description = Column(Text, nullable=True)
        category = Column(String(128), nullable=True)
        store_id = Column(String(60), ForeignKey('pharmacy_stores.store_id'))
        in_stock = Column(Boolean, default=True)
        created_at = Column(DateTime)
        updated_at = Column(DateTime)
        
        pharmacy_stores = relationship("PharmacyStore",
                                       secondary="pharmacy_stores_drugs",
                                       back_populates="drugs")
    else:
        drug_id = None
        name = None
        price = None
        description = None
        category = None
        in_stock = None

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
