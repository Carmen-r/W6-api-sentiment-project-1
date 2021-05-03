from config.configuration import db,collection_juego, collection_personajes,collection_episodios,collection_sentencia
import json
from bson import json_util, ObjectId



# Base de datos de juego de tronos
def bdmongo():
    query = {}
    todo = list(collection_juego.find(query,{"_id": 0, "Release Date": 1,"Season": 1, "Episode": 1, "Episode Title": 1,"Name": 1, "Sentence": 1}))
    return todo



# Todas las frases de un personaje 

def mensajespersonaje(id_personaje):
    
    query = {"Name": f"{id_personaje}"}
    frases = list(collection_sentencia.find(query,{"_id": 0}))
    return frases 

# Todos los personajes de la base de datos

def personajes():
   
    personajes = list(collection_personajes.find( { }, {'Name':1}))
    personajes = json.loads(json_util.dumps(personajes))
    return personajes


# Todos los dialogos de todos los episodios

def sentencias():
    total_sentences = []
    sentencias = list(collection_sentencia.find( { }, {'Name':1,"Episode":1, "Sentence":1}))
    sentencias = json.loads(json_util.dumps(sentencias))
    for item in sentencias:
        episodio = json.loads(json_util.dumps(list(collection_episodios.find({"_id": ObjectId(item['Episode'])},{'Episode':1}))))
        name = json.loads(json_util.dumps(list(collection_personajes.find({"_id": ObjectId(item['Name'])},{'Name':1}))))
        sentence = {"personaje_id": item['_id']['$oid'] ,'Name': name[0]['Name'],'Episode': episodio[0]['Episode'],'Episode_id': item["Episode"],'Sentence': item["Sentence"]}
        total_sentences.append(sentence)
    return total_sentences
    

# Todos las sentencias de un episodio

def sentencia_episodio(id_episodio):
    total_sentences = []
    sent_episodios = list(collection_sentencia.find({"Episode": f"{id_episodio}"},{'Name':1,"Episode":1, "Sentence":1}))
    sent_episodios = json.loads(json_util.dumps(sent_episodios))
    for item in sent_episodios:
        episodio = json.loads(json_util.dumps(list(collection_episodios.find({"_id": ObjectId(item['Episode'])},{'Episode':1}))))
        name = json.loads(json_util.dumps(list(collection_personajes.find({"_id": ObjectId(item['Name'])},{'Name':1}))))
        sentence = {"personaje_id": item['_id']['$oid'] ,'Name': name[0]['Name'],'Episode': episodio[0]['Episode'],'Episode_id': item["Episode"],'Sentence': item["Sentence"]}
        total_sentences.append(sentence)
    return total_sentences



