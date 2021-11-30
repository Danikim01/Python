from heap import HeapMinimal

class ColaConPrioridad:
	def __init__(self,comparador):
		self.cola = HeapMinimal(comparador)
		self.tope = 0
	def encolar(self,elemento):
		self.cola.heap_insertar(elemento)
		self.tope += 1
	def desencolar(self):
		if self.cola_vacia():
			raise TypeError("Cola con prioridad vacia")
		extraido = self.cola.heap_extraer_raiz()
		self.tope -= 1
		return extraido
	def cola_vacia(self):
		return self.cola.heap_vacio() and self.tope == 0
	def mostrar_cola(self):
		self.cola.heap_mostrar()