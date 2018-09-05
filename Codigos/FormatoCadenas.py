cadena = "Este es el Curso de Python"
print(len(cadena))
print(cadena[1])
print(cadena[11:16])
print(cadena[:20])
print(cadena[::])
#Formato de cadena
print(cadena.upper())
print(cadena.lower())
print(cadena.swapcase())
print(cadena.title())
print(cadena.capitalize())
print(cadena.center(70,"*")) ## Investigar 
print(cadena.count("Pytho"))

#Ciclos
listaUsuarios = []
#Leer de teclado
usuario = input("Ingresa tu usuario: ")
listaUsuarios.append(usuario)
print(listaUsuarios)

#Ciclo while
contador = 0
while(contador < 10):
	print("El contador tiene el valor de: ", contador)
	contador+=1






