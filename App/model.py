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
from DISClib.DataStructures import probehashtable
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import quicksort as qui
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
               'BeginDate': None,
               'Medium': None,
               'Nationality': None,
               'ConstituentID': None}


    #####-----#####-----#####-----#####   Definición Listas de Elementos   #####-----#####-----#####-----#####
    """
        La siguiente lista contiene la información de todos los artistas encontrados en  los archivos de carga.
        Estos no están ordenadas bajo ningún criterio, y son referenciados por los índices que se definirán en 
        seguida.

        Cada artista se representa mediante un diccionario, cuyas parejas llave-valor representan información
        relevante de cada artista (como su nombre, id, fecha de nacimiento, entre otros). Toda la información
        que se guarda de cada artista se especfica detalladamente en la función new_artist(). 
    
    """
    catalog['artists'] = lt.newList('SINGLE_LINKED', cmpfunction = cmp_BeginDates)
    
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
        para llegar a la información requerida en tiempo constante.
    
    """

    # Map cuyas llaves son años de nacimiento y cuyas llaves son listas enlazadas que contienen
    # información relevante de los artistas que nacieron el año correspondiente.
    catalog["BeginDate"] = mp.newMap(10000, maptype='CHAINING', loadfactor = 4.0)   # Determinar tipo de mapa y tamaño adecuados.


    # Map cuyas llaves son las técnicas y cuyos valores son listas enlazadas que contienen
    # información relevante de las obras que fueron creadas usando dicha técnica.
    # El tamaño del mapa se asignó como el siguiente primo a 146.100, ya que esta es la cantidad de obras que hay.
    catalog["Medium"] = mp.newMap(probehashtable.nextPrime(146100/0.8), maptype='PROBING', loadfactor=0.8)


    # Map cuyas llaves son las nacionalidades y cuyos valores son listas enlazadas que contienen
    # información relevante de las obras cuyo/s autor/es tiene/n dicha nacionalidad.
    # El tamaño del mapa se asignó como el siguiente primo a 200, porque hay 194 países reconocidos
    # por la ONU y se añadieron 6 espacios extra para evitar re-hashing (en la medida de lo posible).
    catalog["Nationality"] = mp.newMap(probehashtable.nextPrime(200/0.8), maptype='PROBING', loadfactor=0.8)


    # Map cuyas llaves son ConstituentID's y cuyos valores son el artista reconocido con dicho ConstituentID.
    # El tamaño del mapa se asignó como el siguiente primo a 15.224 porque hay 15.224 artistas en el catálogo.
    catalog["ConstituentID"] = mp.newMap(probehashtable.nextPrime(15224), maptype='CHAINING', loadfactor=4.0)



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



# Función que agrega una pareja llave-valor al map "BeginDate".
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
    exists = mp.contains(map_BeginDate, param_BeginDate)


    # Si ya existe la pareja llave-valor.
    if (exists):

        # Crear variable que guarda la lista de los artistas que nacieron en param_BeginDate.
        list_BegDat_artists = mp.get(map_BeginDate, param_BeginDate)["value"]

        # Añade el artista a list_BegDet_artists.
        lt.addLast(list_BegDat_artists, artist)


    # Si no existe la pareja llave-valor.
    else:

        # Crear una nueva lista de los artistas que nacieron en param_BeginDate.
        new_list_BegDat_artists = lt.newList('SINGLE_LINKED')
        
        # Añade el artista a new_list_BegDat_artists.
        lt.addLast(new_list_BegDat_artists, artist)

        # Añade la pareja año-lista_artistas al map.
        mp.put(map_BeginDate, param_BeginDate, new_list_BegDat_artists)



# Función que agrega una pareja llave-valor al map "Medium".
def add_Medium (catalog: dict, param_Medium: str, artwork: dict) -> None:
    """
        Esta función permite agregar una pareja llave-valor al map "Medium" del catálogo.
        
        La llave deberá ser una técnica/medio, es decir, una cadena de caracteres.
        El valor será una lista enlazada, cuyos elementos son diccionarios que
        representan a cada obra (para más detalle de la información contienen estos
        diccionarios, revisar la documentación de la función new_artwork()).

        En caso de que la pareja técnica-lista_orbas ya exista, se añadirá la obra a lista_obras.
        En caso de que la pareja técnica-lista_obras no exitsa, se creará la lista que contiene a las
        obras que fueron creadas con esa técnica, se añadirá la información de la obra a dicha lista
        y se añadirá la nueva pareja técnica-lista_obras al map "Medium" del catálogo.


        Parámetros:
            -> catalog (dict): catálogo.
            -> param_Medium (str): llave referente a una técnica.
            -> artwork (dict): diccionario que representa a la obra que se quiere añadir.

        No tiene retorno.

    """

    # Crear variable que guarda el mapa "Medium" del catálogo.
    map_Medium = catalog["Medium"]

    # Determinar si la pareja llave-valor ya existe.
    exists = mp.contains(map_Medium, param_Medium)


    # Si ya existe la pareja llave-valor.
    if (exists):

        # Crear variable que guarda la lista de las obras quese crearon con dicha técnica.
        list_Medium_artworks = mp.get(map_Medium, param_Medium)["value"]

        # Añade la obra a list_Medium_artworks.
        lt.addLast(list_Medium_artworks, artwork)


    # Si no existe la pareja llave-valor.
    else:

        # Crear una nueva lista de las obras creados con param_Medium.
        new_list_Medium_artists = lt.newList('SINGLE_LINKED')
        
        # Añade la obra a new_list_Medium_artists.
        lt.addLast(new_list_Medium_artists, artwork)

        # Añade la pareja técnica-lista_obras al map.
        mp.put(map_Medium, param_Medium, new_list_Medium_artists)



# Función que agrega una pareja llave-valor al map "Nationality".
def add_Nationality (catalog: dict, param_Nacion: str, artwork: dict) -> None:
    """
        Esta función permite agregar una pareja llave-valor al map "Nationality" del catálogo.
        
        La llave deberá ser una nacionalidad, es decir, una cadena de caracteres.
        El valor será una lista enlazada, cuyos elementos son diccionarios que
        representan a cada obra (para más detalle de la información contienen estos
        diccionarios, revisar la documentación de la función new_artwork()).

        En caso de que la pareja nacionalidad-lista_obras ya exista, se añadirá la obra a lista_obras.
        En caso de que la pareja nacionalidad-lista_obras no exitsa, se creará la lista que contiene a las
        obras con dicha nacionalidad, se añadirá la información de la obra a dicha lista
        y se añadirá la nueva pareja nacionalidad-lista_obras al map "Nationality" del catálogo.


        Parámetros:
            -> catalog (dict): catálogo.
            -> param_Nacion (str): llave referente a una nacionalidad.
            -> artwork (dict): diccionario que representa al artista que se quiere añadir.

        No tiene retorno.

    """

    # Crear variable que guarda el mapa "Nationality" del catálogo.
    map_Nationality = catalog["Nationality"]

    # Determinar si la pareja llave-valor ya existe.
    exists = mp.contains(map_Nationality, param_Nacion)


    # Si ya existe la pareja llave-valor.
    if (exists):

        # Crear variable que guarda la lista de las obras cuya nacionalidad es param_Nacion.
        list_Nationality_artworks = mp.get(map_Nationality, param_Nacion)["value"]

        # Añade la obra a list_Nationality_artworks.
        lt.addLast(list_Nationality_artworks, artwork)


    # Si no existe la pareja llave-valor.
    else:

        # Crear una nueva lista de las obras cuya nacionalidad es param_Nacion.
        new_list_Nationality_artworks = lt.newList('SINGLE_LINKED')
        
        # Añade la obra a new_list_Nationality_artworks.
        lt.addLast(new_list_Nationality_artworks, artwork)

        # Añade la pareja nacionalidad-lista_obras al map.
        mp.put(map_Nationality, param_Nacion, new_list_Nationality_artworks)



# Función que agrega una pareja llave-valor al map "ConstituentID".
def add_ConstituentID (catalog: dict, param_ConsID: int, artist: dict) -> None:
    """
        Esta función permite agregar una pareja llave-valor al map "add_ConstituentID" del catálogo.
        
        La llave deberá ser un ConstituentID, es decir, un número entero mayor que 0.
        El valor será la información del artista cuyo ConstituentID es igual a la llave.


        Parámetros:
            -> catalog (dict): catálogo.
            -> param_ConsID (int): llave referente a un ConstituentID.
            -> artist (dict): diccionario que representa al artista que se quiere añadir.

        No tiene retorno.

    """

    # Crear variable que guarda el mapa "ConstituentID" del catálogo.
    map_ConstituentID = catalog["ConstituentID"]

    # Añadir la pareja ConstituentID-artista al map.
    mp.put(map_ConstituentID, param_ConsID, artist)




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
               "Medium": """""",
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





#####-----#####-----#####-----#####-----#####   #####---#######----#####   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   FUNCIONES DE COMPARACIÓN   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   #####---#######----#####   #####-----#####-----#####-----#####-----#####

"""
    A continuación se definen las funciones que permitirán comparar
    y ordenar los elementos del catálogo (incluyendo las llaves de los maps).

"""

# Función que compara dos artistas según su año de nacimiento.
def cmp_BeginDates (artists_1: dict, artists_2: dict) -> bool:
    """
        Esta función permite determinar si el año de nacimiento del primer artista (artists_1)
        es menor que el año de nacimiento del segundo artista (artists_2).

        Parámetros:
            -> artists_1 (dict): diccionario que contiene la información del primer artista.
            -> artists_2 (dict): diccionario que contiene la información del segundo artista.

        Retorno:
            -> (bool): True en caso de que el año de nacimiento del primer artista sea menor
                       que el año de nacimiento del segundo artista.
                       False de lo contrario. 

    """

    # Guardar los años de nacimiento de los artistas.
    birth_year_1 = artists_1["BeginDate"]
    birth_year_2 = artists_2["BeginDate"]

    # Crear variable que indica si birth_year_1 es menor que birth_year_2 y retornarla.
    return_variable = (birth_year_1 < birth_year_2)
    return return_variable




#####-----#####-----#####-----#####-----#####   #####---#######----#####   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   FUNCIONES REQUERIMIENTOS   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   #####---#######----#####   #####-----#####-----#####-----#####-----#####

"""
    A continuación se definen las funciones referentes a la implementación de
    los requerimientos.

"""

# Función del requerimiento 1.
def req_1 (catalog: dict, first_year: int, last_year: int) -> dict:
    """
        Esta función permite convertir la cadena de texto que guarda los id de los artistas que crearon
        una obra en una lista.

        Parámetros:
            -> catalog (dict): catálogo.
            -> first_year (int): año inicial.
            -> last_year (int): año final.

        Retorno:
            -> (dict): diccionarios que representa la lista que contiene la respuesta.

    """

    # Crear rango que representa un intervalo cerrado que empieza en first_year
    # y termina en last_year.
    interval = range(first_year, last_year + 1)

    # Crear lista que contendrá a los artistas que nacieron dentro de interval.
    return_list = lt.newList("ARRAY_LIST")

    # Guardar el map "BeginDate" del catálogo.
    map_BeginDate = catalog["BeginDate"]


    # Iterar sobre cada año que se encuentra dentro de interval.
    for year in interval:
        
        # Guardar la lista de los artistas que nacieron durante year.
        artists_list = mp.get(map_BeginDate, year)["value"]

        # Crear lista con los elementos de artists_list.
        iter_artists_list = lt.iterator(artists_list)

        # Añadir cada artista a return_list.
        for artist in iter_artists_list:
            lt.addLast(return_list, artist)


    # Ordenar lista cronológicamente (es decir, según los BeginDates).
    ordered_list = qui.sort(return_list, cmp_BeginDates)

    # Retornar la lista ordenada.
    return ordered_list

    



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