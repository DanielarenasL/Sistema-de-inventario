import pymongo
from Instance import connection, database
from Functions import hashing, CreateID

users = database["users"]
products = database["products"]
expenses = database["expenses"]

def CreateUsers():
    username = input("Ingrese el nombre de usuario: ")
    password = input("Ingrese la contraseña: ")
    password = hashing(password)
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
    products.update_one({"_id": productID}, {"$inc": {"stock": cant}})
    print("Se han agregado", cant, "productos al stock")

def AddExpense():
    nombre = input("Ingrese el nombre del gasto: ")
    valor = float(input("Ingrese el valor del gasto: "))
    id = CreateID(expenses)
    description = input("Ingrese la descripción del gasto: ")
    expenses.insert_one({"nombre": nombre, "valor": valor, "_id": id, "description": description})

def Menu():
    print("1. Crear usuario\n2. Crear producto\n3. Eliminar usuario\n4. Agregar stock\n5. Agregar gasto")
    action = int(input("Ingrese la acción a realizar: "))
    if action == 1:
        CreateUsers()
    elif action == 2:
        CreateProduct()
    elif action == 3:
        DeleteUser()
    elif action == 4:
        AddStock()
    elif action == 5:
        AddExpense()
#Menu()



