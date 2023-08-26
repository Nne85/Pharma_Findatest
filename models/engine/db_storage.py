#!/usr/bin/python3
"""
Contains the class PHARMACY_Storage
"""

import models
from models.drugs import Drug
from models.base_model import BaseModel, Base
from models.drugstore_inventory import DrugStoreInventory
from models.pharmacy_store import PharmacyStore
from models.user_searches import UserSearches
from models.user_favorites import UserFavorites
from models.users import User
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Drug": Drug, "PharmacyStore": PharmacyStore,
           "UserSearches": UserSearches, "UserFavorites": UserFavorites, "DrugStoreInventory": DrugStoreInventory, "User": User}


class PHARMACY_Storage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        PHARMACY_MYSQL_USER = getenv('PHARMACY_MYSQL_USER')
        PHARMACY_MYSQL_PWD = getenv('PHARMACY_MYSQL_PWD')
        PHARMACY_MYSQL_HOST = getenv('PHARMACY_MYSQL_HOST')
        PHARMACY_MYSQL_DB = getenv('PHARMACY_MYSQL_DB')
        PHARMACY_ENV = getenv('PHARMACY_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(PHARMACY_MYSQL_USER,
                                             PHARMACY_MYSQL_PWD,
                                             PHARMACY_MYSQL_HOST,
                                             PHARMACY_MYSQL_DB))
        if PHARMACY_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def save(self):
        """ saves objects to the current database session """
        self.__session.commit()

    def rollback_session(self):
        """ rollback a session """
        self.__session.rollback()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """retrieves object based on class and id """
        if cls and id:
            fetch ="{}.{}".format(cls, id)
            all.obj = self.all(cls)
            return all.obj.get(fetch)
        return None
    
    def count(self,cls=None):
        """return all object count"""
        return (len(self.all(cls)))
