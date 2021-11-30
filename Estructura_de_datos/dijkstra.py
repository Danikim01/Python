from cola_con_prioridad import ColaConPrioridad
from grafos_implementacion_con_clases import Grafo_no_dirigido
from grafos_implementacion_con_clases import Vertice
from grafos_implementacion_con_clases import Arista

#Si al Heap inserto tuplas tipo (distancia,vertice)
def comparador_caminos(tupla1,tupla2):
	return tupla1[0] - tupla2[0]

def dijkstra(grafo,origen,funcion_comp):
	dist = {}
	padres = {}
	for v in grafo.obtener_vertices():
		dist[v] = float("inf")
	dist[origen] = 0
	padres[origen] = None
	q = ColaConPrioridad(funcion_comp)
	q.encolar((0,origen))
	visitados = []
	while not q.cola_vacia():
		v = q.desencolar()
		if v[1] not in visitados:
			visitados.append(v[1])
		#v es una tupla (al heap inserto tuplas)
		for w in grafo.adyacentes(v[1]):
			if dist[w] > dist[v[1]] + grafo.peso_entre(v[1],w):
				#si entra al if actualizo la tabla de distancias
				dist[w] = dist[v[1]] + grafo.peso_entre(v[1],w)
				padres[w] = v[1]
				q.encolar((dist.get(w),w))
	return padres,dist,visitados

grafito = Grafo_no_dirigido()

a = grafito.insertar_vertice("a")
b = grafito.insertar_vertice("b")
c = grafito.insertar_vertice("c")
d = grafito.insertar_vertice("d")
e = grafito.insertar_vertice("e")
f = grafito.insertar_vertice("f")

grafito.insertar_arista(a,b,5)
grafito.insertar_arista(a,d,6)
grafito.insertar_arista(b,d,4)
grafito.insertar_arista(b,c,9)
grafito.insertar_arista(d,f,2)
grafito.insertar_arista(d,e,6)
grafito.insertar_arista(f,e,3)
grafito.insertar_arista(f,c,7)
grafito.insertar_arista(c,e,1)

tuplita = dijkstra(grafito,a,comparador_caminos)

dic_padres = tuplita[0]
dic_distancias = tuplita[1]
lista_visitados = tuplita[2]

for i in dic_padres.items():
	if i[1] is None:
		print("Vertice: {},Padre: {}".format(i[0].dato,i[1]))
	else:
		print("Vertice: {},Padre: {}".format(i[0].dato,i[1].dato))

print("\n")

for p in dic_distancias.items():
	print("Vertice: {},distancia: {}".format(p[0].dato,p[1]))	

print("Lista de visitados")
for v in lista_visitados:
	print(v.dato,end=" ")
print("\n")