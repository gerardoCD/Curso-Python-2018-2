from fbchat import Client
from fbchat.models import *
import time, getpass
correo = input("Ingresa tu correo: ")
passa = getpass.getpass("Contraseña")
client = Client(correo,passa)

client.send(Message(text='Hola XD'), thread_id=100001336376535, thread_type=ThreadType.USER)
client.logout()