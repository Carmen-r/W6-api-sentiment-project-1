import os
import dotenv
from pymongo import MongoClient

dotenv.load_dotenv()

dburl = os.getenv("URL")

print(dburl)
if not dburl:
    raise ValueError("no tienes url mongodb")

# Conectamos con la base de datos mongo
client = MongoClient("mongodb://localhost/sentiment")
db = client.get_database()
# collection = db["juego"]
collection_episodios = db["episodios"]
collection_personajes = db["personajes"]
collection_sentencia = db["sentencia"]