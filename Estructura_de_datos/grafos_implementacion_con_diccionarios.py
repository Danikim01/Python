grafo = {
	"a":["c"],
	"b":["c","e"],
	"c":["a","b","d","e"],
	"d":["c"],
	"e":["b","c"],
	"f":[]
}

grafo_dirigido = {
	"a":["c"],
	"b":["d"],
	"c":["e"],
	"d":["a","d"],
	"e":["b","c"],
}

def imprimir_grafo(grafo):
	for vertice in grafo.keys():
		for vecino in grafo[vertice]:
			print("{}->{}".format(vertice,vecino))

#imprimir_grafo(grafo_dirigido)

def contiene_vertice(grafo,vertice):
	if vertice not in grafo.keys():
		raise IndexError("Vertice: {} no esta en el grafo".format(vertice))
	else:
		return True

def agregar_arista(grafo,origen,destino):
	contiene_vertice(grafo,origen)
	contiene_vertice(grafo,destino)
	grafo[origen].append(destino)


#agregar_arista(grafo_dirigido,"a","b")
#imprimir_grafo(grafo_dirigido)

def vecinos(grafo,vertice):
	contiene_vertice(grafo,vertice)
	return grafo[vertice]

#devoler el par origen - destino
def aristas(grafo):
	mis_aristas = []
	for vertice in grafo.keys():
		for vecino in grafo[vertice]:
			mis_aristas.append((vertice,vecino))
	return mis_aristas

lista_aristas = aristas(grafo_dirigido)
print(lista_aristas)

grafo = {
	"a":["c"],
	"b":["c","e"],
	"c":["a","b","d","e"],
	"d":["c"],
	"e":["b","c"],
	"f":[]
}

def camino_entre(grafo,origen,destino,camino=[]):
	camino.append(origen)
	if origen == destino:
		return camino
	for vertice in grafo[origen]:
		if vertice not in camino:
			nuevo_camino = camino_entre(grafo,vertice,destino,camino)
			if nuevo_camino:
				return nuevo_camino

camino_entre_a_y_b = camino_entre(grafo,"a","e")
print(camino_entre_a_y_b)

