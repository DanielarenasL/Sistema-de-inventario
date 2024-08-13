import hashlib, os

def hashing(password):
    hash_object = hashlib.sha3_256()
    hash_object.update(password.encode('utf-8'))
    hashed_password = hash_object.hexdigest()
    return hashed_password

def CreateID(collection):
    id = collection.count_documents({}) + 1
    return id
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

def Clean():
    os.system('cls')
