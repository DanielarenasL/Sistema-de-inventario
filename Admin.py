from Instance import database
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





