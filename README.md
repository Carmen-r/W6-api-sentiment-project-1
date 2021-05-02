


<center> 
<img src= "https://i1.wp.com/codigoespagueti.com/wp-content/uploads/2019/04/game-of-thrones-serie-spin-off-cancelacion.jpg?fit=1080%2C608&quality=80&ssl=1" width="700" height="500">
</center>

## GOTAPI es una api (Application Programming Interfaces), en la que podemos recoger información de 
## de juego de tronos. Podemos coger todas las frases de todos los personajes durante la octava temporada.


### URL

url = "http://localhost:5000"

# @GET

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

### Añadimos nueva sentencia/frase pasandole un personaje y un episodio
("/nuevafrase")

### Creación de un episodio
('/episodio/create)



# LIBRERIAS NECESARIAS

* [Flask](https://palletsprojects.com/p/flask/)
* [NLTK](https://www.nltk.org/)
* [Jupyter](https://jupyter.org/)
* [Python](https://www.python.org/)
* [MongoDB](https://www.mongodb.com/es)



