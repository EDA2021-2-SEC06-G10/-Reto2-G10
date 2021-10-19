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
    for artist in input_file:
        
        # Crear un artista con la información de la iteración actual.
        artist_info = model.new_artist(artist)


        # Determinar su año de nacimiento.
        artists_BegDat = artist_info["BeginDate"]

        # Añadirlo al map "BeginDate" si su año de nacimiento está registrado.
        if not (artists_BegDat == 0):
            model.add_BeginDate(catalog, artists_BegDat, artist_info)


        # Determinar su ConstituentID.
        artist_ConsID = artist_info["ConstituentID"]

        # Añadirlo al map "ConstituentID" si su ConstituentID es diferente de "".
        if not (artist_ConsID == ""):

            # Añadir la pareja al map 'ConstituentID'.
            model.add_ConstituentID(catalog, artist_ConsID, artist_info)



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
    for artwork in input_file:

        # Crear una obra con la información de la iteración actual.
        artwork_info = model.new_artwork(artwork)

        # Crear variables que guardan el Medium, los ConstituentID y el DateAcquired de artwork.
        artwork_Medium = artwork_info["Medium"]
        ConstituentID_list = artwork_info["ConstituentID"]
        artwork_DateAcquired = artwork_info["DateAcquired"]

        # Crear variabes que guardan los maps ConstituentID y DisplayName del catálogo.
        map_ConstituentID = catalog["ConstituentID"]
        map_DisplayName = catalog['DisplayName']



        #####-----#####-----#####-----#####   Bloque Map 'Medium'   #####-----#####-----#####-----#####

        # Añadir la pareja llave-valor al map 'Medium' si su técnica está registrada.
        if not (artwork_Medium == ""):
            model.add_Medium(catalog, artwork_Medium, artwork_info)
        
        

        #####-----#####-----#####-----#####   Bloque Maps 'Nationality' y 'DisplayName'   #####-----#####-----#####-----#####

        # Crear variable que guardará la llave referente a la nacionalidad de la obra.
        new_Nacion_key = ""


        # Recorrer la lista que contiene los ConstituentID de la obra.
        for ConstituentID in ConstituentID_list:
            
            # Si el ConstituentID actual no es una cadena vacía.
            if not (ConstituentID == ""):

                # Convertir el ConstituentID a un entero.
                ConstituentID_key = int(float(ConstituentID))
                
                # Determinar si la llave ConstituentID_key está en el mapa 'ConstituentID_key'.
                exists = mp.contains(map_ConstituentID, ConstituentID_key)


                # Si la llave existe.
                if (exists):
                    
                    #####-----#####-----#####-----#####   Bloque Map 'Nationality'   #####-----#####-----#####-----#####

                    # Crear variable que guarda la nacionalidad del artista identificado con ConstituentID_key.
                    artists_nacion = mp.get(map_ConstituentID, ConstituentID_key)["value"]["Nationality"]

                    # Concatenar la nacionalidad del artista actual con las demás nacionalidades.
                    new_Nacion_key += artists_nacion



                    #####-----#####-----#####-----#####   Bloque Map 'DisplayName'   #####-----#####-----#####-----#####
                    
                    # Crear variable que guarda el nombre del artista identificado con ConstituentID_key.
                    artist_DisplayName = mp.get(map_ConstituentID, ConstituentID_key)['value']['DisplayName']

                    # Determinar si el artista se encuentra en el map 'DisplayName'.
                    exists_DisplayName = mp.contains(map_DisplayName, artist_DisplayName)


                    # Si se encuentra.
                    if (exists_DisplayName):

                        # Guardar el Medium_map del artista y añadir la obra actual al mapa 'Medium' del artista.
                        artists_Medium_map = mp.get(map_DisplayName, artist_DisplayName)['value'] 
                        model.add_pair_Medium_artworkList(artists_Medium_map, artwork_Medium, artwork_info)
                    
                    # Si no se encuentra.
                    else:

                        # Crear una pareja DisplayName-Medium_map.
                        model.add_DisplayName(catalog, artist_DisplayName)

                        # Guardar el Medium_map del artista y añadir la obra actual al mapa 'Medium' del artista.
                        artists_Medium_map = mp.get(map_DisplayName, artist_DisplayName)['value'] 
                        model.add_pair_Medium_artworkList(artists_Medium_map, artwork_Medium, artwork_info)


        # Añadir la pareja llave-valor al map 'Nationality'.
        model.add_Nationality(catalog, new_Nacion_key, artwork_info)



        #####-----#####-----#####-----#####   Bloque Map 'DateAcquired'   #####-----#####-----#####-----#####

        # Añadir la pareja llave-valor al map 'DateAcquired' si su fecha de adquicisión está registrada.
        if not (artwork_DateAcquired == ""):
            model.add_DateAcquired(catalog, artwork_DateAcquired, artwork_info)
        


        
#####-----#####-----#####-----#####-----#####   ########-----#####-----########   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   FUNCIONES CONEXIÓN MODEL Y VIEW   #####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####   ########-----#####-----########   #####-----#####-----#####-----#####-----#####

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

    # Crear variable que guarda la respuesta del requerimiento 1 y retornarla.
    resp_req_1 = model.req_1(catalog, first_year, last_year)
    return resp_req_1



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

    # Crear variable que guarda la respuesta del requerimiento 2 y retornarla.
    resp_req_2 = model.req_2(catalog, first_date, last_date)
    return resp_req_2



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

    # Crear variable que guarda la respuesta del requerimiento 3 y retornarla.
    resp_req_3 = model.req_3(catalog, param_DisplayName)
    return resp_req_3













'''
# Pruebas req.1.

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
'''

"""
# Mapa BeginDate.
mapa_begdat = catalog["BeginDate"]


lista_acual = mp.get(mapa_begdat, 1944)['value']
iterador_elem_lista = lt.iterator(lista_acual)

for elemento in iterador_elem_lista:
    print(elemento)
"""

'''
# Pruebas req 2.
catalog = init_catalog()
load_data(catalog)

resp = model.req_2(catalog, '1944-06-06', '1989-11-09')
print(lt.size(resp[0]), resp[1])

lista = resp[0]
print(lt.getElement(lista,1)['Title'])
print(lt.getElement(lista,2)['Title'])
print(lt.getElement(lista,3)['Title'])
print(lt.getElement(lista, lt.size(lista) - 2)['Title'])
print(lt.getElement(lista, lt.size(lista) - 1)['Title'])
print(lt.getElement(lista, lt.size(lista))['Title'])
'''

'''
map_prueba = mp.newMap()

for i in range(6):
    nuevo_mapa = mp.newMap()
    mp.put(map_prueba, "mapa_" + str(i), nuevo_mapa)

mapa_del_mapa = mp.get(map_prueba, "mapa_1")['value']
for j in range(4):
    mp.put(mapa_del_mapa, "medio_" + str(j), j)

for medio in lt.iterator(mp.keySet(mapa_del_mapa)):
    print(medio)
'''