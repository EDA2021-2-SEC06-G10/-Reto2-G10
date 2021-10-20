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

from math import pi
import config as cf
import datetime as date
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
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

        No tiene parámetros.

        Retorno:
            -> (dict): el catálogo del museo.

    """

    # Definir variable que guarda la información del catálogo e inicializar las parejas llave-valor.
    catalog = {'BeginDate': None,
               'Medium': None,
               'Nationality': None,
               'ConstituentID': None,
               'DateAcquired': None,
               'DisplayName': None,
               'Department': None}
    


    #####-----#####-----#####   Definición Maps/Índices   #####-----#####-----#####

    """
        A continuacion se crearán maps por diferentes criterios
        para llegar a la información requerida en tiempo constante.

        Es importante notar que todos los maps referencian a la misma información;
        es decir, si en un map se guarda la información de una obra y en otro también,
        ambos están referenciando al mismo espacio en memoria, mas no se está copiando
        dos veces la misma información. Esto se debe a la inmutabilidad del tipo de dato
        dict de Python.
    
    """

    # Map cuyas llaves son años de nacimiento y cuyas llaves son listas enlazadas que contienen
    # información relevante de los artistas que nacieron el año correspondiente.
    catalog["BeginDate"] = mp.newMap(10000, maptype='CHAINING', loadfactor = 4.0)   # Determinar tipo de mapa y tamaño adecuados.


    # Map cuyas llaves son las técnicas y cuyos valores son listas enlazadas que contienen
    # información relevante de las obras que fueron creadas usando dicha técnica.
    catalog["Medium"] = mp.newMap(146100, maptype='CHAINING', loadfactor=4.0)


    # Map cuyas llaves son las nacionalidades y cuyos valores son listas enlazadas que contienen
    # información relevante de las obras cuyo/s autor/es tiene/n dicha nacionalidad.
    catalog["Nationality"] = mp.newMap(200, maptype='PROBING', loadfactor=0.5)


    # Map cuyas llaves son ConstituentID's y cuyos valores son el artista reconocido con dicho ConstituentID.
    catalog["ConstituentID"] = mp.newMap(15224, maptype='CHAINING', loadfactor=4.0)


    # Map cuyas llaves son fechas de adquisición (DateAcquired) y cuyos valores son listas enlazadas que contienen
    # información relevante de las obras cuya fecha de adquisición es equivalente a la llave.
    catalog["DateAcquired"] = mp.newMap(146100, maptype='CHAINING', loadfactor=4.0)


    # Map cuyas llaves son nombres de artistas del catálogo (DisplayName) y cuyos valores son maps. En estos últimos,
    # las llaves son las técnicas que usó el artista para crear sus obras (Medium) y los valores son listas enlazadas
    # cuyos elementos son dichas obras.
    catalog["DisplayName"] = mp.newMap(15224, maptype='CHAINING', loadfactor=4.0)


    # Map cuyas llaves son nombres de departamentos del museo (Departments) y cuyos valores son listas enlazadas que contienen
    # información relevante de las obras que pertenecen a dicho departamento.
    catalog["Department"] = mp.newMap(500, maptype='PROBING', loadfactor=0.5)



    # Retorno.
    return catalog




#####-----#####-----#####-----#####-----#####   ###---###----###   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   ADICIÓN DE DATOS   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   ###---###----###   #####-----#####-----######-----####-----#####

"""
    Se definen las funciones que permitirán añadir elementos al catálogo.

"""

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



# Función que agrega una pareja llave-valor al map "DateAcquired".
def add_DateAcquired (catalog: dict, param_Date: str, artwork: dict) -> None:
    """
        Esta función permite agregar una pareja llave-valor al map "DateAcquired" del catálogo.
        
        La llave deberá ser una fecha de adquisición, es decir, una cadena de caracteres.
        El valor será una lista enlazada, cuyos elementos son diccionarios que
        representan a cada obra (para más detalle de la información contienen estos
        diccionarios, revisar la documentación de la función new_artwork()).

        En caso de que la pareja DateAcquired-lista_orbas ya exista, se añadirá la obra a lista_obras.
        En caso de que la pareja DateAcquired-lista_obras no exitsa, se creará la lista que contiene a las
        obras que se adquirieron en DateAcquired, se añadirá la información de la obra a dicha lista
        y se añadirá la nueva pareja DateAcquired-lista_obras al map "DateAcquired" del catálogo.


        Parámetros:
            -> catalog (dict): catálogo.
            -> param_Date (str): llave referente a una fecha de adquisición.
            -> artwork (dict): diccionario que representa a la obra que se quiere añadir.

        No tiene retorno.

    """

    # Crear variable que guarda el mapa "DateAcquired" del catálogo.
    map_DateAcquired = catalog["DateAcquired"]

    # Determinar si la pareja llave-valor ya existe.
    exists = mp.contains(map_DateAcquired, param_Date)


    # Si ya existe la pareja llave-valor.
    if (exists):

        # Crear variable que guarda la lista de las obras que fueron adquiridas en dicha fecha.
        list_DateAcquired_artworks = mp.get(map_DateAcquired, param_Date)["value"]

        # Añade la obra a list_DateAcquired_artworks.
        lt.addLast(list_DateAcquired_artworks, artwork)


    # Si no existe la pareja llave-valor.
    else:

        # Crear una nueva lista de las obras que fueron adquiridas en param_Date.
        new_list_DateAcquired_artists = lt.newList('SINGLE_LINKED')
        
        # Añade la obra a new_list_DateAcquired_artists.
        lt.addLast(new_list_DateAcquired_artists, artwork)

        # Añade la pareja DateAcquired-lista_obras al map.
        mp.put(map_DateAcquired, param_Date, new_list_DateAcquired_artists)



# Función que agrega una pareja llave-valor al map "DisplayName".
def add_DisplayName (catalog: dict, param_DisNam: str) -> None:
    """
        Esta función permite agregar una pareja llave-valor al map "DisplayName" del catálogo.
        
        La llave deberá ser un DisplayName, es decir, una cadena de caracteres.
        El valor será un map que contendrá parejas Medium-lista_obras.


        Parámetros:
            -> catalog (dict): catálogo.
            -> param_DisNam (str): llave referente a un ConstituentID.

        No tiene retorno.

    """

    # Crear variable que guarda el mapa "DisplayName" del catálogo.
    map_DisplayName = catalog["DisplayName"]

    # Crear variable que guardará el mapa que contendrá parejas Medium-lista_obras del autor
    # con nombre param_DisNam.
    new_Medium_map = mp.newMap(maptype = 'PROBING')

    # Añadir la pareja DisplayName-Medium_map al mapa 'DisplayName'.
    mp.put(map_DisplayName, param_DisNam, new_Medium_map)



# Función que agrega una pareja llave-valor a los mapas Medium-artwork_list, los cuales son los
# valores del mapa 'DisplayName' del catálogo.
def add_pair_Medium_artworkList (Medium_map: dict, param_Medium: str, artwork: dict) -> None:
    """
        Esta función permite agregar una pareja llave-valor al map "Medium_map".
        Cada "Medium_map" es un valor del map 'DisplayName' del catálogo. Estos almacenan
        parejas Medium-lista_obras; las llaves son todas las técnicas que ha usado un artista
        para la creación de sus obras, y los valores son listas cuyos elementos son las obras
        que fueron creadas usando dicha técnica.
        
        La llave de "Medium_map" deberá ser una técnica/medio, es decir, una cadena de caracteres.
        El valor será una lista enlazada, cuyos elementos son diccionarios que
        representan a cada obra creada con dicha técnica (para más detalle de la información contienen estos
        diccionarios, revisar la documentación de la función new_artwork()).

        En caso de que la pareja Medium-lista_obras ya exista, se añadirá la obra a lista_obras.
        En caso de que la pareja Medium-lista_obras no exitsa, se creará la lista que contiene a las
        obras que fueron creadas con esa técnica, se añadirá la información de la obra a dicha lista
        y se añadirá la nueva pareja Medium-lista_obras al map "Medium_map".


        Parámetros:
            -> Medium_map (dict): mapa que tiene parejas Medium-lista_obras.
            -> param_Medium (str): llave referente a una técnica.
            -> artwork (dict): diccionario que representa a la obra que se quiere añadir.

        No tiene retorno.

    """

    # Determinar si la pareja llave-valor ya existe.
    exists = mp.contains(Medium_map, param_Medium)


    # Si ya existe la pareja llave-valor en Medium_map.
    if (exists):

        # Crear variable que guarda la lista de las obras que fueron creadas con param_Medium.
        list_Medium_artworks = mp.get(Medium_map, param_Medium)["value"]

        # Añade la obra a list_DateAcquired_artworks.
        lt.addLast(list_Medium_artworks, artwork)


    # Si no existe la pareja llave-valor.
    else:

        # Crear una nueva lista de las obras que fueron creadas con param_Medium.
        new_list_Medium_artists = lt.newList('SINGLE_LINKED')
        
        # Añade la obra a new_list_Medium_artists.
        lt.addLast(new_list_Medium_artists, artwork)

        # Añade la pareja DateAcquired-lista_obras al map.
        mp.put(Medium_map, param_Medium, new_list_Medium_artists)



# Función que agrega una pareja llave-valor al map "Department".
def add_Department (catalog: dict, param_Department: str, artwork: dict) -> None:
    """
        Esta función permite agregar una pareja llave-valor al map "Department" del catálogo.
        
        La llave deberá ser un departamento del catálogo, es decir, una cadena de caracteres.
        El valor deberá ser una lista enlazada, cuyos elementos son diccionarios que
        representan a cada obra (para más detalle de qué información contienen estos
        diccionarios, revisar la documentación de la función new_artwork()).

        En caso de que la pareja Department-lista_obras ya exista, se añadirá la obra a lista_obras
        referente al departemento respectivo (la llave).
        En caso de que la pareja Department-lista_obras no exista, se creará la lista que contiene a las
        obras que pertenecen a dicho depto., se añadirá la información de la obra a dicha lista
        y se añadirá la nueva pareja Department-lista_obras al map "Department" del catálogo.


        Parámetros:
            -> catalog (dict): catálogo.
            -> param_Department (str): cadena referente a un departamento del catálogo.
            -> artwork (dict): diccionario que representa la obra que se quiere añadir.

        No tiene retorno.

    """
    
    # Crear variable que guarda el mapa "Department" del catálogo.
    # Crear variable que determina si la pareja llave-valor ya existe.
    map_Department = catalog["Department"]
    exists = mp.contains(map_Department, param_Department)


    # Si ya existe la pareja llave-valor.
    if (exists):

        # Crear variable que guarda la lista de las obras que pertenecen al dpto.
        list_Department_artworks = mp.get(map_Department, param_Department)["value"]

        # Añade la obra a list_Department_artworks.
        lt.addLast(list_Department_artworks, artwork)


    # Si no existe la pareja llave-valor.
    else:

        # Crear una nueva lista de las obras que pertenecen al dpto.
        new_list_Department_artworks = lt.newList('SINGLE_LINKED')
        
        # Añade la obra a new_list_Department_artworks.
        lt.addLast(new_list_Department_artworks, artwork)

        # Añade la pareja Department-lista_obras al map.
        mp.put(map_Department, param_Department, new_list_Department_artworks)
    






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

    # Actualizar datos desconocidos.
    if artist["DisplayName"] == "":
        artist["DisplayName"] = "N.A."
    if artist["BeginDate"] == 0:
        artist["BeginDate"] = "N.A."
    if artist["EndDate"] == 0:
        artist["EndDate"] = "N.A."
    if artist["Nationality"] == "":
        artist["Nationality"] = "N.A."
    if artist["Gender"] == "":
        artist["Gender"] = "N.A."

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
               "Dimensions": "",
               "CreditLine": "",
               "Classification": "",
               "Department": "",
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

        # De lo contrario.
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



# Función para comparar dos obras según su fecha de adquisición.
def cmp_by_DateAcquired (artwork_1: dict, artwork_2: dict) -> bool:
    """
        Esta función determina si la fecha de adquisición de artwork_1 es menor que
        la de artwork_2.

        Parámetros:
            -> artwork_1: información de la primera obra.
            -> artwork_2: información de la segunda obra.
        
        Retorno:
            -> (bool): True si la fecha de adquisición de obra_1 es menor que la de obra_2.
                       False de lo contrario.
    
    """

    # Crear variable de retorno.
    less_than = False

    # Crear variables que guardan las fechas.
    DateAcquired_1 = artwork_1["DateAcquired"]
    DateAcquired_2 = artwork_2["DateAcquired"]

    # Si las obras no tienen fecha de adquisición.
    if DateAcquired_1 == "":
        DateAcquired_1 = "0001-01-01"
    if DateAcquired_2 == "":
        DateAcquired_1 = "0001-01-01"

    # Crear variables con las fechas de adquisición modificadas.
    mod_DateAcquired_1 = date.datetime.strptime(DateAcquired_1, '%Y-%m-%d')
    mod_DateAcquired_2 = date.datetime.strptime(DateAcquired_2, '%Y-%m-%d')

    # Determinar si es menor.
    if mod_DateAcquired_1 < mod_DateAcquired_2:
        less_than = True
    
    # Retornar respuesta.
    return (less_than)



# Función que compara dos técnicas según la cantidad de veces que se usaron.
def cmp_Mediums (medium_1: tuple, medium_2: tuple) -> bool:
    """
        Esta función permite determinar si la cantidad de veces que se usó medium_1 es mayor que
        la cantidad de veces que se usó medium_2.

        Los parámetros son tuplas cuyo primer elemento es la cadena referente a la técnica y cuyo
        segundo elemento es la cantidad de veces que esta se usó.

        Parámetros:
            -> medium_1 (tuple): tupla de la primera técnica.
            -> medium_2 (tuple): tupla de la segunda técnica.

        Retorno:
            -> (bool): True en caso de que la cantidad de veces que se usó medium_1 es 
                       mayor que la cantidad de veces que se usó medium_2.
                       False de lo contrario. 

    """

    # Determinar si es mayor o no y retornar respuesta.
    answer = (medium_1[1] > medium_2[1])
    return answer



# Función que compara dos obras según sus fechas.
def cmp_artworks_by_Date (artwork_1: dict, artwork_2: dict) -> bool:
    """
        Esta función permite determinar si la fecha de artwork_1 es menor que la fecha de artwork_2.

        Parámetros:
            -> artwork_1: información de la primera obra.
            -> artwork_2: información de la segunda obra.

        Retorno:
            -> (bool): True en caso de que la fecha de artwork_1 sea menor que la fecha de artwork_2.
                       False de lo contrario. 

    """

    # Determinar si es menor o no y retornar respuesta.
    answer = (artwork_1['Date'] < artwork_2['Date'])
    return answer



# Función que compara dos obras según sus fechas.
def cmp_artworks_by_Price (artwork_1: dict, artwork_2: dict) -> bool:
    """
        Esta función permite determinar si la fecha de artwork_1 es menor que la fecha de artwork_2.

        Parámetros:
            -> artwork_1: información de la primera obra.
            -> artwork_2: información de la segunda obra.

        Retorno:
            -> (bool): True en caso de que la fecha de artwork_1 sea menor que la fecha de artwork_2.
                       False de lo contrario. 

    """

    # Determinar si es menor o no y retornar respuesta.
    answer = (artwork_1['Price (USD)'] < artwork_2['Price (USD)'])
    return answer




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
        Esta función retorna una listas cronológicamente ordenada que contiene auqellos artistas
        que nacieron dentro de un rango de años indicado por el usuario.


        Parámetros:
            -> catalog (dict): catálogo.
            -> first_year (int): año inicial.
            -> last_year (int): año final.

        Retorno:
            -> (dict): diccionario que representa la lista que contiene la respuesta.

    """

    # Crear rango que representa un intervalo cerrado que empieza en first_year
    # y termina en last_year.
    interval = range(first_year, last_year + 1)

    # Crear lista que contendrá a los artistas que nacieron dentro de interval.
    # Guardar el map "BeginDate" del catálogo.
    return_list = lt.newList("ARRAY_LIST")
    map_BeginDate = catalog["BeginDate"]


    # Iterar sobre cada año que se encuentra dentro de interval.
    for year in interval:
        
        # Si el año se encuentra en el mapa map_BeginDate.
        if (mp.get(map_BeginDate, year) != None):

            # Guardar la lista de los artistas que nacieron durante year.
            artists_list = mp.get(map_BeginDate, year)["value"]

            # Añadir cada artista a return_list.
            for artist in (lt.iterator(artists_list)):
                lt.addLast(return_list, artist)


    # Ordenar lista cronológicamente según los BeginDates y retornarla.
    ordered_list = qui.sort(return_list, cmp_BeginDates)
    return ordered_list



# Función del requerimiento 2.
def req_2 (catalog: dict, first_date: str, last_date: str) -> tuple:
    """
        Dado un rango de fechas, esta función retorna una tupla que contiene lista cronológicamente ordenada 
        que almacena las obras que fueron compradas por el museo durante dicho rango de tiempo y la cantidad 
        de obras que fueron adquiridas por compra.

        Parámetros:
            -> catalog (dict): catálogo.
            -> first_date (str): fecha inicial.
            -> last_date (str): fecha final.

        Retorno:
            -> (tuple): tupla cuyo primer elemento es la lista que contiene la respuesta
                        y cuyo segundo elemento representa la cantidad de obras que fueron
                        adquiridas por compra.

    """

    # Crear lista y entero de retorno.
    ordered_list = lt.newList("SINGLE_LINKED")
    num_purch = 0

    # Crear variable que guarda el mapa 'DateAcquired' del catálogo.
    map_DateAcquired = catalog['DateAcquired']

    # Crear variables con las fechas de adquisición modificadas.
    mod_first_date = date.datetime.strptime(first_date, '%Y-%m-%d')
    mod_last_date = date.datetime.strptime(last_date, '%Y-%m-%d')

    # Crear lista que contiene las llaves de map_DateAcquired.
    keys_map_DateAcquired = lt.iterator(mp.keySet(map_DateAcquired))


    # Iterar sobre todas las llaves de keys_map_DateAcquired.
    for DateAcquired in keys_map_DateAcquired:

        # Crear variables con el DateAcquired de la iteración actual modificada.
        mod_DateAcquired = date.datetime.strptime(DateAcquired, '%Y-%m-%d')

        # Crear variable que determina si mod_DateAcquired se encuentra dentro del rango.
        in_range = (mod_DateAcquired >= mod_first_date and mod_DateAcquired <= mod_last_date)


        # Si está en el rango.
        if (in_range):

            # Crear variable que guarda la lista de obras (el valor) de la llave DateAcquired.
            list_DateAcquired = lt.iterator(mp.get(map_DateAcquired, DateAcquired)['value'])

            # Iterar sobre las obras de list_DateAcquired.
            for artwork in list_DateAcquired:
                
                # Añadir la obra a la lista de retorno.
                lt.addLast(ordered_list, artwork)

                # Guardar línea de crédito de la obra, determinar si es igual a 'Purchase' y, si lo es,
                # aumentar num_purch en 1.
                artwork_CreditLine = artwork['CreditLine'].lower()
                is_purchase = (artwork_CreditLine == 'purchase' or artwork_CreditLine == 'purchased')
                if (is_purchase):
                    num_purch += 1

    # Ordenar lista.
    ordered_ordered_list = qui.sort(ordered_list, cmp_by_DateAcquired)
        
    # Retornar tupla.
    return (ordered_ordered_list, num_purch)



# Función del requerimiento 3.
def req_3 (catalog: dict, param_DisplayName: str) -> tuple:
    """
        Dado el nombre de un/una artista, esta función retorna 

        Parámetros:
            -> catalog (dict): catálogo.
            -> param_DisplayName (str): nombre del artista.

        Retorno:
            -> (tuple): tupla cuyo primer elemento es la lista que contiene la respuesta
                        y cuyo segundo elemento representa la cantidad de obras que fueron
                        adquiridas por compra.

    """

    # Guardar el mapa de las técnicas del artista con nombre param_DisplayName.
    Mediums_map = mp.get(catalog['DisplayName'], param_DisplayName)['value']

    # Crear variables de retorno.
    total_artworks = 0
    total_mediums = mp.size(Mediums_map)
    most_used_medium = ''
    list_most_used_medium = None
    list_medium_sizes = lt.newList('SINGLE_LINKED')


    # Recorrer todas las técnicas de Mediums_map.
    for medium in lt.iterator(mp.keySet(Mediums_map)):
        
        # Guardar tamaño de lista que contiene las obras que fueron creadas usando la técnica medium.
        # y aumentar valor total_artworks.
        size_artwork_list = lt.size(mp.get(Mediums_map, medium)['value'])
        total_artworks += size_artwork_list

        # Añadir tupla (medium, size_artwork_list) a list_medium_sizes.
        lt.addLast(list_medium_sizes, (medium, size_artwork_list))

    # Organizar list_medium_sizes.
    ordered_list_medium_sizes = qui.sort(list_medium_sizes, cmp_Mediums)

    # Guardar técnica más usada.
    most_used_medium = lt.getElement(ordered_list_medium_sizes, 1)[0]
        
    # Guardar en list_most_used_medium la lista de las obras que fueron creadas con most_used_medium.
    # Crear varable que guarda dicha lista ordenada.
    list_most_used_medium = mp.get(Mediums_map, most_used_medium)['value']
    ordered_list_most_used_medium = qui.sort(list_most_used_medium, cmp_artworks_by_Date)
    
    

    # Armar tupla de retorno y retornarla.
    answer = (total_artworks, total_mediums, most_used_medium, ordered_list_most_used_medium, ordered_list_medium_sizes)
    return answer        



# Función del requerimiento 5.
def req_5 (catalog: dict, param_Dep: str) -> tuple:
    """
        Dado el nombre de un/una artista, esta función retorna 

        Parámetros:
            -> catalog (dict): catálogo.
            -> param_DisplayName (str): nombre del artista.

        Retorno:
            -> (tuple): tupla cuyo primer elemento es la lista que contiene la respuesta
                        y cuyo segundo elemento representa la cantidad de obras que fueron
                        adquiridas por compra.

    """

    # Guardar mapa 'Department'.
    map_Dep = catalog['Department']

    # Guardar lista obras.
    artwork_list = mp.get(map_Dep, param_Dep)['value']

    # Crear variable precio total.
    total_price = 0.0
    total_weight = 0.0

    new_art_lt = lt.newList()

    # Recorrer artwork_list.
    for artwork in lt.iterator(artwork_list):

        # Calcular precio.
        price = calc_price(artwork)
        total_price += price

        # Peso.
        weight = artwork['Weight (kg)']
        total_weight += weight

        # Añadir a new_art_lt si tiene fecha.
        if (artwork['Date'] != ''):
            lt.addLast(new_art_lt,artwork)

        # Añadir a new_art_lt si tiene peso.
        if (artwork['Date'] != ''):
            lt.addLast(new_art_lt,artwork)

    



    order_artw_lt = qui.sort(new_art_lt, cmp_artworks_by_Date)

    order_artwork_list_price = qui.sort(artwork_list, cmp_artworks_by_Price) 

    return(total_price, total_weight, order_artw_lt, order_artwork_list_price)



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



# Función que calcula el precio de transporte de una obra.
def calc_price (artwork: dict) -> float:
    """
        Dada la información de una obra, esta función permite calcular su precio de transporte
        asociado. Además, permite añadir a dicha un atributo nuevo llamado trans_price, el cual
        debe ser de tipo float.

        Parámetros:
            -> artwork (dict): diccionario que contiene la información de la obra.

        Retorno:
            -> (float): precio de transporte de la obra.

    """

    price = 0.0                     # Variable de precio total.
    UNIT_COST = 72                  # Precio unitario por kg.
    VOL_UNIT_COST = 72/1000000      # Precio unitario por m^3.
    AREA_UNIT_COST = 72 /10000      # Precio unitario por m^2.
    radius = 0.0                    # Variable radio.

    # Crear variables que guardan las dimensiones de la obra.
    depth = artwork['Depth (cm)']
    diam = artwork['Diameter (cm)']
    height = artwork['Height (cm)']
    lenght = artwork['Length (cm)']
    weight = artwork['Weight (kg)']
    width = artwork['Width (cm)']
    

    # Variable que cuenta la cantidad de dimensiones que tiene la obra diferentes al diámetro.
    num_dim = 0


    # Condicionales para modificar dimensiones.

    if (depth != ""):
        if (depth != '0'):
            depth = float(depth)
            num_dim += 1
        else:
            depth = 1

    else:
        depth = 1

    if (height != ""):
        if (height != '0'):
            height = float(height)
            num_dim += 1
        else:
            height = 1

    else:
        height = 1

    if (lenght != ""):
        if (lenght != '0'):
            lenght = float(lenght)
            num_dim += 1
        else:
            lenght = 1
    else:
        lenght = 1

    if (width != ""):
        if (width != '0'):
            width = float(width)
            num_dim += 1
        else:
            width = 1
    else:
        width = 1



    #####-----#####-----#####   Cálculos   #####-----#####-----#####

    # Caso -1: no tiene dimensiones.
    if (num_dim == 0 and weight != "" and diam != ""):
        price = 0.0

    else:
        # Caso 0: la figura tiene peso.
        if (weight != ""):
            price = UNIT_COST * float(weight)

        else:
            
            weight = 0.0        # Atualizar valor peso.

            # Si la figura tiene diámetro.
            if (diam != ""):
                
                # Calcular radio.
                radius = float(diam)/2

                # Caso 1: si tiene radio y solo una dimensión más, entonces es cilindro.
                if (num_dim == 1):
                    price = (VOL_UNIT_COST) * (pi * (depth*height*lenght*width) * radius**2)
                    weight = (pi * (depth*height*lenght*width) * radius**2)/100

                # Caso 2: si tiene radio y dos dimensiones o más, entonces es esfera.
                if (num_dim == 2):
                    price = (VOL_UNIT_COST) * (4/3 * pi * radius**3)
                    weight = (4/3 * pi * radius**3)/100

                # Caso 3: si tiene radio y nada más, entonces es círculo.
                if (num_dim == 0):
                    price = (AREA_UNIT_COST) * (pi * radius**2)


            # Si la figura no tiene diámetro.
            else:
                
                # Caso 4: tiene dos dimensiones, entonces es rectángulo.
                if (num_dim == 2):
                    price = (AREA_UNIT_COST) * (depth*height*lenght*width)

                # Caso 5: tiene tres dimensiones, entonces es cubo o figura tridimensional con diferentes medidas.
                if (num_dim == 3):
                    price = (VOL_UNIT_COST) * (depth*height*lenght*width)
                    weight = (depth*height*lenght*width)/100
    

    # Actualizar peso.
    artwork['Weight (kg)'] = weight

    # Retornar precio.
    artwork['Price (USD)'] = price
    return price