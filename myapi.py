import re
from flask import Flask, request, render_template
from flask import jsonify
import tools.getdata as get
import json
import markdown.extensions.fenced_code
import tools.getdata as get
import tools.postdata as pos
from tools.analyze import analyzeResultPersonaje,analyzeResultPersonajeEpisodio, analyzeResultSerie, analyzeResultallPersonajes, visualization
from tools.errorHandler import jsonErrorHandler
from pymongo import MongoClient
import numpy as np
import plotly
import plotly.graph_objects as go
# import nltk





app = Flask(__name__,template_folder='templates')




client = MongoClient("mongodb://localhost:27017")
mydb = client["sentiment"]

@app.route("/")
def index():
    readme_file = open("Readme.md", "r")
    md_template = markdown.markdown( 
        readme_file.read(), extensions=["fenced_code"]
    )
    return md_template

### GET 

# Devuelve las sentencias de un personaje
@jsonErrorHandler
@app.route("/sentencias/<id_personaje>")
def frasespersonaje(id_personaje):
    frases = get.mensajespersonaje(id_personaje)
    return jsonify(frases)

# Devuelve todos los personajes
@jsonErrorHandler
@app.route("/personajes")
def todoslospersonajes():
    personajes = get.personajes()
    return jsonify(personajes)

# Devuelve todas las sentencias
@app.route("/sentencias")
def todaslassentencias():
    sentencias = get.sentencias()
    return jsonify(sentencias)

# Devuelve todas las sentencias de un episodio
@app.route("/sentencias_episodio/<id_episodio>")
def todassentencias_episodio(id_episodio):
    sentencia_episodio = get.sentencia_episodio(id_episodio)
    return jsonify(sentencia_episodio)



### POST
# Creamos un personaje
@app.route('/personaje/create', methods=["POST"])
def insert_Personaje():
    name = request.form.get("Name")
    pos.insertPersonaje(name)
    return "Se ha introducido el personaje en la base de datos"




# Añadimos nueva frase pasandole un personaje y un episodio con POST
@app.route("/nuevafrase", methods=["POST"])
def insertamensaje():
    id_episodio = request.form.get("Episode") 
    id_personaje = request.form.get("Name")
    frase = request.form.get("Sentence")
    pos.insertamensaje(id_episodio,id_personaje,frase)
    return "Se ha introducido el mensaje en la base de datos"


# Creamos un episodio
@app.route('/episodio/create', methods=["POST"])
def insert_Episodio():
    episodio = request.form.get("Episode")
    season = request.form.get("Season")
    pos.insertEpisodio(season,episodio)
    return "Se ha introducido el episodio en la base de datos"


# ANALISIS SENTIMIENTO
# Analizar sentimiento de todas la frases de toda la serie de un personaje
@app.route('/analyze/sentences_serie/<id_personaje>')
def analyze_sentences_serie(id_personaje):
    result = analyzeResultPersonaje(id_personaje)
    return result


# Analizar el sentimiento de todas las frases de los personajes
@app.route('/analyze/sentences_all')
def analyze_sentences_all():
    result = analyzeResultSerie()
    return result

# Analisis de todas las frases de un personaje en un episodio 
@app.route('/analyze/sentences_episodio/<id_episodio>/<id_personaje>')
def analyze_sentences_episodio(id_episodio,id_personaje):
    result = analyzeResultPersonajeEpisodio(id_episodio,id_personaje)
    return result

# Analisis de todos los personajes en toda la serie
@app.route('/analyze/personajes_all')
def analyze_result_all_personajes():
    result = analyzeResultallPersonajes()
    return jsonify(result)


# Visualizacion
@app.route('/visualizacion')
def line():
    visualization()
    return render_template('sentiment.html')



app.run("0.0.0.0", 5000, debug=True)