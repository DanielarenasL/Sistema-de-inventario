import pymongo

#Creacion de la instancia de la base de datos
try:
    connection = pymongo.MongoClient("mongodb://localhost:27017/")
    database = connection["Inventario"]
    print("Conexión exitosa")
except:
    print("Error al conectar con la base de datos")


    
