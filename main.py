import pymongo
from Instance import connection, database
from Admin import users
from Functions import hashing
from Product import Product

sesion = False
users = database["users"]
Product1 = Product(None, None, None, None, None)



if sesion == False:    
    print("        Inicio de sesión           ")

    user = input("Ingrese el nombre de usuario: ")

    password = input("Ingrese la contraseña: ")
    hpassword = hashing(password)

    user_check = users.find_one({"username": user})
        
    if user == user_check["username"] and hpassword == user_check["password"]:
    
        print("Bienvenido")
        sesion = True
    else:
        print("contraseña y/o usuario incorrecto")
else:
    print("menu")
