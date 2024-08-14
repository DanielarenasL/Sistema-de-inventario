import hashlib
from Admin import InventorySystem

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

def Menu(inventory_system):
    while True:
        print("\n1. Crear usuario\n2. Crear producto\n3. Eliminar usuario\n4. Agregar stock\n5. Agregar gasto\n6. Eliminar producto\n7. Salir")
        try:
            action = int(input("Ingrese la acción a realizar: "))
            if action == 1:
                inventory_system.CreateUsers()
            elif action == 2:
                inventory_system.CreateProduct()
            elif action == 3:
                inventory_system.DeleteUser()
            elif action == 4:
                inventory_system.AddStock()
            elif action == 5:
                inventory_system.AddExpense()
            elif action == 6:
                inventory_system.DeleteProduct()
            elif action == 7:
                break
            else:
                print("Por favor, ingrese un número válido.")
        except ValueError:
            print("Entrada no válida. Por favor ingrese un número.")
