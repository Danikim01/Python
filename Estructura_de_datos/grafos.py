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


agregar_arista(grafo_dirigido,"a","b")
imprimir_grafo(grafo_dirigido)

