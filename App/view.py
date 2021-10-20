"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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

import os
import datetime as date
from typing import Container
import config as cf
from DISClib.ADT import map as mp
import time
import sys
import controller
from DISClib.ADT import list as lt
assert cf




#####-----#####-----#####-----#####-----#####-----#####   #####---######---#####   #####-----#####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####-----#####   FUNCIONES DE IMPRESIÓN   #####-----#####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####-----#####   #####---######---#####   #####-----#####-----#####-----#####-----#####-----#####

"""
    Se definen las funciones que permitirán imprimir el menú y los resultados de cada
    requerimiento, de tal forma que se dispongan de una manera amigable para el usuario.

"""

# Función que imprime el menú de opciones de la herramienta.
def print_menu () -> None:
    """
        Esta función imprime el menú de interacción con el usuario. No tiene ni parámetros ni retorno.

    """

    print("""\n======================= BIENVENIDO =======================\n""")
    print("  1- Cargar información al catálogo.")
    print("  2- Cargar requerimiento 1.")
    print("  3- Cargar requerimiento 2.")
    print("  4- Cargar requerimiento 3.")
    print("  5- Cargar requerimiento 4.")
    print("  6- Cargar requerimiento 5.")
    print("  7- Cargar requerimiento del lab. 6.")
    print("  0- Salir.")



# Función que imprime la respuesta del requerimiento 1.
def print_req_1 (first_year: int, last_year: int, resp_req_1: dict) -> None:
    """
        Esta función imprime la respuesta del requerimiento 1 de una manera amigable para el usuario.

        Parámetro:
            -> first_year (int): primer año del intervalo.
            -> last_year (int): último año del intervalo.
            -> resp_req_1 (tuple): lista que contiene las respuestas del requerimiento 1.

        No tiene retorno.

    """

    # Respuesta inicial.
    print('En total, hay', lt.size(resp_req_1), 'artistas que nacieron entre ' + str(first_year) + ' y ' + str(last_year) + '.')

    # Si hay datos en la lista.
    if not (lt.size(resp_req_1) == 0):

        print('Una muestra del rango cronológico se dispone a continuación:\n')

        # Header.
        print("#" * 131)
        print("# ", end = " ")
        print(fixed_length('NOMBRE', 40), end = " # ")
        print(fixed_length('NACIMIENTO', 10), end = " # ")
        print(fixed_length('FALLECIMIENTO', 13), end = " # ")
        print(fixed_length('NACIONALIDAD', 30), end = " # ")
        print(fixed_length('GÉNERO', 21), end = " # ")
        print()
        print("#" * 131)

        # Datos tabla.
        if (lt.size(resp_req_1)) < 6:
            for element in lt.iterator(resp_req_1):
                print("# ", end = " ")
                print(fixed_length(element['DisplayName'], 40), end = " # ")
                print(fixed_length(str(element['BeginDate']), 10), end = " # ")
                print(fixed_length(str(element['EndDate']), 13), end = " # ")
                print(fixed_length(element['Nationality'], 30), end = " # ")
                print(fixed_length(element['Gender'], 21), end = " # ")
                print()
            print("#" * 131)

        else:
            
            new_list = lt.newList('SINGLE_LINKED')
            size_lt_med = lt.size(resp_req_1)
            lt.addLast(new_list, lt.getElement(resp_req_1, 1))
            lt.addLast(new_list, lt.getElement(resp_req_1, 2))
            lt.addLast(new_list, lt.getElement(resp_req_1, 3))
            lt.addLast(new_list, lt.getElement(resp_req_1, size_lt_med -2))
            lt.addLast(new_list, lt.getElement(resp_req_1, size_lt_med -1))
            lt.addLast(new_list, lt.getElement(resp_req_1, size_lt_med))

            for element in lt.iterator(new_list):
                print("# ", end = " ")
                print(fixed_length(element['DisplayName'], 40), end = " # ")
                print(fixed_length(str(element['BeginDate']), 10), end = " # ")
                print(fixed_length(str(element['EndDate']), 13), end = " # ")
                print(fixed_length(element['Nationality'], 30), end = " # ")
                print(fixed_length(element['Gender'], 21), end = " # ")
                print()
            print("#" * 131)
        
    print()    



# Función que imprime la respuesta del requerimiento 2.
def print_req_2 (first_date, last_date, resp_req_2: dict) -> None:
    """
        Esta función imprime la respuesta del requerimiento 2 de una manera amigable para el usuario.

        Parámetro:
            -> first_date: primera fecha del intervalo.
            -> last_date: última fecha del intervalo.
            -> resp_req_2 (tuple): lista que contiene las respuestas del requerimiento 2.

        No tiene retorno.

    """

    # Desempaquetar respuesta.
    ordered_ordered_list, num_purch = resp_req_2
    num_artw = lt.size(ordered_ordered_list)
    
    # Mapa 'ConstituentID'.
    map_consid = catalog['ConstituentID']


    # Respuesta inicial.
    print('En total, el museo adquirió', num_artw, 'obras entre',  first_date, 'y', str(last_date) + '.')
    print('De estas obras,', num_purch, "fueron adquiridas por compra.\n")

    # Lista.
    print('Una muestra de algunas de las obras adquirirdas por el museo entre dichas fechas se dispone a continuación:\n')

    # Tabla técnicas más usadas.
    print("#" * 147)
    print("# ", end = " ")
    print(fixed_length('TÍTULO', 30), end = " # ")
    print(fixed_length('ARTISTA(S)', 40), end = " # ")
    print(fixed_length('FECHA', 5), end = " # ")
    print(fixed_length('TÉCNICA', 25), end = " # ")
    print(fixed_length('DIMENSIONES', 30), end = " # ")
    print()
    print("#" * 147)

    if (lt.size(ordered_ordered_list)) < 6:
        for element in lt.iterator(ordered_ordered_list):
            
            print("# ", end = " ")
            print(fixed_length(element['Title'], 30), end = " # ")

            if len(element['ConstituentID']) == 1:
                artists_id = element['ConstituentID'][0]
                name = mp.get(map_consid, float(int(artists_id)))['value']['DisplayName']
                print(fixed_length(name, 40), end = " # ")
            
            else:
                str_artists = ''
                num_artists = len(element['ConstituentID']) - 1
                counter = 0
                for artist in element['ConstituentID']:
                    name = mp.get(map_consid, float(int(artist)))['value']['DisplayName']
                    if (counter == num_artists):
                        str_artists += name
                    else:
                        str_artists += name + ", "
                    counter += 1
                print(fixed_length(str_artists, 40), end = " # ")

            print(fixed_length(element['Date'], 5), end = " # ")
            print(fixed_length(element['Medium'], 25), end = " # ")
            print(fixed_length(element['Dimensions'], 30), end = " # ")
            print()

        print("#" * 147)

    else:

        new_list = lt.newList('SINGLE_LINKED')
        lt.addLast(new_list, lt.getElement(ordered_ordered_list, 1))
        lt.addLast(new_list, lt.getElement(ordered_ordered_list, 2))
        lt.addLast(new_list, lt.getElement(ordered_ordered_list, 3))
        lt.addLast(new_list, lt.getElement(ordered_ordered_list, num_artw - 2))
        lt.addLast(new_list, lt.getElement(ordered_ordered_list, num_artw - 1))
        lt.addLast(new_list, lt.getElement(ordered_ordered_list, num_artw))
         

        for element in lt.iterator(new_list):
            
            print("# ", end = " ")
            print(fixed_length(element['Title'], 30), end = " # ")

            if len(element['ConstituentID']) == 1:
                artists_id = element['ConstituentID'][0]
                name = mp.get(map_consid, float(int(artists_id)))['value']['DisplayName']
                print(fixed_length(name, 40), end = " # ")
            
            else:
                str_artists = ''
                num_artists = len(element['ConstituentID']) - 1
                counter = 0
                for artist in element['ConstituentID']:
                    name = mp.get(map_consid, float(int(artist)))['value']['DisplayName']
                    if (counter == num_artists):
                        str_artists += name
                    else:
                        str_artists += name + ", "
                    counter += 1
                print(fixed_length(str_artists, 40), end = " # ")

            print(fixed_length(element['Date'], 5), end = " # ")
            print(fixed_length(element['Medium'], 25), end = " # ")
            print(fixed_length(element['Dimensions'], 30), end = " # ")
            print()

        print("#" * 147)



# Función que imprime la respuesta del requerimiento 3.
def print_req_3 (artist_name: str, resp_req_3: tuple) -> None:
    """
        Esta función imprime la respuesta del requerimiento 3 de una manera amigable para el usuario.

        Parámetro:
            -> artist_name (str): nombre del artista.
            -> resp_req_3 (tuple): tupla que contiene las respuestas del requerimiento 3.

        No tiene retorno.

    """

    # Desempaquetar resp_req_3.
    total_artworks, total_mediums, most_used_medium, list_most_used_medium, ordered_list_most_used_medium = resp_req_3


    # Primera parte.
    print(artist_name, 'tiene ' + str(total_artworks) + ' obras a su nombre en el museo.')
    print('Él/ella ha usado ' + str(total_mediums) + ' técnicas diferentes para crear sus obras.')
    print('\nLa lista de sus técnicas más usadas es la siguiente:\n')


    # Tabla técnicas más usadas.
    print("#" * 56)
    print("# ", end = " ")
    print(fixed_length('TÉCNICA', 40), end = " # ")
    print(fixed_length('CANTIDAD', 8), end = " # ")
    print()
    print("#" * 56)

    if (lt.size(ordered_list_most_used_medium)) < 5:
        for element in lt.iterator(ordered_list_most_used_medium):
            print("# ", end = " ")
            print(fixed_length(str(element[0]), 40), end = " # ")
            print(fixed_length(str(element[1]), 8), end = " # ")
            print() 
        print("#" * 56)

    else:
        for i in range (1, 6):
            element = lt.getElement(ordered_list_most_used_medium, i)
            print("# ", end = " ")
            print(fixed_length(str(element[0]), 40), end = " # ")
            print(fixed_length(str(element[1]), 8), end = " # ")
            print() 
        print("#" * 56)

    print("\nComo se puede apreciar, su técnica más usada es '" + str(most_used_medium)+ "'.")

    
    # Tabla obras con técnica most_used_medium.
    print('Una muestra de algunas obras creadas usando dicha técnica se dispone a continuación:\n')
    print("#" * 131)
    print("# ", end = " ")
    print(fixed_length('TÍTULO', 51), end = " # ")
    print(fixed_length('FECHA', 5), end = " # ")
    print(fixed_length('MEDIO', 30), end = " # ")
    print(fixed_length('DIMENSIONES', 31), end = " # ")
    print()
    print("#" * 131)
    
    if (lt.size(list_most_used_medium)) < 6:
        for element in lt.iterator(list_most_used_medium):
            print("# ", end = " ")
            print(fixed_length(element['Title'], 51), end = " # ")
            print(fixed_length(element['Date'], 5), end = " # ")
            print(fixed_length(element['Medium'], 30), end = " # ")
            print(fixed_length(element['Dimensions'], 31), end = " # ")
            print()
        print("#" * 131)

    else:
        new_list = lt.newList('SINGLE_LINKED')
        size_lt_med = lt.size(list_most_used_medium)
        lt.addLast(new_list, lt.getElement(list_most_used_medium, 1))
        lt.addLast(new_list, lt.getElement(list_most_used_medium, 2))
        lt.addLast(new_list, lt.getElement(list_most_used_medium, 3))
        lt.addLast(new_list, lt.getElement(list_most_used_medium, size_lt_med -2))
        lt.addLast(new_list, lt.getElement(list_most_used_medium, size_lt_med -1))
        lt.addLast(new_list, lt.getElement(list_most_used_medium, size_lt_med))

        for element in lt.iterator(new_list):
            print("# ", end = " ")
            print(fixed_length(element['Title'], 51), end = " # ")
            print(fixed_length(element['Date'], 5), end = " # ")
            print(fixed_length(element['Medium'], 30), end = " # ")
            print(fixed_length(element['Dimensions'], 31), end = " # ")
            print()
        print("#" * 131)

    print()



# Función que imprime la respuesta del requerimiento 5.
def print_req_5 (dep_name: str, resp_req_5: tuple) -> None:
    """
        Esta función imprime la respuesta del requerimiento 5 de una manera amigable para el usuario.

        Parámetro:
            -> dep_name (str): nombre del departamento.
            -> resp_req_5 (tuple): tupla que contiene las respuestas del requerimiento 5.

        No tiene retorno.

    """

    # Desempaquetar resp_req_5.
    total_price, total_weight, lt_ord_art_date, lt_ord_art_price = resp_req_5

    # Mapa 'ConstituentID'.
    map_consid = catalog['ConstituentID']

    # Primera parte.
    print('Sería necesario transportar', lt.size(lt_ord_art_price) , 'obras del departamento', "'" + dep_name + "'" , 'del museo.')
    print('Aproximadamente, el costo total de esta operación equivaldría a $USD', str(total_price) + '.')
    print('En total, habría que transportar', total_weight, 'kg aproximadamente.')

    # Segunda parte.
    print('\nUna muestra de las obras con los costos de transporte más altos se dispone a continuación:\n')
    print("#" * 147)
    print("# ", end = " ")
    print(fixed_length('TÍTULO', 30), end = " # ")
    print(fixed_length('ARTISTA(S)', 40), end = " # ")
    print(fixed_length('CLASIFICACIÓN', 15), end = " # ")
    print(fixed_length('FECHA', 5), end = " # ")
    print(fixed_length('DIMENSIONES', 25), end = " # ")
    print(fixed_length('COSTO (USD)', 12), end = " # ")
    print()
    print("#" * 147)

    if (lt.size(lt_ord_art_price)) < 5:
        for element in lt.iterator(lt_ord_art_price):
            
            print("# ", end = " ")
            print(fixed_length(element['Title'], 30), end = " # ")

            if len(element['ConstituentID']) == 1:
                artists_id = element['ConstituentID'][0]
                name = mp.get(map_consid, float(int(artists_id)))['value']['DisplayName']
                print(fixed_length(name, 40), end = " # ")
            
            else:
                str_artists = ''
                num_artists = len(element['ConstituentID']) - 1
                counter = 0
                for artist in element['ConstituentID']:
                    name = mp.get(map_consid, float(int(artist)))['value']['DisplayName']
                    if (counter == num_artists):
                        str_artists += name
                    else:
                        str_artists += name + ", "
                    counter += 1
                print(fixed_length(str_artists, 40), end = " # ")

            print(fixed_length(element['Classification'], 15), end = " # ")
            print(fixed_length(element['Date'], 5), end = " # ")
            print(fixed_length(element['Dimensions'], 25), end = " # ")
            print(fixed_length(str(round(element['Price (USD)'],3)), 12), end = " # ")
            print()
        print("#" * 147)

    else:

        new_list = lt.newList('SINGLE_LINKED')
        lt.addLast(new_list, lt.getElement(lt_ord_art_price, 1))
        lt.addLast(new_list, lt.getElement(lt_ord_art_price, 2))
        lt.addLast(new_list, lt.getElement(lt_ord_art_price, 3))
        lt.addLast(new_list, lt.getElement(lt_ord_art_price, 4))
        lt.addLast(new_list, lt.getElement(lt_ord_art_price, 5))
         

        for element in lt.iterator(new_list):
            
            print("# ", end = " ")
            print(fixed_length(element['Title'], 30), end = " # ")

            if len(element['ConstituentID']) == 1:
                artists_id = element['ConstituentID'][0]
                name = mp.get(map_consid, float(int(artists_id)))['value']['DisplayName']
                print(fixed_length(name, 40), end = " # ")
            
            else:
                str_artists = ''
                num_artists = len(element['ConstituentID']) - 1
                counter = 0
                for artist in element['ConstituentID']:
                    name = mp.get(map_consid, float(int(artist)))['value']['DisplayName']
                    if (counter == num_artists):
                        str_artists += name
                    else:
                        str_artists += name + ", "
                    counter += 1
                print(fixed_length(str_artists, 40), end = " # ")

            print(fixed_length(element['Classification'], 15), end = " # ")
            print(fixed_length(element['Date'], 5), end = " # ")
            print(fixed_length(element['Dimensions'], 25), end = " # ")
            print(fixed_length(str(round(element['Price (USD)'],3)), 12), end = " # ")
            print()
        print("#" * 147)



    # Tercera parte.
    print('\nPor otro lado, una muestra de las obras más antiguas que se van a transportar se dispone a continuación:\n')
    print("#" * 147)
    print("# ", end = " ")
    print(fixed_length('TÍTULO', 30), end = " # ")
    print(fixed_length('ARTISTA(S)', 40), end = " # ")
    print(fixed_length('CLASIFICACIÓN', 15), end = " # ")
    print(fixed_length('FECHA', 5), end = " # ")
    print(fixed_length('DIMENSIONES', 25), end = " # ")
    print(fixed_length('COSTO (USD)', 12), end = " # ")
    print()
    print("#" * 147)

    if (lt.size(lt_ord_art_date)) < 5:
        for element in lt.iterator(lt_ord_art_date):
            
            print("# ", end = " ")
            print(fixed_length(element['Title'], 30), end = " # ")

            if len(element['ConstituentID']) == 1:
                artists_id = element['ConstituentID'][0]
                name = mp.get(map_consid, float(int(artists_id)))['value']['DisplayName']
                print(fixed_length(name, 40), end = " # ")
            
            else:
                str_artists = ''
                num_artists = len(element['ConstituentID']) - 1
                counter = 0
                for artist in element['ConstituentID']:
                    name = mp.get(map_consid, float(int(artists_id)))['value']['DisplayName']
                    if (counter == num_artists):
                        str_artists += name
                    else:
                        str_artists += name + ", "
                    counter += 1
                print(fixed_length(str_artists, 40), end = " # ")

            print(fixed_length(element['Classification'], 15), end = " # ")
            print(fixed_length(element['Date'], 5), end = " # ")
            print(fixed_length(element['Dimensions'], 25), end = " # ")
            print(fixed_length(str(round(element['Price (USD)'],3)), 12), end = " # ")
            print()
        print("#" * 147)

    else:

        new_list = lt.newList('SINGLE_LINKED')
        lt.addLast(new_list, lt.getElement(lt_ord_art_date, 1))
        lt.addLast(new_list, lt.getElement(lt_ord_art_date, 2))
        lt.addLast(new_list, lt.getElement(lt_ord_art_date, 3))
        lt.addLast(new_list, lt.getElement(lt_ord_art_date, 4))
        lt.addLast(new_list, lt.getElement(lt_ord_art_date, 5))
         

        for element in lt.iterator(new_list):
            
            print("# ", end = " ")
            print(fixed_length(element['Title'], 30), end = " # ")

            if len(element['ConstituentID']) == 1:
                artists_id = element['ConstituentID'][0]
                name = mp.get(map_consid, float(int(artists_id)))['value']['DisplayName']
                print(fixed_length(name, 40), end = " # ")
            
            else:
                str_artists = ''
                num_artists = len(element['ConstituentID']) - 1
                counter = 0
                for artist in element['ConstituentID']:
                    name = mp.get(map_consid, float(int(artist)))['value']['DisplayName']
                    if (counter == num_artists):
                        str_artists += name
                    else:
                        str_artists += name + ", "
                    counter += 1
                print(fixed_length(str_artists, 40), end = " # ")

            print(fixed_length(element['Classification'], 15), end = " # ")
            print(fixed_length(element['Date'], 5), end = " # ")
            print(fixed_length(element['Dimensions'], 25), end = " # ")
            print(fixed_length(str(round(element['Price (USD)'],3)), 12), end = " # ")
            print()
        print("#" * 147)

    print()




#####-----#####-----#####-----#####-----#####-----#####   ######---######---######   #####-----#####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####-----#####   FUNCIONES CARGA DE DATOS   #####-----#####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####-----#####   ######---######---######   #####-----#####-----#####-----#####-----#####-----#####

"""
    Se definen las funciones que permitirán inicializar el catálogo del museo y cargar
    los elementos de la base de datos.

"""

# Función que inicializa el catálogo del museo.
def init_catalog () -> dict:
    """
        Inicializa el catálogo del museo.

        No tiene parámtros.
        
        Retorno:
            -> (dict): el catálogo del museo.

    """
    # Crear variable que guarda el catálogo y retornarlo.
    # Este se crea mediante la función homónima de controller.py.
    catalog = controller.init_catalog()
    return catalog



# Función que carga todos los datos al catálogo.
def load_data (catalog: dict) -> None:
    """
        Esta función carga todos los datos de interés de la carpeta Data/MoMA.

        Parámetro:
            -> catalog (dict): catálogo.

        No tiene retorno.

    """
    # Cargar los datos mediante la función homónima de controller.py.
    controller.load_data(catalog)




#####-----#####-----#####-----#####-----#####-----#####   ######---######---######   #####-----#####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####-----#####   FUNCIONES CARGA DE DATOS   #####-----#####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####-----#####   ######---######---######   #####-----#####-----#####-----#####-----#####-----#####

"""
    A continuación se definen funciones que serán de utilidad en general.

"""

# Función que permite acortar texto.
def fixed_length (text:str, lenght: int) -> str:
    if len(text) > lenght:
        text = text[:lenght -3] + '...'
    elif len(text) < lenght:
        text = (text + " " * lenght)[:lenght]
    return(text)



#####-----#####-----#####-----#####-----#####-----#####   ###---##---###   #####-----#####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####-----#####   MENÚ PRINCIPAL   #####-----#####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####-----#####   ###---##---###   #####-----#####-----#####-----#####-----#####-----#####

"""
    Se define la iteración indefinida que permitirá al usuario cargar la información al catálogo y consultar los
    resultados de cada requerimiento. 

"""

# Crear variable que guardará el catálogo.
catalog = None

# Crear variables que permitirán medir el tiempo de ejecución de la carga de datos.
start_time = 0.0
stop_time = 0.0

# Limpiar la consola.
os.system('cls')

# Iteración usuario.
while True:

    # Imprimir el menú.
    print_menu()

    # Preguntar al usuario la acción que desea realizar.
    inputs = input('\nPor favor, seleccione una opción para continuar:\n  -> ')

    # Si el usuario ingresó una opción válida.
    try:

        # Si escoge la opción 1.
        if int(inputs[0]) == 1:

            # Limpiar la consola.
            os.system('cls')
            
            # Imprimir mensaje de carga.
            print("""\n======================= Carga de Datos =======================\n""")
            print("Cargando información al catálogo ...")

            # Inicializar catálogo.
            catalog = init_catalog()

            # Iniciar el tiempo.
            start_time = time.process_time()

            # Cargar datos al catálogo.
            load_data(catalog)

            # Parar el tiempo.
            stop_time = time.process_time()

            # Calcular tiempo de ejecución en milisegundos.
            elapsed_time_mseg = (stop_time - start_time)*1000

            # Imprimir mensaje de éxito.
            print("\n<> Información cargada con éxito. <>")
            print("Tiempo de ejecución:", elapsed_time_mseg, "milisegundos.")



        # Si escoge la opción 2.
        elif int(inputs[0]) == 2:

            # Limpiar la consola.
            os.system('cls')

            # Imprimir mensaje de carga.
            print("""\n======================= Inputs Req. 1 =======================\n""")
                
            # Preguntar al usuario por la nacionalidad.
            inputs_1 = input('Por favor, escriba el año inicial (YYYY):\n  -> ')
            inputs_2 = input('Por favor, escriba el año final (YYYY):\n  -> ')

            # Transformar datos de entrada.
            int_inputs_1 = int(inputs_1)
            int_inputs_2 = int(inputs_2)


            # Si el intervalo es válido.
            if not ((int_inputs_1 >= int_inputs_2) or (int_inputs_1 <= 0 or int_inputs_2 <= 0) or (int_inputs_2 > 2018)):

                # Imprimir mensaje de carga.
                print("""\n====================== Outputs Req. 1 =======================\n""")

                # Iniciar el tiempo.
                start_time = time.process_time()

                # Guardar respuesta del requerimiento 3.
                resp_req_1 = controller.req_1(catalog, int(inputs_1), int(inputs_2))

                # Parar el tiempo.
                stop_time = time.process_time()

                # Calcular tiempo de ejecución en milisegundos e imprimirlo.
                elapsed_time_mseg = (stop_time - start_time)*1000
                print("Tiempo de ejecución del requerimiento:", elapsed_time_mseg, "milisegundos.\n")

                # Imprimir respuesta.
                print_req_1(inputs_1, inputs_2, resp_req_1)


            # De lo contrario.
            else:
                
                # Imprimir mensaje de error.
                print("""\n======================= ERROR =======================\n""")
                print("Debe ingresar un intervalo válido. Intente de nuevo.\n")
                sys.exit(0)



        # Si escoge la opción 3.
        elif int(inputs[0]) == 3:
            
            # Limpiar la consola.
            os.system('cls')

            # Imprimir mensaje de carga.
            print("""\n======================= Inputs Req. 2 =======================\n""")
                
            # Preguntar al usuario por las fechas.
            inputs_1 = input('Por favor, escriba la fecha inicial (AAAA-MM-DD):\n  -> ')
            inputs_2 = input('Por favor, escriba la fecha final (AAAA-MM-DD):\n  -> ')

            # Crear variables con las fechas de adquisición modificadas.
            mod_first_date = date.datetime.strptime(inputs_1, '%Y-%m-%d')
            mod_last_date = date.datetime.strptime(inputs_2, '%Y-%m-%d')

            # Determinar si el intervalo es válido.
            valid = not ((mod_last_date < mod_first_date) or (mod_first_date > mod_last_date) or (mod_first_date == mod_last_date))

            # Si el intervalo es válido..
            if (valid):
                
                # Imprimir mensaje de carga.
                print("""\n====================== Outputs Req. 2 =======================\n""")

                # Iniciar el tiempo.
                start_time = time.process_time()

                # Guardar respuesta del requerimiento 3.
                resp_req_2 = controller.req_2(catalog, inputs_1, inputs_2)

                # Parar el tiempo.
                stop_time = time.process_time()

                # Calcular tiempo de ejecución en milisegundos e imprimirlo.
                elapsed_time_mseg = (stop_time - start_time)*1000
                print("Tiempo de ejecución del requerimiento:", elapsed_time_mseg, "milisegundos.\n")

                # Imprimir respuesta.
                print_req_2(inputs_1, inputs_2, resp_req_2)


            # De lo contrario.
            else:

                # Imprimir mensaje de error.
                print("""\n======================= ERROR =======================\n""")
                print("Debe ingresar un intervalo válido. Intente de nuevo.\n")
                sys.exit(0)



        # Si escoge la opción 4.
        elif int(inputs[0]) == 4:
            
            # Limpiar la consola.
            os.system('cls')

            # Imprimir mensaje de carga.
            print("""\n======================= Inputs Req. 3 =======================\n""")
                
            # Preguntar al usuario por la nacionalidad.
            inputs = input('Por favor, escriba el nombre del artista:\n  -> ')

            # Determinar si el artista con nombre inputs se encuentra en este.
            is_in_catalog = mp.contains(catalog['DisplayName'], inputs)


            # Si se encuentra.
            if (is_in_catalog):

                # Imprimir mensaje de carga.
                print("""\n====================== Outputs Req. 3 =======================\n""")

                # Iniciar el tiempo.
                start_time = time.process_time()

                # Guardar respuesta del requerimiento 3.
                resp_req_3 = controller.req_3(catalog, inputs)

                # Parar el tiempo.
                stop_time = time.process_time()

                # Calcular tiempo de ejecución en milisegundos e imprimirlo.
                elapsed_time_mseg = (stop_time - start_time)*1000
                print("Tiempo de ejecución del requerimiento:", elapsed_time_mseg, "milisegundos.\n")

                # Imprimir respuesta.
                print_req_3(inputs, resp_req_3)

            
            # De lo contrario.
            else:

                # Limpiar la consola.
                os.system('cls')

                # Imprimir mensaje de error.
                print("""\n======================= ERROR =======================\n""")
                print("El/la artista de nombre '" + inputs + "' no se encuentra en el catálogo. Intente de nuevo.\n")
                sys.exit(0)



        # Si escoge la opción 6.
        elif int(inputs[0]) == 6:
            
            # Limpiar la consola.
            os.system('cls')

            # Imprimir mensaje de carga.
            print("""\n======================= Inputs Req. 5 =======================\n""")
                
            # Preguntar al usuario por el departamento.
            inputs = input('Por favor, escriba el nombre del departamento del museo cuyas obras desea transportar:\n  -> ')

            # Determinar si el artista con nombre inputs se encuentra en este.
            is_in_catalog = mp.contains(catalog['Department'], inputs)


            # Si se encuentra.
            if (is_in_catalog):
                
                # Imprimir mensaje de carga.
                print("""\n====================== Outputs Req. 5 =======================\n""")

                # Iniciar el tiempo.
                start_time = time.process_time()

                # Guardar respuesta del requerimiento 3.
                resp_req_5 = controller.req_5(catalog, inputs)

                # Parar el tiempo.
                stop_time = time.process_time()

                # Calcular tiempo de ejecución en milisegundos e imprimirlo.
                elapsed_time_mseg = (stop_time - start_time)*1000
                print("Tiempo de ejecución del requerimiento:", elapsed_time_mseg, "milisegundos.\n")

                # Imprimir respuesta.
                print_req_5(inputs, resp_req_5)


            # De lo contrario.
            else:

                # Limpiar la consola.
                os.system('cls')

                # Imprimir mensaje de error.
                print("""\n======================= ERROR =======================\n""")
                print("El departamento de nombre '" + inputs + "' no se encuentra en el museo. Intente de nuevo.\n")
                sys.exit(0)



        # Si escoge la opción 8.
        elif int(inputs[0]) == 7:

            # Imprimir mensaje de carga.
            print("""\n======================= OPCIÓN 7 =======================\n""")
            
            # Preguntar al usuario por la nacionalidad.
            inputs = input('Por favor, escriba la nacionalidad:\n  -> ')

            # Crear variable que guarda el map 'Nationality'.
            map_Nation = catalog['Nationality']

            # Crear variable que determina si la nacionalidad está o no en el map 'Nationality'.
            exists = mp.contains(map_Nation, inputs)


            # Si la nacionalidad existe.
            if (exists):

                # Guardar lista de obras que tienen esa nacionalidad.
                artists_list = mp.get(map_Nation, inputs)['value']

                # Determinar número total de obras de la nacionalidad.
                num_artists = lt.size(artists_list)

                # Imprimir respuesta.
                print("\n<> Respuesta <>")
                print("El número total de obras cuyo/s autor/es tiene/n nacionalidad", "'" + str(inputs) + "'", "es:", str(num_artists) + ".")


            # Si se ingresa un valor erróneo.
            else:

                # Limpiar la consola.
                os.system('cls')

                # Imprimir mensaje de error.
                print("""\n======================= ERROR =======================\n""")
                print("Debe ingresar una nacionalidad válida.\n")
                sys.exit(0)

            sys.exit(0)




        # Si escoge la opción 0.
        elif int(inputs[0]) == 0:
            # Limpiar la consola.
            os.system('cls')
            
            # Imprimir mensaje de carga.
            print("""\n======================= Exit =======================\n""")
            print("Gracias por usar la herramienta. Hasta pronto.\n")

            sys.exit(0)



        # Si se ingresa un valor erróneo.
        else:
            print("""\n======================= ERROR =======================\n""")
            print("Debe ingresar una opción válida.\n\n")
            sys.exit(0)



    # Si el usuario ingresó una opción inválida.
    except ValueError:
        print("""\n======================= ERROR =======================\n""")
        print("Debe ingresar una opción válida.\n\n")
        sys.exit(0)

sys.exit(0)
