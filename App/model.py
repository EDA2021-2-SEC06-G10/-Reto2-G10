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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """

#####-----#####-----#####-----#####-----#####   ####---#####---####   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   IMPORTACIÓN MÓDULOS   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   ####---#####---####   #####-----#####-----#####-----#####-----#####

import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf




#####-----#####-----#####-----#####-----#####   ########-----######-----########   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   DEFINICIÓN ESTRUCTURAS ELEMENTOS   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   ########-----######-----########   #####-----#####-----#####-----#####-----#####

"""
    Se define la estructura que contiene el catálogo del museo.
    Este tendrá dos listas, una para los artistas y otra para las obras.
    Además, tendrá una serie de maps que guardarán información de interés de cada grupo de
    elementos, como la fecha de nacimiento de los artistas y la técnica de las obras.

"""

# Función que crea el catálogo.
def new_catalog () -> dict:
    """
        Esta función permite crear la estructura de datos que guarda el catálogo del museo.
        
        Crea dos listas vacías que permitirán guardar los siguientes elementos:
         1- Los artistas.
         2- Las obras.

        Además, la función crea los siguientes maps, los cuales guardarán información de interés de cada grupo de elementos:
         1- Mediums: guarda la información de las obras que fueron creadas usando la técnica de la llave respectiva.


        No tiene parámetros.

        Retorno:
            -> (dict): el catálogo del museo.

    """

    # Definir variable que guarda la información del catálogo e inicializar las parejas llave-valor.
    catalog = {'artists': None,
               'artworks': None,
               'BeginDate': None}


    #####-----#####-----#####-----#####   Definición Listas de Elementos   #####-----#####-----#####-----#####
    """
        La siguiente lista contiene la información de todos los artistas encontrados en  los archivos de carga.
        Estos no están ordenadas bajo ningún criterio, y son referenciados por los índices que se definirán en 
        seguida.

        Cada artista se representa mediante un diccionario, cuyas parejas llave-valor representan información
        relevante de cada artista (como su nombre, id, fecha de nacimiento, entre otros). Toda la información
        que se guarda de cada artista se especfica detalladamente en la función new_artist(). 
    
    """
    catalog['artists'] = lt.newList('SINGLE_LINKED')            # Pendiente añadir función de comparación.
    
    """
        La siguiente lista contiene la información de todas las obras encontradas en  los archivos de carga.
        Estas no están ordenadas bajo ningún criterio, y son referenciadas por los índices que se definirán en 
        seguida.

        Cada obra se representa mediante un diccionario, cuyas parejas llave-valor representan información
        relevante de cada obra (como su título, los id de sus autores, entre otros). Toda la información
        que se guarda de cada obra se especfica detalladamente en la función new_artwork(). 
    
    """
    catalog['artworks'] = lt.newList('SINGLE_LINKED')            # Pendiente añadir función de comparación.


    #####-----#####-----#####   Definición Maps/Índices   #####-----#####-----#####

    """
        A continuacion se crearán maps por diferentes criterios
        para llegar a la informacion requerida. Estos no replican información,
        solo referencian los elementos de las listas de artistas y obras.
    
    """

    # Map cuyas llaves son años de nacimiento y cuyas llaves son listas enlazadas que contienen
    # información relevante de los artistas que nacieron el año correspondiente.
    catalog["BeginDate"] = mp.newMap(10000, maptype='CHAINING', loadfactor=4.0,)   # Determinar tipo de mapa y tamaño adecuados.


    #####-----#####-----#####-----#####   Retorno   #####-----#####-----#####-----#####

    return catalog




#####-----#####-----#####-----#####-----#####   ###---###----###   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   ADICIÓN DE DATOS   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   ###---###----###   #####-----#####-----######-----####-----#####

"""
    Se definen las funciones que permitirán añadir elementos al catálogo.

"""

# Función que agrega un artista al catálogo.
def add_artist (catalog: dict, artist_info: dict) -> None:
    """
        Esta función permite crear y agregar un artista al catálogo usando la información
        pasada por parámetro y guardándolo en la lista "artists".

        Parámetros:
            -> catalog (dict): catálogo.
            -> artist_info (dict): información del artista que se quiere adicionar. 

        No tiene retorno.

    """
    
    # Crear un artista con los datos ingresados por parámetro.
    artist_new = new_artist(artist_info)

    # Agregar el artista a la última posición de la lista "artists".
    lt.addLast(catalog['artists'], artist_new)



# Función que agrega una obra al catálogo.
def add_artwork (catalog: dict, artwork_info: dict) -> None:
    """
        Esta función permite agregar una obra al catálogo, guardándolo en el arreglo 'obras'.

        Parámetros:
            -> catalog (dict): catálogo.
            -> artwork_info (dict): obra que se quiere adicionar. 

        No tiene retorno.

    """
    
    # Crear una obra con los datos ingresados por parámetro.
    artwork_new = new_artwork(artwork_info)

    # Agregar la obra a la última posición de la lista "obras".
    lt.addLast(catalog['artworks'], artwork_new)



# Función que agrega una pareja llave valor al map "BeginDate".
def add_BeginDate (catalog: dict, param_BeginDate: int, artist: dict) -> None:
    """
        Esta función permite agregar una pareja llave-valor al map "BeginDate" del catálogo.
        
        La llave deberá ser un año de nacimiento, es decir, un número entero positivo.
        El valor será una lista enlazada, cuyos elementos son diccionarios que
        representan a cada artista (para más detalle de qué información contienen estos
        diccionarios, revisar la documentación de la función new_artist()).

        En caso de que la pareja año-lista_artistas ya exista, se añadirá el artista a lista_artistas
        referente al año de nacimiento respectivo (la llave).
        En caso de que la pareja año-lista_artistas no exitsa, se creará la lista que contiene a los
        artistas que nacieron en la llave año, se añadirá la información del artista a dicha lista
        y se añadirá la nueva pareja año-lista_artistas al map "BeginDate" del catálogo.


        Parámetros:
            -> catalog (dict): catálogo.
            -> param_BeginDate (int): llave referente a un año de nacimiento.
            -> artist (dict): diccionario que representa al artista que se quiere añadir.

        No tiene retorno.

    """

    # Crear variable que guarda el mapa "BeginDate" del catálogo.
    map_BeginDate = catalog["BeginDate"]

    # Determinar si la pareja llave-valor ya existe.
    ya_existe = mp.contains(map_BeginDate, param_BeginDate)


    # Si ya existe la pareja llave-valor.
    if (ya_existe):

        # Crear variable que guarda la lista de los artistas que nacieron en param_BeginDate.
        list_BegDat_artists = mp.get(map_BeginDate, param_BeginDate)["value"]

        # Añade el artista a list_BegDet_artists.
        lt.addLast(list_BegDat_artists, artist)


    # Si no existe la pareja llave-valor.
    else:

        # Crear una nueva lista de los artistas que nacieron en param_BeginDate.
        new_list_BegDat_artists = lt.newList('SINGLE_LINKED')
        
        # Añade el artista a list_BegDet_artists.
        lt.addLast(new_list_BegDat_artists, artist)

        # Añade a pareja año-lista_artistas al map.
        mp.put(map_BeginDate, param_BeginDate, new_list_BegDat_artists)




#####-----#####-----#####-----#####-----#####   ###---####----###   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   CREACIÓN DE DATOS   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   ###---####----###   #####-----#####-----######-----####-----#####

"""
    Se define las funciones que permitirán crear elementos referentes a información
    de interés del catálogo (como los artistas, las obras, las técnicas, entre otros).

"""

# Función que crea un artista.
def new_artist (artist_info: dict) -> dict:
    """
        Esta función permite crear un artista. Estos se representarán mediante 
        el tipo de dato dict de Python.

        Parámetros:
            -> artist_info (dict): diccionario que tiene toda la información de interés del artista.

        Retorno:
            -> (dict): diccionario que representa al artista.

    """

    # Crear diccionario con la información de interés del artista.
    artist = {"ConstituentID": 0,
              "DisplayName": "",
              "Nationality": "",
              "Gender": "",
              "BeginDate": 0,
              "EndDate": 0}

    # Añadir datos.
    artist["ConstituentID"] = int(float(artist_info["ConstituentID"]))
    artist["DisplayName"] = artist_info["DisplayName"]
    artist["Nationality"] = artist_info["Nationality"]
    artist["Gender"] = artist_info["Gender"]
    artist["BeginDate"] = int(float(artist_info["BeginDate"]))
    artist["EndDate"] = int(float(artist_info["EndDate"]))

    # Retornar al artista.
    return artist



# Función que crea una nueva obra.
def new_artwork (artwork_info: dict) -> dict:
    """
        Esta función permite crear una obra. Estas se representarán mediante 
        el tipo de dato dict de Python.

        Parámetros:
            -> info_artwork (dict): diccionario que tiene toda la información de la obra que
                                 se encuentra en la base de datos.

        Retorno:
            -> (dict): diccionario que representa a la obra.

    """

    # Crear variable que guarda el diccionario con la información de interés de la obra.
    artwork = {"ObjectID": "",
               "Title": "",
               "ConstituentID": None,
               "Date": "",
               "Medium": "",
               "Classification": "",
               "DateAcquired": "",
               "Circumference (cm)": "",
               "Depth (cm)": "",
               "Diameter (cm)": "",
               "Height (cm)": "",
               "Length (cm)": "",
               "Weight (kg)": "",
               "Width (cm)": "",
               "Seat Height (cm)": ""}


    # Crear variable que guarda la lista de los id de los atistas que crearon la obra y asignarle la lista
    # que contiene dichos datos.
    list_artists_id = turn_into_list(artwork_info["ConstituentID"])


    # Iteración que añade la información de la obra.
    for property in artwork.keys():

        # Determinar si la propiedad actual es "ConstituentID".
        is_ConstituentID = (property == "ConstituentID")

        # Si la obra no tiene la propiedad actual.
        if (artwork_info[property] == ""):
            # Asignar el valor de la propiedad como "".
            artwork[property] = ""

        # De lo contrario
        else:            
            # Añadir propiedad.
            if not(is_ConstituentID):
                artwork[property] = artwork_info[property]
            else:
                artwork[property] = list_artists_id


    # Retornar obra.
    return artwork




#####-----#####-----#####-----#####-----#####   #####---####----#####   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   FUNCIONES ADICIONALES   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   #####---####----#####   #####-----#####-----#####-----#####-----#####

"""
    A continuación se definen funciones que serán necesarias para desarrollar los
    requerimientos, o que serán de utilidad en general.

"""

# Función que convierte el str de la lista de artistas en una lista.
def turn_into_list (list_in_str: str) -> list:
    """
        Esta función permite convertir la cadena de texto que guarda los id de los artistas que crearon
        una obra en una lista.

        Parámetros:
            -> list_in_str (str): cadena de texto con la lista de los id de los artistas.

        Retorno:
            -> (list): lista con los id de los artistas que crearon la obra.

    """

    # Crear sublista que contenga solo los id de los artistas mediante slicing y la función split().
    # Se hace parar borra los caracteres "[" y "]" que se encuentran al final de la cadena.
    artists_list = (list_in_str[1 : len(list_in_str) - 1]).split(",")

    # Retornar la lista.
    return artists_list