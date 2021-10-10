"""
 * Copyright 2020, Departamento de sistemas y Computación,
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
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

#####-----#####-----#####-----#####-----#####-----#####   ####---#####---####   #####-----#####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####-----#####   IMPORTACIÓN MÓDULOS   #####-----#####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####-----#####   ####---#####---####   #####-----#####-----#####-----#####-----#####-----#####

import config as cf
import model
import csv
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp




#####-----#####-----#####-----#####-----#####   ##########-----###########-----##########   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   FUNCIONES INICIALIZACIÓN Y CARGA DE DATOS   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   ##########-----###########-----##########   #####-----#####-----#####-----#####-----#####

"""
    Se definen las funciones que permitirán inicializar el catálogo del museo y cargar
    los elementos de la base de datos.

"""

# Función que inicializa y retorna el catálogo.
def init_catalog () -> dict:
    """
        Esta función invoca a la función nuevo_catalogo de model.py para crear y retornar al catálogo.

        No tiene parámetros.

        Retorno:
            -> (dict): el catálogo. 

    """

    # Invocar función new_Catalog() de model.py, guardar su retorno en la variable catalog y retornarla.
    catalog = model.new_catalog()
    return catalog



# Función que carga toda la información al catálogo.
def load_data (catalog: dict) -> None:
    """
        Esta función carga toda la información al catálogo, y lo hace invocando a las 
        funciones load_artists() y load_artworks.

        Parámetro:
            -> catalog (dict): catálogo.

        No tiene retorno.

    """

    # Cargar artistas.
    load_artists(catalog)

    # Cargar obras.
    load_artworks(catalog)



# Función que carga todos los artistas.
def load_artists (catalog: dict) -> None:
    """
        Esta función carga la información que se encuentra en la base de datos de todos
        los artistas al catálogo.

        Lo que hace es cargar toda la información de cada artista presente en la base de datos.
        Luego, para cargar la infomación al catálogo, hace lo siguiente:
            -> Mediante la función add_artist() carga la información del artista al catálogo.
            -> Mediante la función add_BeginDate() carga la información del artista al map "BeginDate"
               del catálogo.
        

        Parámetro:
            -> catalog (dict): el catálogo.

        No tiene retorno.
        
    """

    # Crear variable que guarda la referencia al archivo de los artistas.
    artists_file = cf.data_dir + '\\MoMA\\Artists-utf8-small.csv'

    # Crear variable que guarda todos los artistas.
    input_file = csv.DictReader(open(artists_file, encoding='utf-8'))


    # Iterar sobre cada artista del catálogo.
    for artist_info in input_file:
        
        # Añadirlo a la lista 'artists' del catálogo.
        model.add_artist(catalog, artist_info)

        # Determinar su año de nacimiento.
        artists_BegDat = int(float(artist_info["BeginDate"]))

        # Añadirlo al map "BeginDate" si su año de nacimiento está registrado.
        if not (artists_BegDat == 0):
            model.add_BeginDate(catalog, artists_BegDat, artist_info)



# Función que carga todas las obras.
def load_artworks (catalog: dict) -> None:
    """
        Esta función carga la información que se encuentra en la base de datos de todas
        las obras al catálogo.

        Lo que hace es cargar toda la información de cada obra presente en la base de datos.
        Luego, mediante la función add_artwork() carga la información de la obra al catálogo.

        Parámetro:
            -> catalog (dict): el catálogo.

        No tiene retorno.
        
    """

    # Crear variable que guarda la referencia al archivo de las obras.
    artworks_file = cf.data_dir + '\\MoMA\\Artworks-utf8-small.csv'

    # Crear variable que guarda todas las obras.
    input_file = csv.DictReader(open(artworks_file, encoding='utf-8'))

    # Añadir cada obra al catálogo.
    for artwork_info in input_file:
        model.add_artwork(catalog, artwork_info)









# Inicialización del Catálogo de libros

# Funciones para la carga de datos

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo



# Pruebas.

catalog = init_catalog()
load_data(catalog)

resp = model.req_1(catalog, 1920, 1985)
print(lt.size(resp))
print(lt.getElement(resp, 1)["ConstituentID"], lt.getElement(resp, 1)["BeginDate"])
print(lt.getElement(resp, 2)["ConstituentID"], lt.getElement(resp, 2)["BeginDate"])
print(lt.getElement(resp, 3)["ConstituentID"], lt.getElement(resp, 3)["BeginDate"])
print(lt.getElement(resp, lt.size(resp) - 2)["ConstituentID"], lt.getElement(resp, lt.size(resp) - 2)["BeginDate"])
print(lt.getElement(resp, lt.size(resp) - 1)["ConstituentID"], lt.getElement(resp, lt.size(resp) - 1)["BeginDate"])
print(lt.getElement(resp, lt.size(resp))["ConstituentID"], lt.getElement(resp, lt.size(resp))["BeginDate"])

"""
# Mapa BeginDate.
mapa_begdat = catalog["BeginDate"]


lista_acual = mp.get(mapa_begdat, 1944)['value']
iterador_elem_lista = lt.iterator(lista_acual)

for elemento in iterador_elem_lista:
    print(elemento)
"""