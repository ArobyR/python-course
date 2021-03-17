try:
    fic = open("archivo.txt", "r")

    # print(fic.read(5)) solo lee 5 caracteres
    
    # lineas completas 
    print(fic.readline())
except Exception as e:
    print(e)
finally:
    fic.close()