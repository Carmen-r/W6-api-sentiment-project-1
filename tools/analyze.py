from config.configuration import db, collection_personajes,collection_episodios,collection_sentencia
import json
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from bson import json_util, ObjectId
import pandas as pd
import plotly
import plotly.graph_objects as go

#NLTK 

nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

# Analizar sentimiento de todas la frases de toda la serie

def analyzeResultPersonaje(personaje_id):
    all_sentences = list(collection_sentencia.find({"Name":{"$eq" : personaje_id}}))
    name = json.loads(json_util.dumps(list(collection_personajes.find({"_id": ObjectId(personaje_id)},{'Name':1}))))
    all_sentences = json.loads(json_util.dumps(all_sentences))
    total_score = {"personaje_id":personaje_id , 'Personaje': name[0]['Name'], 'neg': 0.0, 'neu': 0.0, 'pos': 0.0, 'compound': 0.0}
    for i in all_sentences:
        score = sia.polarity_scores(i['Sentence'])
        total_score['neg'] += score['neg']
        total_score['pos'] += score['pos']
        total_score['neu'] += score['neu']
        total_score['compound'] += score['compound']
    return total_score


# Analizar el sentimiento de todas las frases de los personajes
def analyzeResultSerie():
    all_sentences = list(collection_sentencia.find({}))
    all_sentences = json.loads(json_util.dumps(all_sentences))
    total_score = {'neg': 0.0, 'neu': 0.0, 'pos': 0.0, 'compound': 0.0}
    for i in all_sentences:
        score = sia.polarity_scores(i['Sentence'])
        total_score['neg'] += score['neg']
        total_score['pos'] += score['pos']
        total_score['neu'] += score['neu']
        total_score['compound'] += score['compound']
    return total_score


# Todas las frases de un personaje en un episodio

def analyzeResultPersonajeEpisodio(episodio_id, personaje_id):
    all_sentences = list(collection_sentencia.find({"$and":[ {"Episode":{"$eq": episodio_id}}, {"Name":{"$eq" : personaje_id}}]}))
    all_sentences = json.loads(json_util.dumps(all_sentences))
    total_score = {'episodio_id': episodio_id, "personaje_id":personaje_id , 'neg': 0.0, 'neu': 0.0, 'pos': 0.0, 'compound': 0.0}
    for i in all_sentences:
        score = sia.polarity_scores(i['Sentence'])
        total_score['neg'] += score['neg']
        total_score['pos'] += score['pos']
        total_score['neu'] += score['neu']
        total_score['compound'] += score['compound']
    return total_score


# Analisis de todos los personajes en toda la serie

def analyzeResultallPersonajes():
    all_personajes = list(collection_personajes.find({}))
    all_personajes = json.loads(json_util.dumps(all_personajes))
    total = []
    for item in all_personajes:
        all_sentences = list(collection_sentencia.find({"Name": item['_id']['$oid']}))
        all_sentences = json.loads(json_util.dumps(all_sentences))
        name = json.loads(json_util.dumps(list(collection_personajes.find({"_id": ObjectId(item['_id']['$oid'])},{'Name':1}))))
        total_score = {"personaje_id": item['_id']['$oid'] ,'Name': name[0]['Name'], 'neg': 0.0, 'neu': 0.0, 'pos': 0.0, 'compound': 0.0}
        for i in all_sentences:
            score = sia.polarity_scores(i['Sentence'])
            total_score['neg'] += score['neg']
            total_score['pos'] += score['pos']
            total_score['neu'] += score['neu']
            total_score['compound'] += score['compound']
        total.append(total_score)
    return total



def visualization():
    total =  analyzeResultallPersonajes()
    total_df = pd.DataFrame(total)
    sample = total_df.sample(5)
    fig = go.Figure(data=[
    go.Bar(name='Negativo', x=sample['Name'], y=sample['neg']),
    go.Bar(name='Neutro',x=sample['Name'], y=sample['neu']),
    go.Bar(name='Positivo', x=sample['Name'], y=sample['pos']),
    go.Bar(name='Compound', x=sample['Name'], y=sample['compound'])
    ])

    fig.update_layout(barmode='group')
    fig.write_html("templates/sentiment.html")    
    

    