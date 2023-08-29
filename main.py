#!/usr/bin/env python3

import sys
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models
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

    # Read input data from stdin
    input_data = sys.stdin.readline().strip()

    # Extract attributes from input data
    attributes = {}
    for item in input_data.split():
        key, value = item.split('=')
        attributes[key] = value.strip('"')

    # Create instances based on input data
    if 'create' in attributes:
        create_type = attributes.pop('create')

        if create_type == 'Drug':
            instance = Drug(**attributes)
        elif create_type == 'PharmacyStore':
            instance = PharmacyStore(**attributes)
        elif create_type == 'DrugStoreInventory':
            instance = DrugStoreInventory(**attributes)
        elif create_type == 'UserSearches':
            instance = UserSearches(**attributes)
        elif create_type == 'UserFavorites':
            instance = UserFavorites(**attributes)
        elif create_type == 'User':
            instance = User(**attributes)
        else:
            print(f"Unsupported create_type: {create_type}")
            sys.exit(1)
        
        session.add(instance)
    
    session.commit()
    session.close()


if __name__ == "__main__":
    main()
