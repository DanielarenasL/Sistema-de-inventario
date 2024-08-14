from Instance import database
users = database["users"]

class User():
    def __init__(self, _id, username, password):
        self.username = username
        self.password = password
        self._id = _id
    
    def CreateUsers(self):

        from Functions import CreateID, hashing
        self.username = input("Ingrese el nombre de usuario: ")
        self.password = input("Ingrese la contraseña: ")
        self.password = hashing(self.password)
        self._id = CreateID(users)
        users.insert_one({"username": self.username, "password": self.password, "_id": self._id, "admin": False})
        print("Usuario creado con éxito")

    def DeleteUser(self):

        userID = int(input("Ingrese el ID del usuario a eliminar: "))
        users.delete_one({"_id": userID})
        print("Usuario eliminado con éxito")


