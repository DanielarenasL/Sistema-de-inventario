from Instance import database
products = database["products"]

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
        self.name = input("Ingrese el nombre del producto: ")
        self.price = float(input("Ingrese el precio del producto: "))
        self._id = CreateID(products)
        self.description = input("Ingrese la descripción del producto: ")
        self.stock = int(input("Ingrese la cantidad de producto: "))
        products.insert_one({"name": self.name, "price": self.price, "_id": self._id, "description": self.description, "stock": self.stock})
        print("Producto creado con éxito")
    
    def AddStock(self):
        productID = int(input("Ingrese el ID del producto a modificar: "))
        cant = int(input("Ingrese la cantidad a agregar: "))
        products.update_one({"_id": productID}, {"$inc": {"stock": cant}})
        print("Se han agregado", cant, "productos al stock")

    def DeleteProduct(self):
        productID = int(input("Ingrese el ID del producto a eliminar: "))
        products.delete_one({"_id": productID})
        print("Producto eliminado con éxito")