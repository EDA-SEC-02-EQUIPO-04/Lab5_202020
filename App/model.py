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
        #'producer_companies': mp.newMap(1000, maptype='PROBING', loadfactor=2, comparefunction=compare_ids)
        #'producer_companies': mp.newMap(200, maptype='PROBING', loadfactor=10, comparefunction=compare_ids)
        #'producer_companies': mp.newMap(4000, maptype='PROBING', loadfactor=0.5, comparefunction=compare_ids)
        'movies_ids': mp.newMap(5000, maptype='PROBING', loadfactor=0.4, comparefunction=compare_ids),
        'producer_companies': mp.newMap(5000, maptype='PROBING', loadfactor=0.4, comparefunction=compare_producers)
    }
    return catalog

def newProducer(name,id):
    tag = {'name':'',
           'tag_id':'',
           'movies': None,
           'count':0.0}
    tag['name'] = name
    tag['tag_id'] = id
    tad['movies'] = lt.newList()
    return tag

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

def addProductionCompanies(catalog, producer_name, movie):
    producers = catalog['producer_companies']
    exitproducer = mp.contains(producers, productors_name)
    if exitproducer:
        entry = mp.get(producers, producer_name)
        producer = me.getValue(entry)
    else:
        producer = newProducer(producer_name)
        mp.put(producers, producer_name, producer)
    lt.addLast(producer['movie'], movie)

    produceravg = producer['value_average']
    movieavg = movie['value_average']
    if produceravg == 0.0:
        producer['value_average'] = float(movieavg)
    else:
        producer['value_average'] = (produceravg  + float(movieavg)/2)




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

def total_average(lista):
    total = lt.size(lista)
    votes = 0
    for i in range(lt.size(lista)):
        movie = lt.getElement(lista,i)
        votes += float(movie)
    total_vote_average = votes / total
    return round(total_vote_average,1)


def productors_movies(catalog,production):
    lista = lt.newList('ARRAYLIST')
    values_average = lt.newList('ARRAYLIST')
    lista_movies = lt.newList('ARRAYLIST')
    for i in range(lt.size(catalog['details'])):
        file = lt.getElement(catalog['details'],i)
        if production.strip().lower() == file['production_companies'].strip().lower():
            movies = file['title']
            average = file['vote_average']
            lt.addLast(values_average,average)
            lt.addLast(lista,movies)

    for i in range(lt.size(lista)):
        print('-',lt.getElement(lista,i))
           
    average_number = total_average(values_average)
    return average_number, lt.size(lista)

  

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

def compare_producers(keyname,producer):
    proentry = me.getKey(producer)
    if keyname == entry:
        return 0
    elif keyname > proentry:
        return 1
    else:
        return 0
