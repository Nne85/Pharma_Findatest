#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.drugs import Drug

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new Drug 1 --")
my_drug = Drug()
my_drug.name = "Omeprazole"
my_drug.description = "Manages peptic ulcer"
my_drug.category = "Peptic Ulcer Management"
my_drug.price = 30.0
my_drug.in_stock = "True"
my_drug_id = "0001"
my_drug.save()
print(my_drug)

print("-- Create a new Drug 2 --")
my_drug = Drug()
my_drug.name = "Paracetemol"
my_drug.description = "Pain relieve"
my_drug.category = "Pain Management"
my_drug.price = 57.20
my_drug.in_stock = "True"
my_drug_id = "0002"
my_drug.save()
print(my_drug)
