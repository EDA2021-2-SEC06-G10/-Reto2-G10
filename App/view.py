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

    print("""\n\n======================= BIENVENIDO =======================\n""")
    print("  1- Cargar información al catálogo.")
    print("  2- Cargar requerimiento 1.")
    print("  3- Cargar requerimiento 2.")
    print("  4- Cargar requerimiento 3.")
    print("  5- Cargar requerimiento 4.")
    print("  6- Cargar requerimiento 5.")
    print("  6- Cargar requerimiento 6.")
    print("  7- Cargar requerimiento del lab. 6.")
    print("  0- Salir.")




#####-----#####-----#####-----#####-----#####-----#####   ######---######---######   #####-----#####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####-----#####   FUNCIONES CARGA DE DATOS   #####-----#####-----#####-----#####-----#####-----#####
#####-----#####-----#####-----#####-----#####-----#####   ######---######---######   #####-----#####-----#####-----#####-----#####-----#####

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


# Iteración usuario.
while True:

    # Imprimir el menú.
    print_menu()

    # Preguntar al usuario la acción que desea realizar.
    inputs = input('Por favor, seleccione una opción para continuar:\n  -> ')

    # Si el usuario ingresó una opción válida.
    try:

        # Si escoge la opción 1.
        if int(inputs[0]) == 1:

            # Imprimir mensaje de carga.
            print("""\n======================= OPCIÓN 1 =======================\n""")
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
            print("Tiempo de demora:", elapsed_time_mseg, "milisegundos.")



        # Si escoge la opción 2.
        elif int(inputs[0]) == 2:
            pass



        # Si escoge la opción 7.
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
                    print("""\n======================= ERROR =======================\n""")
                    print("Debe ingresar una nacionalidad válida.\n\n")
                    sys.exit(0)





        # Si escoge la opción 0.
        elif int(inputs[0]) == 0:
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
