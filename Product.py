from Instance import database

class Product():
    def __init__(self, _id, name, price, description, stock):
        self.name = name
        self.price = price
        self._id = _id
        self.description = description
        self.stock = stock
        self.database = database["products"]
    
    def CreateProduct(self):
        
        from Functions import CreateID
        name = input("Ingrese el nombre del producto: ")
        price = float(input("Ingrese el precio del producto: "))
        id = CreateID(self.products)
        description = input("Ingrese la descripción del producto: ")
        stock = int(input("Ingrese la cantidad de producto: "))
        self.products.insert_one({"name": name, "price": price, "_id": id, "description": description, "stock": stock})
        print("Producto creado con éxito")
    
    def AddStock(self):
        productID = int(input("Ingrese el ID del producto a modificar: "))
        cant = int(input("Ingrese la cantidad a agregar: "))
        self.products.update_one({"_id": productID}, {"$inc": {"stock": cant}})
        print("Se han agregado", cant, "productos al stock")

    def DeleteProduct(self):
        productID = int(input("Ingrese el ID del producto a eliminar: "))
        self.products.delete_one({"_id": productID})
        print("Producto eliminado con éxito")