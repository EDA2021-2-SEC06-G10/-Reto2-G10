Integrantes:
 <> José Nicolás Cárdenas - 201922006 - j.cardenast@uniandes.edu.co
 <> Andrés Leonardo Beltran - 202014143 - al.beltran@uniandes.edu.co

Requerimientos:
 Req. 3 - Andrés Leonardo Beltrán
 Req. 4 - José Nicolás Cárdenas



#####-----#####-----#####   Modificaciones   #####-----#####-----#####


##--##--##  General  ##--##--##

 1- Se añadió la carpeta de datos (MoMA) al repositorio.


##--##--##  Model  ##--##--##

 1- Se actualizó la documentación relacionada a la estructura del catálogo.

 2- Se creó la función newCatalog():
    > Se creó la lista enlazada que guardará la información de las obras.
    > Se creó el índice que permitirá identificar los medios o técncias de lass obras.

 3- Se definió la función de creación función new_artwork().

 4- Se definieron las funciones de adición add_artwork() y add_medium().



#####-----#####-----#####   Pendiente   #####-----#####-----#####


##--##--##  Model  ##--##--##

 1- De la función newCatalog():
    > Actualizar el cuerpo para poder guardar la información de los artistas.
    > Añadir las funciones de comparación de la lista 'artworks' y el map 'Medium'.

 2- De la función add_medium(), añadir bloque de código para añadir obra si la técnica ya existe.

 3- Implementar el código que permita realizar el siguiente requerimiento: “las n obras más antiguas para un medio específico”.