

#Ejercicio 15.9.8. Una lista doblemente enlazada es una lista en la cual cada nodo tiene una
#referencia al anterior además de al próximo de modo que es posible recorrerla en ambas direcciones.
#Escribir la clase ListaDobleEnlazada, incluyendo los métodos insert, append, remove
#y pop.

class Nodo:
	def __init__(self,dato,prox=None,anterior=None):
		self.dato = dato
		self.anterior = anterior
		self.prox = prox

class ListaDoblementeEnlazada:
	def __init__(self):
		self.inicio = None
		self.final = None
		self.len = 0
	def append(self,dato):
		nodo = Nodo(dato)
		if self.inicio is None:
			self.inicio = nodo
			self.final = self.inicio
		else:
			nodo.anterior = self.final
			self.final.prox = nodo
			self.final = nodo
		self.len += 1
	def esta_vacia(self):
		return self.len == 0
	def insert(self,dato,posicion):
		if posicion < 0 or (posicion != 0 and posicion >= self.len):
			raise IndexError("La posicion es invalida")
		nuevo_nodo = Nodo(dato)
		if posicion == 0:
			if self.inicio is None:
				self.inicio = nuevo_nodo
				self.final = self.inicio
			else:
				nuevo_nodo.prox = self.inicio
				self.inicio.anterior = nuevo_nodo
				self.inicio = nuevo_nodo
		else:
			nodo_aux = self.inicio
			for pos in range(0,posicion-1):
				nodo_aux = nodo_aux.prox
			nuevo_nodo.anterior = nodo_aux
			nuevo_nodo.prox = nodo_aux.prox
			nodo_prox = nodo_aux.prox
			nodo_aux.prox = nuevo_nodo
			nodo_prox.anterior = nuevo_nodo
		self.len += 1
	def pop(self,i=None):
		if self.esta_vacia():
			raise IndexError("Lista Vacia")
		if i is None:
			nodo_ultimo = self.final
			dato = nodo_ultimo.dato
			if nodo_ultimo.anterior is not None:
				nodo_anterior = nodo_ultimo.anterior
				self.final = nodo_anterior
				nodo_ultimo.anterior = None
				nodo_anterior.prox = None
			else:
				self.final = None
				self.inicio = None
			self.len -= 1
			return dato
		if i<0 or i>self.len:
			raise IndexError("La posicion a eliminar es invalida")
		if i == 0:
			nodo_aux = self.inicio
			nodo_prox = nodo_aux.prox
			self.inicio = nodo_aux.prox
			nodo_aux.prox = None
			nodo_prox.anterior = None
			dato = nodo_aux.dato
		else:
			nodo_act = self.inicio
			for pos in range(0,i):
				nodo_act = nodo_act.prox
			dato = nodo_act.dato
			nodo_ant = nodo_act.anterior
			if nodo_act.prox is not None:
				nodo_prox = nodo_act.prox
				nodo_ant.prox = nodo_prox
				nodo_prox.anterior = nodo_ant
				nodo_act.anterior = None
				nodo_act.prox = None
			else:
				nodo_ultimo = self.final
				dato = nodo_ultimo.dato
				if nodo_ultimo.anterior is not None:
					nodo_anterior = nodo_ultimo.anterior
					self.final = nodo_anterior
					nodo_ultimo.anterior = None
					nodo_anterior.prox = None
				else:
					self.final = None
					self.inicio = None
		self.len -= 1
		return dato
	def remove(self,elemento):
		nodo_aux = self.inicio
		index = 0
		while nodo_aux.dato != elemento and  nodo_aux is not None:
			index += 1
			nodo_aux = nodo_aux.prox
		if nodo_aux.dato == elemento:
			return self.pop(index)
		else:
			raise IndexError("El elemento no esta en la lista")
	def mostrar(self):
		nodo_aux = self.inicio
		while nodo_aux:
			print(nodo_aux.dato)
			nodo_aux = nodo_aux.prox

lista = ListaDoblementeEnlazada()
print("Inserto elementos")
lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)
lista.insert(7,1)
lista.mostrar()
print("Elimino por nombre")
lista.remove(4)
lista.mostrar()

