
#<> 

def es_primo(dato_numerico):
	if dato_numerico == 1:
		return False
	for divisor in range(2,dato_numerico):
		if dato_numerico%divisor == 0:
			return False
	return True

class Nodo:
	def __init__(self,dato,prox=None):
		self.dato = dato
		self.prox = prox
	def __str__(self):
		return "{}".format(self.dato)

class ListaEnlazada:
	def __init__(self):
		self.primero = None
		self.cantidad_nodos = 0
	def insert(self,dato,posicion):
		if posicion < 0 or posicion > self.cantidad_nodos:
			raise IndexError("La posicion es invalida")
		nuevo_nodo = Nodo(dato)
		if posicion == 0:
			nuevo_nodo.prox = self.primero
			self.primero = nuevo_nodo
		else:
			nodo_actual = self.primero
			for value in range(0,posicion-1):
				nodo_actual = nodo_actual.prox
			nuevo_nodo.prox = nodo_actual.prox
			nodo_actual.prox = nuevo_nodo
			
		self.cantidad_nodos += 1
	def pop(self,i=None):
		if i is None:
			i = self.cantidad_nodos-1
		if i<0 or i>self.cantidad_nodos:
			raise IndexError("La posicion a eliminar es invalida")
		if i == 0:
			dato = self.primero.dato
			self.primero = self.primero.prox
		else:
			nodo_anterior = self.primero
			nodo_actual = nodo_anterior.prox
			for pos in range(0,i-1):
				nodo_anterior = nodo_actual
				nodo_actual = nodo_actual.prox
			dato = nodo_actual.dato
			nodo_anterior.prox = nodo_actual.prox
		self.cantidad_nodos -= 1
		return dato

	def remove(self,x):
		if self.cantidad_nodos == 0:
			raise ValueError("La lista esta vacia")

		if self.primero.dato == x:
			#Eliminar el primer elemento
			self.primero = self.primero.prox
		else:
			#El elemento a eliminar no es el primero
			nodo_anterior = self.primero
			nodo_actual = nodo_anterior.prox
			while nodo_actual.dato != x and nodo_actual is not None:
				nodo_anterior = nodo_actual
				nodo_actual = nodo_actual.prox

			if nodo_actual is None:
				ValueError("El valor no está en la lista.")

			nodo_anterior.prox = nodo_actual.prox

		self.cantidad_nodos -= 1
	
	def append(self,dato):
		nuevo_nodo = Nodo(dato)
		if self.cantidad_nodos == 0:
			nuevo_nodo.prox = self.primero
			self.primero = nuevo_nodo
		else:
			nodo = self.primero
			for value in range(0,self.cantidad_nodos-1):
				nodo = nodo.prox
			nodo.prox = nuevo_nodo
		self.cantidad_nodos += 1

	def extend(self,lista_enlazada):
		cant_elementos = lista_enlazada.cantidad_nodos
		nodo_aux = lista_enlazada.primero
		while nodo_aux is not None:
			self.append(nodo_aux)
			nodo_aux = nodo_aux.prox

	def remover_todos(self,elemento):
		cant_removidos = 0
		while self.primero is not None and self.primero.dato == elemento:
				self.primero = self.primero.prox
				cant_removidos += 1

		if self.primero is None:
			print("Todos los elementos fueron borrados")
			return

		nodo_anterior = self.primero
		nodo_actual = nodo_anterior.prox

		while nodo_actual is not None:
			if nodo_actual.dato == elemento:
				nodo_anterior.prox = nodo_actual.prox
				cant_removidos += 1
				nodo_actual = nodo_actual.prox
				continue
			nodo_anterior = nodo_actual
			nodo_actual = nodo_actual.prox
		print("La cantidad de elementos removidos son {}".format(cant_removidos))
		return cant_removidos
		
	def mostrar_elementos(self):
		if self.cantidad_nodos == 0:
			print("La lista esta vacia")
			return
		aux = self.primero
		while aux:
			print(aux.dato)
			if(aux.dato is None):
				print("No hay nada")
			aux = aux.prox
	def duplicar(self,elemento):
		nodo = self.primero
		index = 0
		while nodo is not None:
			if nodo.dato == elemento:
				self.insert(elemento,index)
				index += 1
			index += 1
			nodo = nodo.prox
	def filter(self,funcion):
		if self.cantidad_nodos == 0:
			print("Lista vacia")
			return
		lista_aux = ListaEnlazada()
		nodo_original = self.primero
		nodo_previo = None
		while nodo_original:
			if funcion(nodo_original.dato) == True:
				nuevo_nodo = Nodo(nodo_original.dato)
				if lista_aux.primero is None:
					nuevo_nodo.prox = lista_aux.primero
					lista_aux.primero = nuevo_nodo
					previo = lista_aux.primero
					lista_aux.cantidad_nodos += 1
					nodo_original = nodo_original.prox
					continue
				previo.prox = nuevo_nodo
				siguiente = previo.prox
				previo = siguiente
			nodo_original = nodo_original.prox
		return lista_aux
	def invertir_lista(self):
		nodo_previo = None
		nodo_actual = self.primero
		while nodo_actual:
			siguiente = nodo_actual.prox
			nodo_actual.prox = nodo_previo
			nodo_previo = nodo_actual
			nodo_actual = siguiente
		self.primero = nodo_previo
			

Mi_lista = ListaEnlazada()
print("Inserto elementos")
Mi_lista.append(1)
Mi_lista.append(2)
Mi_lista.append(3)
Mi_lista.append(4)
Mi_lista.append(5)

Mi_lista.insert(7,1)
Mi_lista.insert(10,3)
Mi_lista.insert(78,2)

Mi_lista.mostrar_elementos()
print("Elimino elmentos")
Mi_lista.pop()
#Mi_lista.remover_todos(8)
#print("Invierto la lista")
#Mi_lista.invertir_lista()
Mi_lista.mostrar_elementos()


#Otra_lista = Mi_lista.filter(es_primo)
#print("Los elementos de la nueva lista son")
#Otra_lista.mostrar_elementos()

def concatenar(lista,caracter):
	string = caracter.join(map(str,lista))
	return string

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
		if posicion < 0 or posicion >= self.len:
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
		if posicion < 0 or posicion >= self.len:
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
		while (nodo_act.dato != elemento):
			nodo_act = nodo_act.prox
		if(nodo_act.dato == elemento):
			return nodo_act.dato
		else:
			raise IndexError("El elemento buscado no se encuentra en la lista")

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

Mi_lista = ListaEnlazada2()
Mi_lista.append(5)
Mi_lista.append(10)
Mi_lista.append(7)
#print(Mi_lista.mostrar())

#Mi_lista.mostrar()



class IteradorListaEnlazada:
	def __init__(self,lista_enlazada):
		self.nodo_corriente = lista_enlazada.primero
		self.lista = lista_enlazada
	def avanzar(self):
		self.nodo_corriente = self.nodo_corriente.prox
	def dato_actual(self):
		return self.nodo_corriente.dato
	def esta_al_final(self):
		return self.nodo_corriente is None



#l = ListaEnlazada()
#l.append(7)
#l.append(3)
#l.append(5)
#l.mostrar_elementos()

#it = IteradorListaEnlazada(l)
#print(it.esta_al_final())

#print(it.dato_actual())

#it.avanzar()
#print(it.esta_al_final())

#print(it.dato_actual())

#it.avanzar()
#print(it.esta_al_final())

#print(it.dato_actual())

#it.avanzar()
#print(it.esta_al_final())

