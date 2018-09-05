"""archivo = open("archivo2","r")
contenido = archivo.readlines()
for linea in contenido:
	#print(linea)
# Escritura """
archivo2 = open("archivo3.txt","r+")
cadena2 = "\nLinea3"
arregloCadenas = ["\nLinea4","\nLinea5"]
print(archivo2.read())
archivo2.write(cadena2)
archivo2.writelines(arregloCadenas)
archivo2.close()






 