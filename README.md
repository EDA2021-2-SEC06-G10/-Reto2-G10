Integrantes:
 <> José Nicolás Cárdenas - 201922006 - j.cardenast@uniandes.edu.co
 <> Andrés Leonardo Beltran - 202014143 - al.beltran@uniandes.edu.co



#####-----#####-----#####-----#####   ###---##---###   #####-----#####-----#####-----#####
#####-----#####-----#####-----#####   MODIFICACIONES   #####-----#####-----#####-----#####
#####-----#####-----#####-----#####   ###---##---###   #####-----#####-----#####-----#####


##--##--##  General  ##--##--##

 1- 


##--##--##  Model  ##--##--##

 1- Mediante la función new_catalog(), se añadieron tres maps al catálogo: 'Medium', 'Nacionality' y 'ConstituentID'.

 2- Se importó la librería probehashtable para poder usar la función nextPrime().

 3- Se definieron las siguientes funciones:
    -> add_Medium().
    -> add_Nationality().
    -> add_ConstituentID().



##--##--##  Controller  ##--##--##

 1- Se modificó la función load_artists() de tal forma que esta permita añadir parejas llave-valor al map 'ConstituentID'.

 2- Se modificó la función load_artworks() de tal forma que esta permita añadir parejas llave-valor a los maps 'Medium' y 'Nationality'.


##--##--##  View  ##--##--##
 
 1- Se importó la librería time para poder realizar las mediciones de tiempo.

 2- Se modificó la iteración del usuario para que fuese posible calcular el tiempo que se demora en cargar los datos.

 3- Se modificó la función print_menu() para que considerara una séptima opción, la cual hará referencia al requerimiento extra del laboratorio 6.

 4- Se importó la librería map.


#####-----#####-----#####-----#####   #---#---#   #####-----#####-----#####-----#####
#####-----#####-----#####-----#####   PENDIENTE   #####-----#####-----#####-----#####
#####-----#####-----#####-----#####   #---#---#   #####-----#####-----#####-----#####


##--##--##  Dudas  ##--##--##
 1- ¿Por qué sale un error de recursión al intentar imprimir la lista de artistas implementada como una lista enlazada?

 2- ¿Por qué sale un KeyError cuando se intentan cargar los datos del archivo large de los artistas?

 3- Modificar model y controller de tal forma que los valores de los maps del catálogo hagan referencia a los valores de las listas de artistas y obras, de tal forma que se disminuya el uso del espacio. 


##--##--##  Model  ##--##--##

 1- De la función newCatalog():
    -> Determinar si es más conveniente implementar las listas de las obras y de los artistas como una lista enlazada o como un arreglo. Además, hay que añadir las funciones de comparación de cada uno.
    -> Determinar qué tipo de tabla de Hash será la más conveniente para el mapa "BeginDate" y el tamaño adecuado.

  2- Modificar la función new_artist() de tal forma que los datos desconocidos del artista se guarden como "N.A.".

  3- Determinar si la quicksort es el algoritmo más conveniente para ordenar la lista de la función req_1().

  4- Determinar el tamaño adecuado para el map 'Nationality'.



##--##--##  Controller  ##--##--##

 1- 