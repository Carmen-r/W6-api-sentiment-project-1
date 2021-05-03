
<meta charset="utf-8"/>


<center> 
<img src= "https://i1.wp.com/codigoespagueti.com/wp-content/uploads/2019/04/game-of-thrones-serie-spin-off-cancelacion.jpg?fit=1080%2C608&quality=80&ssl=1" width="700" height="500">
</center>


## GOTAPI es una api (Application Programming Interfaces), en la que podemos recoger y aumentar informacion de la serie Juego de Tronos


### URL

url = "http://localhost:5000"

# @GET

### Base de datos
("/basedatos")

### Devuelve las sentencias de un personaje
("/sentencias/<"id_personaje>")

### Devuelve todos los personajes
("/personajes")

### Devuelve todas las sentencias/frases de los personajes
("/sentencias")


### Devuelve todas las sentencias/frases de un episodio
("/sentencias_episodio/<id_episodio>")

# @POST

### Creamos un personaje
('/personaje/create')

### Creamos nueva sentencia/frase pasandole un personaje y un episodio
("/nuevafrase")

### Creamos un nuevo episodio
('/episodio/create)

# @Analisis de sentimiento

### Analizar sentimiento de todas la frases de toda la serie de un personaje
('/analyze/sentences_serie/<id_personaje>')

### Analizar el sentimiento de todas las frases de los personajes
(/analyze/sentences_all

### Analisis de todas las frases de un personaje en un episodio 
(/analyze/sentences_episodio/<id_episodio>/<id_personaje>')

### Analisis de todos los personajes en la temporada 8
('/analyze/personajes_all')

### Visualizacion de todos los personajes
('/visualizacion_total')

### Visualizacion de 5 personajes aleatorios
('/visualizacion')

## LIBRERIAS NECESARIAS

* [Flask](https://palletsprojects.com/p/flask/)
* [NLTK](https://www.nltk.org/)
* [Jupyter](https://jupyter.org/)
* [Python](https://www.python.org/)
* [MongoDB](https://www.mongodb.com/es)


