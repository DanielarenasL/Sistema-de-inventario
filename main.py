from Instance import database
from Admin import users
from Functions import hashing, Menu
from Product import Product
from User import User

Product1 = Product(None, None, None, None, None)
User1 = User(None, None, None)
global sesion 
sesion = False
users = database["users"]



while not sesion:  
    print("        Inicio de sesión           ")

    user = input("Ingrese el nombre de usuario: ")

    password = input("Ingrese la contraseña: ")
    hpassword = hashing(password)

    user_check = users.find_one({"username": user})
            
    if user == user_check["username"] and hpassword == user_check["password"]:
        
        print("Bienvenido")
        sesion = True
        break
    else:

        print("contraseña y/o usuario incorrecto")
        sesion = False
Menu(Product1, User1)

