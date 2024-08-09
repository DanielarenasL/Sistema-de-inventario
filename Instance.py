from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv() #carga las variables de entorno del .env
api_key = os.getenv("MONGODB_API_KEY")

uri = f"mongodb+srv://danielarenasl:{api_key}@madtrigcrew.9iqhp.mongodb.net/?retryWrites=true&w=majority&appName=madtrigcrew"

# Create a new connection and connect to the server
connection = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    connection.admin.command('ping')
    database = connection["Inventory"]
    print("Conexion exitosa a la base de datos")
except Exception as e:
    print(e)