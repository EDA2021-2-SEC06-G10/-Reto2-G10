Integrantes:
 <> José Nicolás Cárdenas - 201922006 - j.cardenast@uniandes.edu.co
 <> Andrés Leonardo Beltran - 202014143 - al.beltran@uniandes.edu.co



#####-----#####-----#####-----#####   ###---##---###   #####-----#####-----#####-----#####
#####-----#####-----#####-----#####   MODIFICACIONES   #####-----#####-----#####-----#####
#####-----#####-----#####-----#####   ###---##---###   #####-----#####-----#####-----#####


##--##--##  General  ##--##--##

 1- 


##--##--##  Model  ##--##--##

 1- Se modificó la función new_artwork() de tal forma que fuese posible saber el CreditLine y las Dimensions de cada obra.

 2- Se modificó la función new_catalog() para añadir al catálogo el map 'DateAcquired'. Además, se borraron de esta las listas 'artists' y 'artworks', ya que estas no servían propósito alguno.

 3- Teniendo en cuenta esto último, se eliminaros las funciones add_artist() y add_artwork(), ya que tampoco servían para nada.

 4- Se definieron las siguientes funciones:
    -> add_DateAcquired().
    -> cmp_by_DateAcquired().

5- Se importó la librería datetime.



##--##--##  Controller  ##--##--##

 1- Se modificó la función load_artworks() de tal forma que siempre que se añada información de una obra se haga referencia al mismo diccionario que representa dicha usando la función model.new_artwork(). 

 2- Se modificó la función load_artworks() para que se pudiesen añadir parejas llave-valor al map 'DateAcquired'.


##--##--##  View  ##--##--##
 
 1- 


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