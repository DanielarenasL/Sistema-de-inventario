from Instance import database
users = database["users"]

class User():
    def __init__(self, _id, username, password):
        self.username = username
        self.password = password
        self._id = _id
        self.admin = False
    
    def CreateUsers(self):

        from Functions import CreateID, hashing
        self.username = input("Ingrese el nombre de usuario: ")
        self.password = input("Ingrese la contraseña: ")
        self.password = hashing(self.password)
        self._id = CreateID(users)
        users.insert_one({"username": self.username, "password": self.password, "_id": self._id})
        print("Usuario creado con éxito")


