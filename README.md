Integrantes:
 <> José Nicolás Cárdenas - 201922006 - j.cardenast@uniandes.edu.co
 <> Andrés Leonardo Beltran - 202014143 - al.beltran@uniandes.edu.co



#####-----#####-----#####-----#####   ###---##---###   #####-----#####-----#####-----#####
#####-----#####-----#####-----#####   MODIFICACIONES   #####-----#####-----#####-----#####
#####-----#####-----#####-----#####   ###---##---###   #####-----#####-----#####-----#####


##--##--##  General  ##--##--##

 1- Se añadió la carpeta de datos (MoMA) al repositorio.


##--##--##  Model  ##--##--##

 1- Se actualizó la documentación relacionada a la estructura del catálogo.

 2- Se actualizó la función newCatalog() para que sea posible añadir la información de los artistas.

 3- Se definieron las siguientes funciones:
   -> new_artist().
   -> add_artist().

 4- Se eliminó el map "Medium" del catálogo.

 5-  


##--##--##  Controller  ##--##--##

 1- Se definieron las siguientes funciones:
   -> init_catalog().
   -> load_data().
   -> load_artists().
   -> load_artworks().


##--##--##  View  ##--##--##
 
 1- Se definieron las siguientes funciones:
   -> print_menu().
   -> init_catalog().
   -> load_data().

 2- Se actualizó el iteración indefinida para que notificara error en caso de que el usuario ingrese opciones inválidas.

 3- Se modificó el código de la iteración indefinida para que se pudisese cargar la información al catálogo.


#####-----#####-----#####-----#####   #---#---#   #####-----#####-----#####-----#####
#####-----#####-----#####-----#####   PENDIENTE   #####-----#####-----#####-----#####
#####-----#####-----#####-----#####   #---#---#   #####-----#####-----#####-----#####


##--##--##  Dudas  ##--##--##
 1- ¿Por qué sale un error de recursión al intentar imprimir la lista de artistas implementada como una lista enlazada?


##--##--##  Model  ##--##--##

 1- De la función newCatalog(), determinar si es más conveniente implementar las listas de las obras y de los artistas como una lista enlazada o como un arreglo. Además, hay que añadir las funciones de comparación de cada uno.


##--##--##  Controller  ##--##--##

 1- Añadir a la función init_catalog() las funciones que permitirán añadir los maps del catalogo.