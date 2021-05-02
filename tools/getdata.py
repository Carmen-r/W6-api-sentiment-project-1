from config.configuration import db, collection_personajes,collection_episodios,collection_sentencia
import json
from bson import json_util, ObjectId



# Todas las frases de un personaje

def mensajespersonaje(id_personaje):
    
    query = {"Name": f"{id_personaje}"}
    frases = list(collection_sentencia.find(query,{"_id": 0}))
    return frases 



# Todos los personajes de la base de datos

def personajes():
   
    users = list(collection_personajes.find( { }, {'Name':1}))
    users = json.loads(json_util.dumps(users))
    return users


# Todos los dialogos de todos los episodios

def sentencias():
    
    sentencias = list(collection_sentencia.find( { }, {'Name':1,"Episode":1, "Sentence":1}))
    sentencias = json.loads(json_util.dumps(sentencias))
    return sentencias

# Todos las sentencias de un episodio

def sentencia_episodio(id_episodio):
    query = {"Episode": f"{id_episodio}"}
    sent_episodios = list(collection_sentencia.find(query,{'Name':1,"Episode":1, "Sentence":1}))
    sent_episodios = json.loads(json_util.dumps(sent_episodios))
    return sent_episodios



