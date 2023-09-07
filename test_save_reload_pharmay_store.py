#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.pharmacy_store import PharmacyStore

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new  Pharmacy Store --")
my_pharmacy = PharmacyStore()
my_pharmacy.name = "Lanyard Pharmacy"
my_pharmacy.address = "Plot 12 New Road, Apapa, Lagos"
my_pharmacy.city = "Lagos"
my_pharmacy.state = "Lagos"
my_pharmacy.portal_code = "LA"
my_pharmacy.country = "Nigeria"
my_pharmacy.store_id = "0001"
my_pharmacy.latitude = 127.8
my_pharmacy_longitude = 55.9
my_pharmacy.save()
print(my_pharmacy)

print("-- Create a new Pharmacy 2 --")
my_pharmacy = PharmacyStore()
my_pharmacy.name = "Alpha_Plus Pharmacy"
my_pharmacy.address = "No 13. Mathias Okonkwo, Lagos"
my_pharmacy.city = "Lagos"
my_pharmacy.state = "Lagos"
my_pharmacy.portal_code = "LA"
my_pharmacy.country = "Nigeria"
my_pharmacy.store_id = "0002"
my_pharmacy.latitude = 127.87
my_pharmacy_longitude = 85.9
my_pharmacy.save()
print(my_pharmacy)
