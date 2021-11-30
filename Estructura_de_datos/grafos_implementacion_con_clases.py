class Pila:
	def __init__(self):
		self.items = []
	def apilar(self,x):
		self.items.append(x)
	def desapilar(self):
		return self.items.pop()
	def esta_vacia(self):
		return len(self.items) == 0
	def mostrar(self):
		lista = []
		for valor in self.items:
			lista.append(valor.dato)
		print("Estado de la pila: ",lista)

class Cola:
	def __init__(self):
		self.items = []
	def encolar(self,x):
		self.items.append(x)
	def desencolar(self):
		if self.esta_vacia():
			raise TypeError("Cola vacia")
		return self.items.pop(0)
	def esta_vacia(self):
		return len(self.items) == 0
	def mostrar(self):
		lista = []
		for valor in self.items:
			lista.append(valor.dato)
		return lista

class Vertice:
	def __init__(self,dato):
		self.dato = dato
	def dato(self):
		return self.dato

class Arista:
	def __init__(self,origen,destino,peso=0):
		self.origen = origen
		self.destino = destino
		self.peso = peso
	def peso(self):
		return self.peso
	#vertices devuelve una tupla que corresponda al origen y al destino (origen,destino)
	def vertices(self):
		return (self.origen,self.destino)
	def opuesto(self,vertice):
		if vertice==self.origen:
			return self.destino
		elif vertice==self.destino:
			return self.origen

#Implementacion de grafo no dirigido con peso 1
class Grafo_no_dirigido:
	def __init__(self):
		self.vertices = {}
	def insertar_vertice(self,dato):
		vertice = Vertice(dato)
		self.vertices[vertice] = {}
		return vertice
	def insertar_arista(self,origen,destino,peso=1):
		arista = Arista(origen,destino,peso)
		#Para que el grafo sea no dirigido:
		self.vertices[origen][destino] = arista
		self.vertices[destino][origen] = arista
	def cantidad_vertices(self):
		return (len(self.vertices.keys()))

	def retornar_arista(self,origen,destino):
		return self.vertices[origen].get(destino)

	def peso_entre(self,origen,destino):
		arista = self.retornar_arista(origen,destino)
		return arista.peso

	def cantidad_aristas(self):
		contador = 0
		for vertice in self.vertices:
			for valor in self.vertices[vertice].values():
					contador += valor.peso
		return int(contador/2)

	def adyacentes(self,vertice):
		lista = []
		for v in self.vertices[vertice]:
			lista.append(v)
		return lista

	def obtener_vertices(self):
		lista = []
		for v in self.vertices.keys():
			lista.append(v)
		return lista

	def bfs(self,origen):
		visitados = []
		cola = Cola()
		visitados.append(origen)
		cola.encolar(origen)
		while not cola.esta_vacia():
			v = cola.desencolar()
			#print("Procesando vertice: ",v.dato)
			for w in grafo.adyacentes(v):
				#print("Sus adyacentes son: ",w.dato)
				if w not in visitados:
					#print("El vertice: ",w.dato,"no fue visitado")
					visitados.append(w)
					#print("Estado de visitados: ")
					#for valor in visitados:
					#	print(valor.dato)
					cola.encolar(w)
					#print(cola.mostrar())
		return visitados
	
	def _dfs(self,origen,visitados):
		for v in self.adyacentes(origen):
			if v not in visitados:
				visitados.append(v)
				self._dfs(v,visitados)

	def dfs(self,origen):
		visitados = []
		visitados.append(origen)
		self._dfs(origen,visitados)
		return visitados

	def dfs_recorrido_completo(self):
		visitados = []
		for v in self.obtener_vertices():
			if v not in visitados:
				visitados.append(v)
				self._dfs(v,visitados)
		return visitados

	def dfs_con_pilas(self,origen):
		visitados = []
		pila = Pila()
		visitados.append(origen)
		pila.apilar(origen)
		while not pila.esta_vacia():
			v = pila.desapilar()
			for w in self.adyacentes(v):
				if w not in visitados:
					visitados.append(w)
					pila.apilar(w)
		return visitados			
	#Devuelve las aristas incidentes en un vertice
	def aristas_incidentes(self,vertice):
		for arista in self.vertices[vertice].values():
			yield arista

	#La cantidad de componentes conexas de un grafo solo aplica para grafos no dirigidos
	def cant_componentes_conexas(self):
		componentes = 0
		visitados = []
		for v in self.obtener_vertices():
			if v not in visitados:
				componentes += 1
				visitados.append(v)
				self._dfs(v,visitados)
		return componentes


#vertices = {origen1:{destino1:arista1,destino2:arista2},origen2:{destino1:arista1,...}}

grafo = Grafo_no_dirigido()
a = grafo.insertar_vertice("a")
b = grafo.insertar_vertice("b")
c = grafo.insertar_vertice("c")
d = grafo.insertar_vertice("d")
e = grafo.insertar_vertice("e")
f = grafo.insertar_vertice("f")

grafo.insertar_arista(a,b,5)
grafo.insertar_arista(a,d,6)
grafo.insertar_arista(b,d,4)
grafo.insertar_arista(b,c,9)
grafo.insertar_arista(d,f,2)
grafo.insertar_arista(d,e,6)
grafo.insertar_arista(f,e,3)
grafo.insertar_arista(f,c,7)
grafo.insertar_arista(c,e,1)

print("Los vertices son:{}".format(grafo.obtener_vertices()))
print("Los adyacentes de c son:{}".format(grafo.adyacentes(c)))


#Al ser un grafo no dirigido:
print("El peso entre a y b es {}".format(grafo.peso_entre(a,b)))
print("El peso entre b y a es {}".format(grafo.peso_entre(b,a)))

#print("Los vertices son:{}".format(grafo.obtener_vertices()))
#print("Los adyacentes de f (Einstein) son:{}".format(grafo.adyacentes(f)))

print(grafo.cantidad_aristas())
print(grafo.cantidad_vertices())

print("Recorrido mediante BFS")
lista_visitados_bfs = grafo.bfs(a)
for vertices in lista_visitados_bfs:
	print(vertices.dato)

print("Recorrido mediante DFS")
lista_visitados_dfs = grafo.dfs(a)
for vertices in lista_visitados_dfs:
	print(vertices.dato)

print("Recorrido DFS mediante pilas")
lista_visitados_dfs2 = grafo.dfs_con_pilas(a)
for vertices_aux in lista_visitados_dfs2:
	print(vertices_aux.dato)

print("La cantidad de componentes conexas son:",grafo.cant_componentes_conexas())

#arista_a_b = grafo.retornar_arista(a,b)
#print(arista_a_b.peso,arista_a_b.origen.dato,arista_a_b.destino.dato)

#arista_incidente = grafo.aristas_incidentes(a)
#El vertice a tiene 2 aristas incidentes
#print(next(arista_incidente))
#print(next(arista_incidente))



