Integrantes:
 <> José Nicolás Cárdenas - 201922006 - j.cardenast@uniandes.edu.co
 <> Andrés Leonardo Beltran - 202014143 - al.beltran@uniandes.edu.co



#####-----#####-----#####-----#####   ###---##---###   #####-----#####-----#####-----#####
#####-----#####-----#####-----#####   MODIFICACIONES   #####-----#####-----#####-----#####
#####-----#####-----#####-----#####   ###---##---###   #####-----#####-----#####-----#####


##--##--##  General  ##--##--##

 1- 


##--##--##  Model  ##--##--##

 1- Se modificó la función new_catalog() para añadir el map 'DisplayName'.
 
 2- Se definieron las siguientes funciones:
    -> add_DisplayName().
    -> add_pair_Medium_artworkList().
    -> cmp_Mediums().
    -> req_3().
    -> cmp_artworks_by_Date().



##--##--##  Controller  ##--##--##

 1- En la función load_artworks(), se realizaron las siguientes modificaciones:
    -> Se ordenó el cuerpo de la función de tal forma que primero se guarden las variables de los valores de interés de la obra y los maps de interés del catálogo.
    -> Se añadió el bloque de código que permitirá añadir parejas llave valor al map 'DisplayName' del catálogo.

 2- Se definieron las siguientes funciones:
    -> req_1().
    -> req_2().
    -> req_3().   


##--##--##  View  ##--##--##
 
 1- Se definieron las siguientes funciones:
    -> print_req_3().
    -> fixed_length().

 2- Se importó la librería os.

 3- Se modificó el menú principal para que fuese posible implementar el requerimiento 3.


#####-----#####-----#####-----#####   #---#---#   #####-----#####-----#####-----#####
#####-----#####-----#####-----#####   PENDIENTE   #####-----#####-----#####-----#####
#####-----#####-----#####-----#####   #---#---#   #####-----#####-----#####-----#####


##--##--##  Dudas  ##--##--##
 1- ¿Por qué sale un error de recursión al intentar imprimir la lista de artistas implementada como una lista enlazada?

 2- ¿Por qué sale un KeyError cuando se intentan cargar los datos del archivo large de los artistas?

 3-


##--##--##  General  ##--##--##

 1- Modificar model y controller de tal forma que los valores de los maps del catálogo hagan referencia a los valores de las listas de artistas y obras, de tal forma que se disminuya el uso del espacio.

 2- Implementar el controller y el view de tal forma que se pueda usar los requerimientos 1 y 2.


##--##--##  Model  ##--##--##

 1- De la función newCatalog():
    -> Determinar si es más conveniente implementar las listas de las obras y de los artistas como una lista enlazada o como un arreglo. Además, hay que añadir las funciones de comparación de cada uno.
    -> Determinar qué tipo de tabla de Hash será la más conveniente para el mapa "BeginDate" y el tamaño adecuado.

  2- Modificar la función new_artist() de tal forma que los datos desconocidos del artista se guarden como "N.A.".

  3- Determinar si la quicksort es el algoritmo más conveniente para ordenar la lista de la función req_1().

  4- Determinar el tamaño adecuado para el map 'Nationality'.



##--##--##  Controller  ##--##--##

 1- 