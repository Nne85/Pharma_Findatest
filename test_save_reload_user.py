#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.users import User

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
my_user = User()
my_user.username = "Betty"
my_user.email = "nneuka@mail.com"
my_user.search_results = "Panadol"
my_user.password = "root"
my_user.save()
print(my_user)

print("-- Create a new User 2 --")
my_user2 = User()
my_user2.first_name = "Seun"
my_user2.email = "seunjoko2@mail.com"
my_user2.password = "rootme"
my_user2.save()
print(my_user2)
