
#Para cada cuenta de banco, tenemos:
##Datos:
#cust id
#name
#balance

##Acciones
#deposite
#withdraw

#Para crear una estructura se hace:
class Account:
	#Si quiero que cada vez que se cree una cuenta de banco
	#incremento el contador, puedo hacer lo siguiente:
	count = 0

	@classmethod
	def incr_count(cls):
		cls.count += 1

	@classmethod
	def get_count(cls):
		return cls.count

	@staticmethod
	def print_Val():
		print("Static mehod in account class")




	def __init__(self,customer_id,name,initial_balance=0):
		self.__id = customer_id
		self.__name = name
		self.__balance = initial_balance
		#Account.count += 1
		Account.incr_count()
	def get_balance(self):
		return self.__balance
	def get_name(self):
		return self.__name
	def get_id(self):
		return self.__id
	def deposite(self,ammount):
		self.__balance += ammount
		return self.__balance
	def withdraw(self,ammount):
		if ammount > self.__balance:
			return "Te quedaste pobre michi"
		self.__balance -= ammount
		return self.__balance


customer1 = Account("101","ABC")
#print(customer1)

##Como acceder a cada variable aunque haya __variable (si hay __por delante de una variabe)
#es convencion que no se puede acceder al struct

#pero puedo acceder asi de todas formas:

#print(customer1._Account__id)

#y para acceder a todos los datos

#print(customer1.__dict__,type(customer1.__dict__))

customer2 = Account("102","XYZ")
#print(customer2)

customer3 = Account("103","PQR")
#print(customer3)

#print(customer1.id,customer1.name,customer1.balance)

#print(customer1.get_balance())
#print(customer1.deposite(50000))
#print(customer2.get_balance())
#print(customer1.withdraw(60000))

customer4 = Account("104","QWE")

customer2.deposite(8000)
customer3.deposite(7000)
customer4.deposite(70000)

#l = [customer1, customer2, customer3, customer4]

#for obj in l:
#	if obj.get_balance() < 10000:
#		print(obj.get_id(),obj.get_name())


#print("La cantidad de cuentas que se crearon son {}".format(Account.count))
#print(customer1.count)
#print(customer2.count)
#Account.count += 5
#print("La cantidad de cuentas que se crearon son {}".format(Account.count))
#print(customer1.count)
#print(customer2.count)

#customer1.count = 100
#print(Account.count)
#print(customer1.__dict__)

#print(Account.get_count())

#Account.print_Val()

##Inheritance


class Saving_Account(Account):
	def __init__(self,id,name,initial_bal=0):
		super().__init__(id,name,initial_bal)
		#Describe un limite de dinero que puedo extraer al dia (supongamos)
		self.limit = 50000

	def withdraw_2(self,ammount):
		if ammount < self.limit:
			new_balance = super().withdraw(ammount)
			self.limit -= ammount
			return new_balance
		else:
			print("Daily limite reached")

cust1 = Saving_Account(101,"ABC")
#print(cust1.__dict__)
print(cust1.deposite(80000))
print(cust1.withdraw_2(40000))
print(cust1.withdraw_2(40000))

##Multiple inheritance

class A:
	pass
class B:
	pass
class C(A,B):
	pass

obj = C()
#help(obj)
class A:
	pass
class B:
	pass
class C(B,A):
	pass


obj = C()
#help(obj)

def validar_numero(valor):
	if not isinstance(valor, (int, float, complex)):
		raise TypeError("{} no es un valor numérico".format(valor))
	return valor

class Punto:
	def __init__(self,x,y):
		self.x = validar_numero(x)
		self.y = validar_numero(y)
	def restar(self,otro):
		return Punto(self.x-otro.x,self.y-otro.y)
	def norma(self):
		return (self.x**2+self.y**2)**(1/2)
	def distancia(self,otro):
		return self.restar(otro).norma()
	def __repr__(self):
		return ("{},{}".format(self.x,self.y))
	def __add__(self,otro):
		return ("({})".format(Punto(self.x+otro.x,self.y+otro.y)))
	def __sub__(self,otro):
		return ("({})".format(Punto(self.x-otro.x,self.y-otro.y)))
	def __eq__(self,otro):
		return (self.x == otro.x and self.y == otro.y)

p = Punto(5,7)
q = Punto(2,3)
#print(p.distancia(q))
#print(repr(p),type(repr(p)))
print(p+q,p-q,type(p+q),type(p-q))


def validar_numero_positivo(numero):
	if (not isinstance(numero, (int, float, complex))) or (numero<=0):
		raise TypeError("Reingrese un valor numerico positivo")
	return numero

def validar_cadena_no_vacia(cadena):
	if not isinstance(cadena,(str)):
		raise TypeError("{} no es un string".format(cadena))
	elif cadena == "" or cadena == '':
		raise TypeError("La cadena esta vacia, por favor ingrese algo")
	return cadena

class Hotel:
	def __init__(self,nombre,ubicacion,puntaje,precio):
		self.nombre = validar_cadena_no_vacia(nombre)
		self.ubicacion = validar_cadena_no_vacia(ubicacion)
		self.puntaje = validar_numero_positivo(puntaje)
		self.precio = validar_numero_positivo(precio)
	def __str__(self):
		return "{} de {} - Puntaje: {} - Precio: {} pesos".format(
			self.nombre,
			self.ubicacion,
			self.puntaje,
			self.precio
			)
	def ratio(self):
		return ((self.puntaje**2)*10/self.precio)
	#Metodo "less than" devuelve true si self es comparativamente menor a otro hotel.
	def __lt__(self,otro):
		return self.ratio() < otro.ratio()
	def precio(self):
		return self.precio

h = Hotel("Hotel City","Mercedes",3.2,20)
i = Hotel("Hotel Mascardi","Bariloche",6,150)
#print(i>h,i<h)

##Como ordenar una lista de hoteles
h1 = Hotel("Hotel 1* normal", "MDQ", 1, 10)
h2 = Hotel("Hotel 2* normal", "MDQ", 2, 40)
h3 = Hotel("Hotel 3* carisimo", "MDQ", 3, 130)
h4 = Hotel("Hotel vale la pena","MDQ", 4, 130)
lista = [h1, h2, h3, h4]
#lista.sort()
#Al aplicar lista.sort() se ordena segun el metodo definido en def __lt__(self,...) dentro de la clase Hotel
#for hotel in lista:
#	print(hotel)

#Otra forma de ordenar sin usar el metodo def __lt__ es haciendo
lista.sort(key=Hotel.precio) #o se puede hacer lista.sort(key=Hotel.ratio) si se quiere
for hotel in lista:
	print(hotel)

#Otras formas de comparacion:

p = Punto(3,4)
q = Punto(3,4)
#print(p==q)

#Ejercicio 14.9.1. Mejorar la clase Rectangulo, agregando métodos para calcular las dimensiones
#alto y ancho, y las coordenadas del punto central.

def verificar_relacion(noroeste,sudeste):
	if noroeste.y > sudeste.y and noroeste.x < sudeste.x:
		return True
	return False

class Rectangulo:
	#Representa un rectangulo en el plano
	def __init__(self,noroeste,sudeste):
		if(verificar_relacion(noroeste,sudeste)==False):
			raise TypeError("Las coordenadas no cumplen con lo pedido")
		self.noroeste = noroeste
		self.sudeste = sudeste
	def calcular_ancho(self):
		return self.sudeste.x - self.noroeste.x
	def calcular_alto(self):
		return self.noroeste.y - self.sudeste.y
	def coordenada_central(self):
		return Punto((self.noroeste.x+self.sudeste.x)/2,(self.noroeste.y+self.sudeste.y)/2)


p = Punto(3,5)
q = Punto(7,3)
r = Rectangulo(p,q)
c = r.coordenada_central()
print("El alto del rectangulo es {}".format(r.calcular_alto()))
print("El ancho del rectangulo es {}".format(r.calcular_ancho()))
print(c)

def encontrar_divisor_comun(dividendo,divisor):
	divisor_comun = 1
	for value in range(2,10):
		if dividendo%value == 0 and divisor%value == 0:
			return value
	return divisor_comun

class Fraccion:
	def __init__(self,dividendo,divisor):
		self.dividendo = dividendo
		self.divisor = divisor
	def __add__(self,otro):
		return (self.dividendo/self.divisor + otro.dividendo/otro.divisor)
	def __mul__(self,otro):
		return (self.dividendo/self.divisor * otro.dividendo/otro.divisor)
	def simplificar(self):
		divisor = encontrar_divisor_comun(self.dividendo,self.divisor)
		if divisor == 1:
			print("No se puede simplificar brother")
			return Fraccion(self.dividendo,self.divisor)
		while(self.dividendo%divisor == 0 and self.divisor%divisor==0 and divisor != 1):
			self.dividendo = self.dividendo/divisor
			self.divisor = self.divisor/divisor
			divisor = encontrar_divisor_comun(self.dividendo,self.divisor)

	def __str__(self):
		return "{}/{}".format((self.dividendo),(self.divisor))

p = Fraccion(3,4)
q = Fraccion(5,4)
z = p*q
#print(z)

k = Fraccion(5,5)
k.simplificar()
print(k)