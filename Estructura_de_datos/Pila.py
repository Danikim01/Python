
##Ejercicio 1:

def concatenar(lista,caracter):
	string = caracter.join(map(str,lista))
	return string

class Nodo:
	def __init__(self,dato):
		self.dato = dato
		self.prox = None

class ListaEnlazada2:
	def __init__(self):
		self.inicio = None
		self.final = None
		self.len = 0
	def append(self,dato):
		nodo_nuevo = Nodo(dato)
		if self.len == 0:
			nodo_nuevo.prox = self.inicio
			self.inicio = nodo_nuevo
			self.final = nodo_nuevo
		else:
			nodo_aux = self.final
			nodo_aux.prox = nodo_nuevo
			self.final = nodo_nuevo
		self.len += 1
	def remove(self,dato):
		if self.len == 0:
			raise TypeError("Lista vacia")
		if self.inicio.dato == dato:
			self.inicio = self.inicio.prox
		else:
			nodo_ant = self.inicio
			nodo_act = nodo_ant.prox
			nodo_aux = None
			while nodo_act.dato != dato and nodo_act is not None:
				nodo_aux = nodo_ant
				nodo_ant = nodo_act
				nodo_act = nodo_act.prox
			if nodo_act is None:
				if nodo_ant.dato == dato:
					nodo_aux.prox = None
					self.final = nodo_aux
					self.len -= 1
					print("El nodo final es {}".format(self.final.dato))
					return
				else:
					raise IndexError("El elemento no esta en la lista")
			if nodo_act == self.final:
				self.final = nodo_ant
				nodo_ant.prox = None
				self.len -= 1
				return
			nodo_ant.prox = nodo_act.prox
		print("El nodo final es {}".format(self.final.dato))
		self.len -= 1
	def insertar_en_posicion(self,posicion,dato):
		if posicion < 0 or posicion > self.len:
			raise TypeError("Posicion invalida")
		nuevo_nodo = Nodo(dato)
		if posicion == 0:
			nuevo_nodo.prox = self.inicio
			self.inicio = nuevo_nodo
		else:
			nodo_aux = self.inicio
			for pos in range(0,posicion-1):
				nodo_aux = nodo_aux.prox
			nuevo_nodo.prox = nodo_aux.prox
			nodo_aux.prox = nuevo_nodo
		self.len += 1
	def remover_en_posicion(self,posicion):
		if posicion < 0 or posicion > self.len:
			raise TypeError("Posicion invalida")
		if posicion == 0:
			elemento = self.inicio
			self.inicio = self.inicio.prox
		else:
			nodo_ant = self.inicio
			nodo_act = nodo_ant.prox
			for pos in range(0,posicion-1):
				nodo_ant = nodo_act
				nodo_act = nodo_act.prox
			elemento = nodo_act
			if nodo_act is self.final:
				nodo_ant.prox = None
				self.final = nodo_ant
			else:
				nodo_ant.prox = nodo_act.prox
		self.len -= 1
		return elemento
	def esta_vacia(self):
		return self.len == 0
	def obtener_elemento(self,elemento):
		if self.esta_vacia():
			raise IndexError("Lista vacia")
		nodo_act = self.inicio
		while (nodo_act):
			if(nodo_act.dato == elemento):
				return nodo_act.dato
			nodo_act = nodo_act.prox
		if(nodo_act is None):
			raise IndexError("Elemento no encontrado")
	
	def mostrar(self):
		if self.len == 0:
			print("La lista esta vacia")
			return
		lista = []
		aux = self.inicio
		while aux:
			lista.append(aux.dato)
			aux = aux.prox
		string = concatenar(lista,",")
		return string

class Avion:
	def __init__(self,nombre):
		self.nombre = nombre

class TorreDeControl:
	def __init__(self):
		self.cola_aterrizaje = ListaEnlazada2()
		self.cola_despegue = ListaEnlazada2()
	def nuevo_arribo(self,nombre_avion):
		avion = Avion(nombre_avion)
		self.cola_aterrizaje.append(avion.nombre)
	def nueva_partida(self,nombre_avion):
		avion = Avion(nombre_avion)
		self.cola_despegue.append(avion.nombre)
	def asignar_pista(self):
		if(self.cola_aterrizaje.esta_vacia() == False):
			print("El vuelo {} aterrizo con exito".format(self.cola_aterrizaje.remover_en_posicion(0).dato))
		elif (self.cola_despegue.esta_vacia() == False):
			print("El vuelo {} despegó con exito".format(self.cola_despegue.remover_en_posicion(0).dato))
		else:
			print("No hay vuelos en la espera")
	def ver_estado(self):
		print("Vuelos esperando para aterrizar : {}".format(self.cola_aterrizaje.mostrar()))
		print("Vuelos esperando para despegar : {}".format(self.cola_despegue.mostrar()))
		
##Ejercicio 2:

class Impresora:
	def __init__(self,nombre,cantidad_tinta=0):
		self.nombre = nombre
		self.cantidad_tinta = cantidad_tinta
		self.documentos = ListaEnlazada2()
	def encolar(self,nombre):
		self.documentos.append(nombre)
	def imprimir(self):
		if self.documentos.esta_vacia():
			raise IndexError("No hay documentos para imprimir")
		if self.cantidad_tinta < 10:
			raise IndexError("No hay tinta suficiente anda a comprar")
		print(self.documentos.mostrar())
		self.cantidad_tinta -= 1
	def cargar_tinta():
		while self.cantidad_tinta < 10:
			self.cantidad_tinta += 1

class Oficina:
	def __init__(self):
		self.impresoras = ListaEnlazada2()
	def agregar_impresora(self,impresora_a_agregar):
		self.impresoras.append(impresora_a_agregar)
	def impresora(self,nombre):
		if self.impresoras.esta_vacia():
			raise IndexError("Lista vacia")
		nodo_act = self.impresoras.inicio
		while (nodo_act):
			if(nodo_act.dato.nombre == nombre):
				return nodo_act.dato
			nodo_act = nodo_act.prox
		if(nodo_act is None):
			raise IndexError("Elemento no encontrado")

	def quitar_impresora(self,nombre):
		self.impresoras.remove(nombre)
	def obtener_impresora_libre(self):
		impresora_actual = self.impresoras.inicio
		impresora_prox = impresora_actual.prox
		while(impresora_prox):
			if(impresora_prox.dato.documentos.len < impresora_actual.dato.documentos.len ):
				impresora_actual = impresora_prox

			impresora_prox = impresora_prox.prox
		return impresora_actual.dato

class Carta:
	def __init__(self,valor,palo):
		self.valor = valor
		self.palo = palo
class Solitario:
	def __init__(self):
		self.pila = ListaEnlazada2()
	def obtener_tope(self):
		if(self.pila.esta_vacia()):
			raise IndexError("Esta vacia")
		return self.pila.final.dato
	def apilado_especial(self,carta):
		tope_carta = obtener_tope(carta)
		if(carta.valor < tope_carta.valor and carta.palo != tope_carta.palo):
			self.pila.append(carta)
		else:
			raise IndexError("NO se puede apilar")




class PilaConMaximo:
	def __init__(self):
		self.items = []
	def apilar(self,x):
		self.items.append(x)
	def desapilar(self):
		return self.items.pop()
	def esta_vacia(self):
		return len(self.items) == 0
	def mostrar(self):
		for valor in self.items:
			print(valor)
	def devolver_copia(self,lista_nueva):
		for value in self.items:
			lista_nueva.apilar(value)
	def obtener_max(self):
		pila_aux = PilaConMaximo()
		self.devolver_copia(pila_aux)

		elemento = pila_aux.desapilar()
		while(pila_aux.esta_vacia() == False):
			anterior = pila_aux.desapilar()
			if(anterior < elemento):
				anterior = elemento
			elemento = anterior
		return anterior

pila = PilaConMaximo()
pila.apilar(5)
pila.apilar(8)
pila.apilar(12)
pila.apilar(3)

print("El maximo es",pila.obtener_max())

pila.mostrar()

