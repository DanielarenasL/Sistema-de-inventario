import hashlib

def hashing(password):
    hash_object = hashlib.sha3_256()
    hash_object.update(password.encode('utf-8'))
    hashed_password = hash_object.hexdigest()
    return hashed_password

def CreateID(collection):
    # Buscar el documento con el ID más alto
    ultimo_documento = collection.find_one(sort=[("_id", -1)])
    if ultimo_documento is None:
        return 1
    else:
        id = ultimo_documento["_id"] + 1
        return id

    

def Menu(Product1, User1):
    print("1. Crear usuario\n2. Crear producto\n3. Eliminar usuario\n4. Agregar stock\n5. Agregar gasto")
    action = int(input("Ingrese la acción a realizar: "))
    if action == 1:
        User1.CreateUsers()
    elif action == 2:
        Product1.CreateProduct()
    elif action == 3:
        User1.DeleteUser()
    elif action == 4:
        Product1.AddStock()
    elif action == 5:
        Product1.AddExpense()
    elif action == 6:
        Product1.DeleteProduct()
    elif action == 7:
        exit()
