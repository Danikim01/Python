import random

#Se usaran las funciones "ord" y "chr"

#print(ord('a'),ord('z'))
#print(ord('A'),ord('Z'))
#print(chr(97),chr(122))
#print(chr(65),chr(90))

#Crear una funcion que genere una contraseña de 8 caracteres al azar : 1 caracter en mayuscula, 1 en minuscula
#1 caracter especial, y 5 digitos

def generar_contraseña():
	l = ['@','#','$','&']
	mayuscula = chr(random.randint(65,90))
	minuscula = chr(random.randint(97,122))
	especial = random.choice(l)
	digitos = str(random.randint(10000,99999))
	return mayuscula+minuscula+especial+digitos

contraseña_1 = generar_contraseña()
#print(contraseña_1)

#Ahora quiero crear una funcion que tambien genere una contraseña de 8 caracteres pero que sea de un largo que le pase
#el usuario por parametro (para ello uso la funcion random.sample(...)->lo cual devuelve una lista), por ejemplo:

def generar_contraseña_de_largo_n(largo):
	l = ['@','#','$','&']
	mayuscula = chr(random.randint(65,90))
	minuscula = chr(random.randint(97,122))
	especial = random.choice(l)
	digitos = str(random.randint(10000,99999))
	contraseña = mayuscula+minuscula+especial+digitos
	#La funcion random.sample devuelve una lista
	lista = random.sample(contraseña,largo)
	string_retorno = ("").join(lista)
	return string_retorno

#Pre condicion : El largo de la contraseña tiene que ser menor o igual a 8.
#Largo 8 :
#print(generar_contraseña_de_largo_n(8))
#Largo 6:
#print(generar_contraseña_de_largo_n(6))

#En caso de que no me pasen ningun valor puede especificar yo una variable por defecto
#de esta forma:

def generar_contraseña_de_largo_n_2(largo=8):
	l = ['@','#','$','&']
	mayuscula = chr(random.randint(65,90))
	minuscula = chr(random.randint(97,122))
	especial = random.choice(l)
	digitos = str(random.randint(10000,99999))
	contraseña = mayuscula+minuscula+especial+digitos
	#La funcion random.sample devuelve una lista
	lista = random.sample(contraseña,largo)
	string_retorno = ("").join(lista)
	return string_retorno

#print(generar_contraseña_de_largo_n_2(1))

#Quiero crear una funcion que valide un usuario y una contraseña


def validate(username,password):
	if username == "ABC" and password == "Abc@123":
		print("Contraseña valida")
	else:
		print("Contraseña invalida")

#En las funciones puedo enviar los parametros de 2 formas:
validate("ABC","Abc@123")
#o asi
validate(password="Abc@123",username="ABC")

##Tambien, en python, se pueden hacer cosas ilegales como estas

##Por defecto el print establece la coma como separador entre cosas que quieras imprimir
# y el final como un \n:
print(100,200)
print("Hi")
##Esto deberia imprimir:
# 100 200
# "Hi"

##Pero se pueden hacer cosas como estas
print(100,200,sep=",",end=" ")
print("Hi")
#Esto imprime:
# 100,200 Hi
