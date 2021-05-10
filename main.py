#Escribir en un archivo

archivo = open(input("Dame el nombre del archivo: ") + ".txt", 'w')

archivo.write("Hola")