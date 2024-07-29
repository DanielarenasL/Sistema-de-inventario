import pymongo
from Instance import connection, database
from Admin import users

user = input("Ingrese el nombre de usuario: ")
password = input("Ingrese la contraseña: ")


if user == users.find_one({"username": user}):
    if password == users.find_one({"password": password}):
        print("Bienvenido")
    else:
        print("Contraseña incorrecta")