import hashlib

def hashing(password):
    hash_object = hashlib.sha3_256()
    hash_object.update(password.encode('utf-8'))
    hashed_password = hash_object.hexdigest()
    return hashed_password

def CreateID(collection):
    id = collection.count_documents({}) + 1
    return id

def Menu(Product1):
    print("1. Crear usuario\n2. Crear producto\n3. Eliminar usuario\n4. Agregar stock\n5. Agregar gasto")
    action = int(input("Ingrese la acción a realizar: "))
    if action == 1:
        Product1.CreateUsers()
    elif action == 2:
        Product1.CreateProduct()
    elif action == 3:
        Product1.DeleteUser()
    elif action == 4:
        Product1.AddStock()
    elif action == 5:
        Product1.AddExpense()
    elif action == 6:
        exit()
