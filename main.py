import pymongo
from Instance import connection, database
from Admin import users
from Functions import hashing

user = input("Ingrese el nombre de usuario: ")
password = input("Ingrese la contraseña: ")
password = hashing(password)

if user == users.find_one({"username": user}):
    if password == users.find_one({"password": password}):
        print("Bienvenido")
    else:
        print("Contraseña incorrecta")

