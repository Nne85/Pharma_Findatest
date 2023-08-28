#!/usr/bin/env python3

import sys
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import BaseModel, Base
from models.drugs import Drug
from models.pharmacy_store import PharmacyStore
from models.drug_store_inventory import DrugStoreInventory
from models.user_searches import UserSearches
from models.user_favorites import UserFavorites
from models.users import User

def main():
    """ Creates the database engine """
    PHARMACY_MYSQL_USER = getenv('PHARMACY_MYSQL_USER')
    PHARMACY_MYSQL_PWD = getenv('PHARMACY_MYSQL_PWD')
    PHARMACY_MYSQL_HOST = getenv('PHARMACY_MYSQL_HOST')
    PHARMACY_MYSQL_DB = getenv('PHARMACY_MYSQL_DB')
    PHARMACY_ENV = getenv('PHARMACY_ENV')
    engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                           format(PHARMACY_MYSQL_USER,
                                  PHARMACY_MYSQL_PWD,
                                  PHARMACY_MYSQL_HOST,
                                  PHARMACY_MYSQL_DB))

    """ Create tables"""
    Base.metadata.create_all(engine)

    """ Create a session """
    Session = sessionmaker(bind=engine)
    session = Session()

    data = sys.stdin.readline().strp()
    drug = Drug(name=data)

    session.add(drug)
    session.commit()


if __name__ == "__main__":
    main()
