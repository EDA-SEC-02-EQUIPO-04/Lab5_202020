"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """
import config
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me

assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria.
"""


# -----------------------------------------------------
# API del TAD Catalogo de películas.
# -----------------------------------------------------
def new_catalog():
    """ Inicializa el catálogo de películas

    Crea una lista vacia para guardar todas las películas.

    Se crean indices (Maps) por los siguientes criterios:
    ID películas

    Retorna el catálogo inicializado.
    """
    catalog = {
        'details': lt.newList('SINGLE_LINKED'),
        'casting': lt.newList('SINGLE_LINKED'),
        'movies_ids': mp.newMap(200, maptype='PROBING', loadfactor=0.4, comparefunction=compare_ids)
    }
    return catalog


# Funciones para agregar información al catálogo.
def add_details(catalog, movie):
    """
    Esta función adiciona detalles a la lista de películas,
    adicionalmente los guarda en un Map usando como llave su Id.
    """
    lt.addLast(catalog['details'], movie)
    mp.put(catalog['movies_ids'], movie['id'], movie)


def add_casting(catalog, movie):
    """
    Esta función adiciona un elenco a la lista de películas,
    adicionalmente lo guarda en un Map usando como llave su Id.
    """
    lt.addLast(catalog['casting'], movie)
    mp.put(catalog['movies_ids'], movie['id'], movie)


# ==============================
# Funciones de consulta
# ==============================
def details_size(catalog):
    # Número de detalles en el catálogo.
    return lt.size(catalog['details'])


def casting_size(catalog):
    # Número de elencos en el catálogo.
    return lt.size(catalog['casting'])


def show_movie_data(catalog, index):
    el = lt.getElement(catalog['details'], index)
    return (f'- {el["title"]}:'
            + f'\n   con un puntaje promedio de {el["vote_average"]} y un total de {el["vote_count"]} votaciones,'
            + f'\n   fue estrenada en {el["release_date"]} en el idioma "{el["original_language"]}".')


# ==============================
# Funciones de Comparacion
# ==============================
def compare_ids(id, tag):
    entry = me.getKey(tag)
    if int(id) == int(entry):
        return 0
    elif int(id) > int(entry):
        return 1
    else:
        return 0


# ==============================
# Opción de programa alternativa.
# ==============================

""" Opción B.
def newCatalog_movies():
    ===========
    Inicializa el catálogo de películas

    Crea una lista vacia para guardar todas las películas 

    Se crean indices (Maps) por los siguientes criterios:
     Id
     Budget 
     Genres
     IMDB Id
     Original Language
     Original Title
     Overview
     Popularity
     Production Companies
     Production Countries
     Relase Date
     Revenue
     Runtime
     Spoken Languages
     Status 
     Tag Line 
     Title 
     Vote average
     Vote count
     Production companies number 
     Production countries number 
     Spoken languages number 

     Retorna el catalogo inicializado
    ======
    catalog = {'movies': None,
               'moviesIds': None,
               'genres': None,
               'imdb_id': None,
               'original_language': None,
               'original_title': None,
               'overview': None,
               'popularity': None,
               'production_companies': None,
               'production_countries': None, 
               'relase_date': None,
               'revenue': None,
               'runtime': None,
               'spoken_languages': None,
               'status': None,
               'tag_line':None,
               'title':None,
               'vote_average':None,
               'vote_count':None,
               'production_companies_number':None,
               'production_countries_number':None}

    catalog['movies'] = lt.newList('SINGLE_LINKED')
    catalog['moviesIds'] = mp.newMap(4000,
                                    maptype = 'PROBING',
                                    loadfactor = 0.5,
                                    comparefunction = compareMapMoviesIds)
    catalog['genres'] = mp.newMap(4000,
                            maptype = 'PROBING',
                            loadfactor = 0.5,
                            comparefunction = compareMapMoviesIds)
    catalog['imdb_id'] = mp.newMap(4000,
                            maptype = 'PROBING',
                            loadfactor = 0.5,
                            comparefunction =None )
    catalog["original_language"] = mp.newMap(4000,
                            maptype = 'PROBING',
                            loadfactor = 0.5,
                            comparefunction = None)
    catalog['iriginal_title'] = mp.newMap(4000,
                            maptype = 'PROBING',
                            loadfactor = 0.5,
                            comparefunction = None)
    catalog['overview'] = mp.newMap(4000,
                            maptype = 'PROBING',
                            loadfactor = 0.5,
                            comparefunction = None)
    catalog['popularity'] = mp.newMap(4000,
                            maptype = 'PROBING',
                            loadfactor = 0.5,
                            comparefunction = None)
    catalog['production_companies'] = mp.newMap(4000,
                            maptype = 'PROBING',
                            loadfactor = 0.5,
                            comparefunction = None)
    catalog['production_countries'] = mp.newMap(4000,
                            maptype = 'PROBING',
                            loadfactor = 0.5,
                            comparefunction = None)
    catalog['relase_date'] = mp.newMap(4000,
                            maptype = 'PROBING',
                            loadfactor = 0.5,
                            comparefunction =None )
    catalog['revenue'] = mp.newMap(4000,
                            maptype = 'PROBING',
                            loadfactor = 0.5,
                            comparefunction =None )
    catalog['runtime'] = mp.newMap(4000,
                            maptype = 'PROBING',
                            loadfactor = 0.5,
                            comparefunction = None)
    catalog['spoken_language'] = mp.newMap(4000,
                            maptype = 'PROBING',
                            loadfactor = 0.5,
                            comparefunction = None)
    catalog['status'] = mp.newMap(4000,
                            maptype = 'PROBING',
                            loadfactor = 0.5,
                            comparefunction = None)
    catalog['tag_line'] = mp.newMap(4000,
                            maptype = 'PROBING',
                            loadfactor = 0.5,
                            comparefunction = None)
    catalog['title'] = mp.newMap(4000,
                            maptype = 'PROBING',
                            loadfactor = 0.5,
                            comparefunction =None )
    catalog['vote_average'] = mp.newMap(4000,
                            maptype = 'PROBING',
                            loadfactor = 0.5,
                            comparefunction = None)
    catalog['vote_count'] = mp.newMap(4000,
                            maptype = 'PROBING',
                            loadfactor = 0.5,
                            comparefunction = None)
    catalog['production_companies_number'] = mp.newMap(4000,
                            maptype = 'PROBING',
                            loadfactor = 0.5,
                            comparefunction = None )
    catalog['production_conuntries_number'] = mp.newMap(4000,
                            maptype = 'PROBING',
                            loadfactor = 0.5,
                            comparefunction = None)
    return catalog


def newCatalog_casting():
    ============
    Inicializa el catálogo del casting

    Crea una lista vacia para guardar los participantes de las 
    perlículas

    Se crean indices (Maps) por los siguientes criterios:

    Id Movie
    actor1_name
    actor1_gender
    actor2_name
    actor2_gender
    actor3_name
    actor3_gender
    actor4_name
    actor4_gender
    actor5_name
    actor5_gender
    actor_number
    director_name
    director_gender
    director_number
    producer_name
    producer_number
    screeplay_name
    editor_name

    ================

    catalog = {'Id Movie': None,
               'actor1_name': None,
               'actor1_gendre': None,
               'actor2_name': None,
               'actor2_gendre': None,
               'actor3_name': None,
               'actor3_gendre': None,
               'actor4_name': None,
               'actor4_gendre': None,'actor'
               'actor5_name': None,
               'actor5_gendre': None,
               'actor_number': None,
               'director_name': None,
               'director_gendre': None,
               'director_number' : None,
               'producer_name': None,
               'producer_number': None,
               'screenplay': None,
               'editor_name': None}
    catalog['casting'] = lt.newList('SINGLE_LINKED', compareMoviesIds)
    catalog['Id Movie'] = mp.newMap(4000,
                                    maptype= 'PROBING',
                                    loadfactor=0.5,
                                    comparefunction=None)
    catalog['actor1_name'] = mp.newMap(4000,
                                       maptype='PROBING',
                                       loadfactor=0.5,
                                       comparefunction=None)
    catalog['actor1_gender'] = mp.newMap(4000,
                                    maptype= 'PROBING',
                                    loadfactor=0.5,
                                    comparefunction=None)
    catalog['actor2_name'] = mp.newMap(4000,
                                       maptype='PROBING',
                                       loadfactor=0.5,
                                       comparefunction= None)
    catalog['actor2_gender'] = mp.newMap(4000,
                                    maptype= 'PROBING',
                                    loadfactor=0.5,
                                    comparefunction= None)
    catalog['actor3_name'] = mp.newMap(4000,
                                       maptype='PROBING',
                                       loadfactor=0.5,
                                       comparefunction= None)
    catalog['actor3_gender'] = mp.newMap(4000,
                                    maptype= 'PROBING',
                                    loadfactor=0.5,
                                    comparefunction=None)
    catalog['actor4_name'] = mp.newMap(4000,
                                       maptype='PROBING',
                                       loadfactor=0.5,
                                       comparefunction=None)           
    catalog['actor4_gender'] = mp.newMap(4000,
                                    maptype= 'PROBING',
                                    loadfactor=0.5,
                                    comparefunction= None)
    catalog['actor5_name'] = mp.newMap(4000,
                                       maptype='PROBING',
                                       loadfactor=0.5,
                                       comparefunction=None)
    catalog['actor5_gender'] = mp.newMap(4000,
                                    maptype= 'PROBING',
                                    loadfactor=0.5,
                                    comparefunction=None)
    catalog['actor_number'] = mp.newMap(4000,
                                       maptype='PROBING',
                                       loadfactor=0.5,
                                       comparefunction=None)
    catalog['director_name'] = mp.newMap(4000,
                                    maptype= 'PROBING',
                                    loadfactor=0.5,
                                    comparefunction=None)
    catalog['director_gender'] = mp.newMap(4000,
                                       maptype='PROBING',
                                       loadfactor=0.5,
                                       comparefunction=None)
    catalog['director_number'] = mp.newMap(4000,
                                    maptype= 'PROBING',
                                    loadfactor=0.5,
                                    comparefunction=None)
    catalog['producer_name'] = mp.newMap(4000,
                                       maptype='PROBING',
                                       loadfactor=0.5,
                                       comparefunction=None)    
    catalog['producer_number'] = mp.newMap(4000,
                                       maptype='PROBING',
                                       loadfactor=0.5,
                                       comparefunction=None)    
    catalog['screenplay'] = mp.newMap(4000,
                                       maptype='PROBING',
                                       loadfactor=0.5,
                                       comparefunction=None) 
    catalog['editor_name'] = mp.newMap(4000,
                                       maptype='PROBING',
                                       loadfactor=0.5,
                                       comparefunction=None)      
    return catalog

def newDirector(name):
    =========
    Crea una estructura para modelar las peliculas de un director y su
    promedio de raiting
    =========
    director = {'name': "",'movies': None, "average_raiting": 0}
    director['name'] = name
    director['movies'] = lt.newList('SINGLE_LINKERD',compareDirectorsByName)
    return director
"""

""" Opción 2.
def addMovie(catalog, movie):
    # Esta función adiciona una película a la lista de películas,
    # adicionalmente lo guarda en un Map usando com llave su Id.
    lt.addLast(catalog['movies'], movie)
    mp.put(catalog['moviesIds'], movie['id'], movie)


def addMovieDirector(catalog_movies, catalog_casting, directorname, movie):
    # Esta función adiciona una película a la lista de películas dirigidas
    # por un director
    # Cuando se adiciona el libro, se actualiza el promedio de dicho autor
    directors = catalog_casting['director_name']
    movies = catalog_movies['movies']
    existdirector = mp.contains(directors, directorname)
    existmovie = mp.contains(movies, movie)
    if existdirector:
        entry = mp.get(directors,directorname)
        value = mp.getValue(entry)
    else:
        director = newDirector(directorname)
        mp.put(directors,directors,director)
"""

# ==============================
# Funciones de consulta
# ==============================

""" Opcion 3
def movies_size(catalog):
    return lt.size(catalog['movies'])


def casting_size(catalog):
    return lt.size(catalog['casting'])
...
"""
""" Opción 2.
def moviesSize(catalog):
    # Número de películas en el catago
    return lt.size(catalog['movies'])


def movie_name(catalog, position):
    # Devuelve el nombre de la película
    lista = lt.getElement(catalog['movies'], position)
    return lista['title'] 


def movie_vote_average(catalog, position):
    # Devuelve el vote average de la película   
    lista = lt.getElement(catalog['movies'],position)
    return lista['vote_average'] 


def movie_relase_date(catalog, position):
    # Devuelve la fecha de estreno de la película
    lista = lt.getElement(catalog['movies'],position)
    return lista['release_date']


def movie_vote_count(catalog, position):
    # Devuelve el número de votos de la película
    lista = lt.getElement(catalog['movies'],position)
    return lista ['vote_count']


def movie_language(catalog, position):
    # Devuelve el lenguaje en el que se habla la película
    lista = lt.getElement(catalog['movies'],position)
    return lista ['original_language']
"""

"""Opcion 3
def new_catalog():

      catalog = {
        'movies': lt.newList('SINGLE_LINKED'),
        'casting': lt.newList('SINGLE_LINKED'),
        'movie_id': mp.newMap(200, maptype='PROBING', loadfactor=0.4, comparefunction=compare_ids)
    }
    return catalog

# Funciones para agregar informacion al catalogo
def add_movies(catalog, movie):
    lt.addLast(catalog['movies'], movie)
    mp.put(catalog['movie_id'], movie['id'], movie)

def add_casting(catalog, movie):
    lt.addLast(catalog['casting'], movie)
    mp.put(catalog['movie_id'], movie['id'], movie)

...
"""

# ==============================
# Funciones de Comparacion
# ==============================
""" Opcion 3
def comp_id(id,movies)
    first = lt.getElement(catalog['movies'['id']])
    if id == first:
        return 0
    elif id > first:
        return 1
    else:
        -1
...
"""
""" Opción 2.
def compareMoviesIds(id1, id2):
    # Compara dos ids de película
    # Args:
    # id1 (int): Id Película i
    # id2 (int): Id Película i+1
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1


def compareMapMoviesIds(id, entry):
    # Compara dos ids de las películas, id es un identificador
    # y entry una pareja llave-valor
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1


def compareDirectorsByName(keyname, director)
    # Compara dos nombres de directores. El primero es una cadena
    # y el segundo un entry de un map
    authentry = me.getKey(author)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1
"""
