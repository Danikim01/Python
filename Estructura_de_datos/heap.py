#como funciona el comparador : 
#el comparador recibe 2 elementos cualesquiera (del mismo tipo) a y b, 
#hace "a" - "b", si el resultado es positivo entonces a > b
#si el resultado es negativo entonces "b" es mayor a "a"

#comparador(elementos[pos_padre],elementos[pos_actual])

#def comparador(a,b):
#	return a-b

class HeapMinimal:
    def __init__(self,comparador):
        self.elementos = []
        self.len = 0
        self.comparador = comparador
    def swap(self,a,b):
        aux = self.elementos[a]
        self.elementos[a] = self.elementos[b]
        self.elementos[b] = aux

    def sift_up(self,pos_actual):
        if pos_actual == 0:
            return
        pos_padre = (pos_actual-1)//2
        if self.comparador(self.elementos[pos_padre],self.elementos[pos_actual]) > 0:
            self.swap(pos_padre,pos_actual)
            self.sift_up(pos_padre)

    def sift_down(self,pos_actual):
        hijo_izq = (2*pos_actual)+1
        hijo_der = (2*pos_actual)+2

        #caso sin hijos
        if hijo_izq >= self.len:
            return

        #caso un hijo izquierdo
        if hijo_izq < self.len and hijo_der >= self.len:
            #me fijo si mi hijo izquierdo es menor al actual
            if self.comparador(self.elementos[hijo_izq],self.elementos[pos_actual]) < 0:
                self.swap(hijo_izq,pos_actual)
                self.sift_down(hijo_izq)

        #caso dos hijos
        if hijo_der < self.len:
            #me fijo si mi actual es menor a alguno de mis dos hijos
            if self.comparador(self.elementos[hijo_izq],self.elementos[pos_actual]) < 0 or self.comparador(self.elementos[hijo_der],self.elementos[pos_actual]) < 0:
                if self.comparador(self.elementos[hijo_izq],self.elementos[hijo_der]) < 0:
                    self.swap(hijo_izq,pos_actual)
                    self.sift_down(hijo_izq)
                elif self.comparador(self.elementos[hijo_der],self.elementos[hijo_izq]) < 0:
                    self.swap(hijo_der,pos_actual)
                    self.sift_down(hijo_der)

    def heap_insertar(self,elemento):
        self.elementos.append(elemento)
        self.sift_up(self.len)
        self.len += 1
        
    def heap_extraer_raiz(self):
        if self.heap_vacio():
            raise TypeError("Heap Vacio")
        extraido = self.elementos[0]
        self.elementos[0] = self.elementos[self.len-1]
        self.elementos.pop()
        self.len -= 1
        self.sift_down(0)
        return extraido

    def heapify(self,vector_nros):
    	pos_aux = (self.len-1)//2
    	for i in range(pos_aux,-1,-1):
    		self.sift_down(i)

    def heap_sort(self):
    	lista_aux = []
    	while not self.heap_vacio():
    		lista_aux.append(self.heap_extraer_raiz())
    	return lista_aux

    def heap_vacio(self):
        return self.len == 0

    def heap_mostrar(self):
        print(self.elementos)
        #for valor in self.elementos:
        #	print(valor[1].dato)


#heap = HeapMinimal(comparador)
#heap.heap_insertar(32)
#heap.heap_insertar(30)
#heap.heap_insertar(70)
#heap.heap_insertar(45)
#heap.heap_insertar(1)
#heap.heap_insertar(25)
#heap.heap_insertar(3)
#heap.heap_insertar(2)
#heap.heap_insertar(9)
#heap.heap_insertar(11)
#heap.heap_insertar(6)
#heap.heap_insertar(45)
#heap.heap_insertar(4)
##heap.heap_mostrar()

#lista = heap.heap_sort()
#print(lista)
