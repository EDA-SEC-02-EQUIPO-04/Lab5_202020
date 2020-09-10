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

import config as cf
from App import model
import csv

"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta. Esta responsabilidad
recae sobre el controlador.
"""


# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________
def init_catalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    # catalog es utilizado para interactuar con el modelo.
    catalog = model.new_catalog()
    return catalog


# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________
def load_data(catalog, casting_file, details_file):
    """
    Carga los datos de los archivos en el modelo
    """
    load_details(catalog, details_file)
    load_casting(catalog, casting_file)


def load_details(catalog, details_file):
    """
    Carga cada una de las lineas del archivo de detalles.
    - Se agrega cada película al catalogo de películas.
    - Por cada libro se encuentran sus autores y por cada
      autor, se crea una lista con sus libros
    """
    dialect, dialect.delimiter = csv.excel(), ';'
    with open(details_file, encoding='utf-8-sig') as input_file:
        file_reader = csv.DictReader(input_file, dialect=dialect)
        for movie in file_reader:
            model.add_details(catalog, movie)


def load_casting(catalog, casting_file):
    """
    Carga en el catalogo el elenco a partir de la información
    del archivo de casting.
    """
    dialect, dialect.delimiter = csv.excel(), ';'
    with open(casting_file, encoding='utf-8-sig') as input_file:
        file_reader = csv.DictReader(input_file, dialect=dialect)
        for movie in file_reader:
            model.add_casting(catalog, movie)


# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________
def details_size(catalog):
    # Numero de detallesleídos.
    return model.details_size(catalog)


def casting_size(catalog):
    # Numero de elencos leídos.
    return model.casting_size(catalog)


def show_movie(catalog, index):
    print(model.show_movie_data(catalog, index))


# ==============================
# Opción de programa alternativa.
# ==============================
# Opción 1.
"""
def initCatalog_movies():
||||"""
# Llama la función de inicialización del catalogo de películas del modelo.

"""
# catalog_movies es utilizado para interactuar con el modelo de películas
catalog_movies = model.newCatalog_movies()
# catalog_casting es utilizado para interactural con l modelo de casting
return catalog_movies
"""

# Opción 1
"""
def loadData(catalog_movies, movies):
    """
# Carga los datos de los archivos del modelo

# Args:
#   movies (csv): Archivo  que contiene las películas
#  casting (csv): Archivo que contiene el casting de las películas
"""
loadMovies(catalog_movies, movies)
"""
# Opción 1
"""
def loadMovies(catalog, moviesfile):
    """
# Carga cada una de las lineas del archivo de movies
"""
dialect = csv.excel()
dialect.delimiter =';'
with open(moviesfile,encoding='utf-8-sig') as input_file:
    file_reader = csv.DictReader(input_file, dialect=dialect)
    for movie in file_reader:
        model.addMovie(catalog, movie)    
"""
""" Opcion 2
def init_catalog():
    # catalog es utilizado para interactuar con el modelo.
    catalog = model.new_catalog()
    return catalog

def MoviesCatalog():
    moviesCatalog = model.newMoviesCatalog()
    return moviesCatalog

def CastingCatalog():
    castingCatalog = model.newCastingCatalog()
    return  castingCatalog
    
def loadData(moviesCatalog, castingCatalog, movies, casting):
    loadMovies(castingCatalog, casting)
    loadMovies(moviesCatalog, movies)

def loadMovies(moviesCatalog, catalog):
    dialect = csv.excel()
    dialect.delimiter =';'
    with open(moviesCatalog,encoding='utf-8-sig') as input_file:
        file_reader = csv.DictReader(input_file, dialect=dialect)
        for movie in file_reader:
            model.addMovie(moviesCatalog, movie) 

def loadCasting(castingCatalog,catalog):
    dialect = csv.excel()
    dialect.delimiter =';'
    with open(moviesCatalog,encoding='utf-8-sig') as input_file:
        file_reader = csv.DictReader(input_file, dialect=dialect)
        for movie in file_reader:
            model.addCatsing(castingCatalog, movie) 

 
def movies_size(catalog):
    # Número de películas leídas
    return model.moviesSize(catalog)



def movies_data(catalog, position):
    # Devuelve el vote average de la película
    return model.movie_name(catalog,position),model.movie_relase_date(catalog,position),model.movie_vote_average(catalog,position), model.movie_vote_count(catalog,position),model.movie_language(catalog, position)
"""
