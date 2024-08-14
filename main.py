from Instance import database
from Admin import InventorySystem
from Functions import Menu
from Product import Product
from User import User
from Admin import hashing

users = database["users"]
products = database["products"]
expenses = database["expenses"]

inventory_system = InventorySystem(users, products, expenses)

product_instance = Product(None, None, None, None, None)
user_instance = User(None, None, None)

sesion = False

while not sesion:  
    print("        Inicio de sesión           ")
    user = input("Ingrese el nombre de usuario: ")
    password = input("Ingrese la contraseña: ")
    hpassword = hashing(password)

    user_check = users.find_one({"username": user})
    
    if user_check and user == user_check["username"] and hpassword == user_check["password"]:
        print("Bienvenido")
        sesion = True
        break
    else:
        print("Contraseña y/o usuario incorrecto")
        sesion = False

Menu(inventory_system)