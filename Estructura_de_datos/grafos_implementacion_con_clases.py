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

class Grafo:
	def __init__(self):
		self.vertices = {}
	def insertar_vertice(self,dato):
		vertice = Vertice(dato)
		self.vertices[vertice] = {}
		return vertice
	def insertar_arista(self,origen,destino,peso):
		arista = Arista(origen,destino,peso)
		self.vertices[origen][destino] = arista
	def cantidad_vertices(self):
		return (len(self.vertices.keys()))

	def retornar_arista(self,origen,destino):
		return self.vertices[origen].get(destino)

	def cantidad_aristas(self):
		contador = 0
		for vertice in self.vertices:
			contador += len(self.vertices[vertice].values())
		return contador
	#Devuelve las aristas incidentes en un vertice
	def aristas_incidentes(self,vertice):
		for arista in self.vertices[vertice].values():
			yield arista

	def camino_entre(self,origen,destino,camino=[]):
		camino.append(origen)
		if origen == destino:
			return camino
		for vertice in self.vertices:
			for sub_vertice in self.vertices[vertice]:
				if sub_vertice not in camino:
					nuevo_camino = camino_entre(grafo,vertice,destino,camino)
					if nuevo_camino:
						return nuevo_camino
	

	def imprimir_grafo(self):
		return self.vertices.items()

#vertices = {origen1:{destino1:arista1,destino2:arista2},origen2:{destino1:arista1,...}}


grafo = Grafo()
#a = Vertice("mariano")
#b = Vertice("lucas")
#c = Vertice("gabriel")

#grafo.insertar_arista(a,b,8)
#grafo.insertar_arista(a,c,8)
#grafo.insertar_arista(b,c,1)



#a = grafo.insertar_vertice("mariano")
#b = grafo.insertar_vertice("lucas")
#c = grafo.insertar_vertice("gabriel")

#grafo.insertar_arista(a,b,8)
#grafo.insertar_arista(a,c,8)
#grafo.insertar_arista(b,c,1)

#print(grafo.cantidad_aristas())
#print(grafo.cantidad_vertices())

#arista_a_b = grafo.retornar_arista(a,b)
#print(arista_a_b.peso,arista_a_b.origen.dato,arista_a_b.destino.dato)

#arista_incidente = grafo.aristas_incidentes(a)
#El vertice a tiene 2 aristas incidentes
#print(next(arista_incidente))
#print(next(arista_incidente))

