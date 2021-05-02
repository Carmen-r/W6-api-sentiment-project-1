from config.configuration import db, collection_personajes,collection_episodios,collection_sentencia
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
mydb = client["sentiment"]


# Creamos un personaje
def insertPersonaje(name):
    dic_name = {"Name": name}
    collection_personajes.insert_one(dic_name)



# Añadir un usuario al chat
def insertamensaje(id_episodio,id_personaje,frase):
    dic_insert = {
    "Episode": f"{id_episodio}",
    "Name":id_personaje,
    "Sentence": frase
    }
    collection_sentencia.insert_one(dic_insert)


# Añadir un episodio
def insertEpisodio(season, episodio):
    dic_episodio = {"Season": season, "Episode": episodio}
    collection_episodios.insert_one(dic_episodio)