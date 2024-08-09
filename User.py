import pymongo
from Instance import connection, database
from Admin import users, products

articles = []

def Sell():
    productoID = int(input("Ingrese el ID del producto: "))
    
    if products.find_one({"_id": productoID}) is None:
        print("El ID del producto no existe en la base de datos")
    elif products.find_one({"_id": productoID}): 
        cant = int(input("Ingrese la cantidad: "))
        products.update_one({"_id": productoID}, {"$inc": {"stock": -cant}})
        another = input("¿Desea vender otro producto? (s/n): ")
        if another == "s":
            Sell()
        else:
            print("Venta realizada con éxito")
    else:
        print("No hay suficiente stock")
Sell()
