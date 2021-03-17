import os

class CatalogoPelicula:
    
    ruta_archivo = "peliculas.txt"
    
    @staticmethod
    def agregar_pelicula(obj_pelicula):
        try:
            fich = open(CatalogoPelicula.ruta_archivo, "a")
            fich.write(obj_pelicula.get_nombre_pelicula() + "\n")
        except Exception as e:
            print("Hubo un error:", e)
        finally:
            fich.close()
    
    @staticmethod
    def listar_peliculas():
        try:
            fich = open(CatalogoPelicula.ruta_archivo, "r")
            print(f"Listado:\n {fich.read()}")
        except Exception:
            fich = open(CatalogoPelicula.ruta_archivo, "w")
            print(f"Listado:\n {fich.read()}")
        finally:
            fich.close()
    
    @staticmethod
    def eliminar_catalogo():
        try:
            os.remove(CatalogoPelicula.ruta_archivo)
        except Exception as e:
            print("ERROR:", e)
            
    def __init__(self):
        pass