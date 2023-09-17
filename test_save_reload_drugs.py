#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.drugs import Drug

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new Drug --")
my_drugs = Drug()
my_drugs.name = "Diclofenac"
my_drugs.price= 200.55
my_drugs.description = "Pain Relieve"
my_drugs.category = "Pain Management"
my_drugs.in_stock = True
my_drugs.save()
print(my_drugs)

print("-- Create a new Drug 2 --")
my_drugs = Drug()
my_drugs.name = "Paracetemol"
my_drugs.price= 200.55
my_drugs.description = "Pain Relieve"
my_drugs.category = "Pain Management"
my_drugs.in_stock = True
my_drugs.save()
print(my_drugs)

print("-- Create a new Drug 3 --")
my_drugs = Drug()
my_drugs.name = "Vitamin C"
my_drugs.price= 200.55
my_drugs.description = "Multivitamin"
my_drugs.category = "Supplement"
my_drugs.in_stock = True
my_drugs.save()
print(my_drugs)
