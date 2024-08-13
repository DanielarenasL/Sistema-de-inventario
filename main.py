import pymongo
from Instance import connection, database
from Admin import users
from Functions import hashing, Menu, Clean
from Product import Product

sesion = False

Product = Product(None, None, None, None, None)

    
Clean()
print("        Inicio de sesión           ")

user = input("Ingrese el nombre de usuario: ")
password = input("Ingrese la contraseña: ")
password = hashing(password)

    

if user == users.find_one({"username": user}):
    if password == users.find_one({"password": password}):
        print("Bienvenido")
        sesion = True
    else:
        print("Contraseña incorrecta")
