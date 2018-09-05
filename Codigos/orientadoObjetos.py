




class SerVivo:
	tieneVida = True
	def respirar(self):
		print("Estoy respirando")
	def reproducir(self):
		print("Me estoy reprodiciendo")

class Persona(SerVivo):
	altura = 0.0
	genero = ""
	colorCabello = ""
	tatuajes = False
	complexion = ""
	def __init__(self,altura,genero,colorCabello,tatuajes):
		print("Se ejecuta este codigo")
		self.altura = altura
		self.genero = genero
		self.colorCabello = colorCabello
		self.tatuajes = tatuajes
	def corre(self):
		print("Estoy corriendo")
	def escribir(self):
		print("Estoy escribiendo")

class Mujer(Persona):
	def multitask():
		print("Ejecutando dos tareas a la vez")



Humano1 = Persona(1.70,"M","Cafe",True)
Humano2 = Persona(1.89,"M","Azul",False)
Humano1.complexion = "Ectomorfo"
#Humano1.altura = 1.70
#Humano1.genero = "M"
#Humano1.colorCabello = "Cafe"
#Humano1.tatuajes = True
#Humano1.complexion = "Ectomorfo"

print(Humano1.altura)
print(Humano1.genero)
print(Humano1.colorCabello)
print(Humano1.complexion)
print(Humano1.corre())
print(Humano1.tieneVida)
print(Humano1.respirar())
print(Humano1.reproducir())
#print(Humano1.escribir())

Mujer1 = Mujer(1.70,"F","Cafe",True)
Mujer1.tieneVida = False
print("\n\n")
print(Mujer1.tieneVida)
print("\n\n")
print(Mujer.tieneVida)

#Polimorfismo 

class Gato:
	def rugir(self):
		print("El gato maulla")

class Perro:
	def rugir(self):
		print("El perro ladra")

def rugir(animal):
	animal.rugir()

perro = Perro()
gato = Gato()
rugir(gato)


# Encapsulamiento 
class Ejemplo:
	def __init__(self):
		self.publico = "variable publica"
		self.__privado = "Variable privada"
	def getVariable(self):
		return self.__privado



ejemplo1 = Ejemplo()
#print(ejemplo1.publico)
variable = ejemplo1.getVariable
print(variable)


usuarios= {"usuario":Humano1,"usuario2":Humano2}