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

"""

# Función que crea el catálogo.
def new_Catalog () -> dict:
    """
        Esta función permite crear la estructura que guarda el catálogo del museo.
        
        Crea dos listas vacías que permitirán guardar los siguientes elementos:
         1- Los artistas.
         2- Las obras.

        Además, esta función crea un índice por técnica ("Mediums") de cada obra.


        No tiene parámetros.

        Retorno:
            -> (dict): el catálogo del museo.

    """

    # Definir variable que guarda la información del catálogo e inicializarla.
    catalog = {'artworks': None,
                'Mediums': None}


    #####-----#####-----#####-----#####   Definición Listas Elementos   #####-----#####-----#####-----#####

    """
        La siguiente lista contiene todas los obras encontradas en 
        los archivos de carga. Estas no estás ordenadas bajo ningún 
        criterio, y son referenciadas por los índices que se definirán
        en seguida.
    
    """
    catalog['artworks'] = lt.newList('SINGLE_LINKED')            # Pendiente añadir función de comparación.


    #####-----#####-----#####   Definición Índices   #####-----#####-----#####

    """
        A continuacion se crearán índices por diferentes criterios
        para llegar a la informacion requerida. Estos índices no
        replican informacion, solo referencian los libros de la lista
        creada anteriormente.
    
    """
    
    # Índice que crea un map cuya llave es la técnica las obras.
    catalog['Mediums'] = mp.newMap(4000,
                                  maptype='PROBING',
                                  loadfactor=0.5,
                                  comparefunction="") # Pendiente añadir función de comparación del map.


    #####-----#####-----#####-----#####   Retorno   #####-----#####-----#####-----#####

    return catalog


# Funciones para agregar informacion al catalogo





#####-----#####-----#####-----#####-----#####   ###---###----###   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   ADICIÓN DE DATOS   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   ###---###----###   #####-----#####-----######-----####-----#####

"""
    Se define las funciones que permitirán añadir elementos al catálogo.

"""

# Función que agrega una obra al catálogo.
def add_artwork (catalog: dict, artwork: dict) -> None:
    """
        Esta función permite agregar una obra al catálogo, guardándolo en el arreglo 'obras'.

        Parámetros:
            -> catalog (dict): catálogo.
            -> artwork (dict): obra que se quiere adicionar. 

        No tiene retorno.

    """
    
    # Crear una obra con los datos ingresados por parámetro.
    artwork_new = new_artwork(artwork)

    # Agregar la obra a la última posición de la lista "obras".
    lt.addLast(catalog['artworks'], artwork_new)



# Función que agrega una obra al índice de técnicas.
def add_medium (catalog: dict, artwork: dict) -> None:
    """
        Esta función permite agregar al índice "Mediums" del catálogo una pareja llave-valor 
        referente a una técnica y obra determinadas.

        Parámetros:
            -> catalog (dict): catálogo.
            -> artwork (dict): obra.

        No tiene retorno.

    """

    # Crear variable que guarda el map 'Mediums' del catálogo.
    mediums = catalog['Mediums']

    # Guardar técnica de la obra ingresada por parámetro.
    medium_artwork = artwork['Medium']
   
    # Si la obra tiene una técnica registrada.
    if (medium_artwork != ''):
        # Añadir obra.
        mp.put(mediums, medium_artwork, artwork) 





#####-----#####-----#####-----#####-----#####   ###---####----###   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   CREACIÓN DE DATOS   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   ###---####----###   #####-----#####-----######-----####-----#####

"""
    Se define las funciones que permitirán crear elementos referentes a información
    de interés del catálogo, como los artistas, las obras, las técnicas, entre otros.

"""

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
    list_artists_id = []
    list_artists_id = turn_into_list(artwork_info["ConstituentID"])


    # Iteración que añade la información de la obra.
    for property in artwork.keys():

        # Determinar si la propiedad actual es "ConstituentID".
        is_ConstituentID = (property == "ConstituentID")

        # Si la obra no tiene la propiedad actual.
        if (artwork[property] == ""):
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

    # Crear lsta vacía en la que se guardarán los id de los artistas.
    artists_list = []

    # Crear sublista que contenga solo los id de los artistas mediante slicing y la función split().
    # Se hace parar borra los caracteres "[" y "]" que se encuentran al final de la cadena.
    artists_list = (list_in_str[1 : len(list_in_str) - 1]).split(",")

    # Retornar la lista.
    return artists_list