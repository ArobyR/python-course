import os
from servicio.catalogo_pelicula import CatalogoPelicula
from dominio.pelicula import Pelicula 

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

run_time = True


while run_time:
    print(""" \tMenu de opciones:\n
          1) Agregar pelicula\n
          2) Listar pelicula\n
          3) Eliminar catalogo de peliculas\n
          4) Salir\n
          """)
    option = (input("Introduce una opcion: "))
    
    if option == "1":
        nombre_pelicula = input("Introduce el nombre de la pelicula: ")
        pelicula = Pelicula()
        pelicula.set_nombre_pelicula(nombre_pelicula)
        CatalogoPelicula.agregar_pelicula(pelicula)
    
    if option == "2":
        clear_console()
        CatalogoPelicula.listar_peliculas()
        
    if option == "3":
        CatalogoPelicula.eliminar_catalogo()
    
    if option == "4":
        clear_console()
        break