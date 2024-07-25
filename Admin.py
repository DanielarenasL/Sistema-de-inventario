import pymongo
from Instance import connection, database

users = database["vendedor"]
products = database["producto"]

def CreateID(collection):
    id = collection.count_documents({}) + 1
    return id

def CreateUsers():
    
    username = input("Ingrese el nombre de usuario: ")
    password = input("Ingrese la contraseña: ")
    id = CreateID(users)
    users.insert_one({"username": username, "password": password, "_id": id})
    print("Usuario creado con éxito")

def DeleteUser():
    userID = int(input("Ingrese el ID del usuario a eliminar: "))
    users.delete_one({"_id": userID})
    print("Usuario eliminado con éxito")


def CreateProduct():
    name = input("Ingrese el nombre del producto: ")
    price = float(input("Ingrese el precio del producto: "))
    id = CreateID(products)
    description = input("Ingrese la descripción del producto: ")
    stock = int(input("Ingrese la cantidad de producto: "))
    products.insert_one({"name": name, "price": price, "_id": id, "description": description, "stock": stock})
    print("Producto creado con éxito")

def AddStock():
    productID = int(input("Ingrese el ID del producto a modificar: "))
    cant = int(input("Ingrese la cantidad a agregar: "))
    product = products.find_one({"_id": productID})
    

def Menu():
    print("1. Crear usuario\n2. Crear producto")
    action = int(input("Ingrese la acción a realizar:"))
    if action == 1:
        CreateUsers()
    elif action == 2:
        CreateProduct()
    elif action == 3:
        DeleteUser()
Menu()



