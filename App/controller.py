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
