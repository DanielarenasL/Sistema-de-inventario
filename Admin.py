import hashlib
from Instance import database

users = database["users"]
products = database["products"]
expenses = database["expenses"]

def hashing(password):
    hash_object = hashlib.sha3_256()
    hash_object.update(password.encode('utf-8'))
    hashed_password = hash_object.hexdigest()
    return hashed_password

def CreateID(collection):
    ultimo_documento = collection.find_one(sort=[("_id", -1)])
    if ultimo_documento is None:
        return 1
    else:
        id = ultimo_documento["_id"] + 1
        return id

class InventorySystem:
    def __init__(self, users, products, expenses):
        self.users = users
        self.products = products
        self.expenses = expenses

    def CreateUsers(self):
        username = input("Ingrese el nombre de usuario: ")
        while True:
            password = input("Ingrese la contraseña: ")
            if len(password) < 8:
                print("La contraseña debe tener al menos 8 caracteres.")
            else:
                break
        password = hashing(password)
        id = CreateID(self.users)
        self.users.insert_one({"username": username, "password": password, "_id": id})
        print("Usuario creado con éxito")

    def DeleteUser(self):
        try:
            userID = int(input("Ingrese el ID del usuario a eliminar: "))
            result = self.users.delete_one({"_id": userID})
            if result.deleted_count > 0:
                print("Usuario eliminado con éxito")
            else:
                print("Usuario no encontrado")
        except ValueError:
            print("ID no válido. Ingrese un número entero.")

    def CreateProduct(self):
        name = input("Ingrese el nombre del producto: ")
        try:
            price = float(input("Ingrese el precio del producto: "))
            stock = int(input("Ingrese la cantidad de producto: "))
        except ValueError:
            print("Entrada no válida. Precio y stock deben ser números.")
            return
        id = CreateID(self.products)
        description = input("Ingrese la descripción del producto: ")
        self.products.insert_one({"name": name, "price": price, "_id": id, "description": description, "stock": stock})
        print("Producto creado con éxito")

    def AddStock(self):
        try:
            productID = int(input("Ingrese el ID del producto a modificar: "))
            cant = int(input("Ingrese la cantidad a agregar: "))
            result = self.products.update_one({"_id": productID}, {"$inc": {"stock": cant}})
            if result.matched_count > 0:
                print(f"Se han agregado {cant} productos al stock")
            else:
                print("Producto no encontrado")
        except ValueError:
            print("Entrada no válida. ID y cantidad deben ser números enteros.")

    def AddExpense(self):
        nombre = input("Ingrese el nombre del gasto: ")
        try:
            valor = float(input("Ingrese el valor del gasto: "))
        except ValueError:
            print("Valor no válido. Ingrese un número.")
            return
        id = CreateID(self.expenses)
        description = input("Ingrese la descripción del gasto: ")
        self.expenses.insert_one({"nombre": nombre, "valor": valor, "_id": id, "description": description})
        print("Gasto registrado con éxito")

    def DeleteProduct(self):
        try:
            productID = int(input("Ingrese el ID del producto a eliminar: "))
            result = self.products.delete_one({"_id": productID})
            if result.deleted_count > 0:
                print("Producto eliminado con éxito")
            else:
                print("Producto no encontrado")
        except ValueError:
            print("ID no válido. Ingrese un número entero.")
