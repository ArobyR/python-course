""" copy file """
try:
    fich = open("archivo.txt", "r")
    fich2 = open("archivo2.txt", "w")
    
    fich2.write(fich.read())
    
except Exception as e:
    print(e)
finally:
    fich.close()
    fich2.close()