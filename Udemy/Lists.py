l = [100,200,300,400,500]
#iterar sobre elementos alternadamente:

for value in l[::2]:
	print(value)

#agregar elementos a una lista

#l.append(600)
#print(l)

#agregar multiples elementos a una lista simultaneamente

l.extend([500,600,700,800])

#l.extend("Python")

#insertar elemento en posicion (lista)
#l.insert(1,1000)

#forma de copiar correctamente una lista a otra lista 

#l = [10,20,30]
#l2 = l.copy() #en vez de l2 = l (aunque es valido)
#l.append(40) #de esta forma el contenido solo le agrega en la primera lista
#print(l,l2)

#actualizar elemento en una lista

l = [10,20,30,40,50]
#l[2] = 300

#metodos de eliminacion:pop(desapilar),remove,clear,del
#1) .pop() desapila el ultimo elemento de la lista y la devuelve

#r = l.pop()
#print(l,r)

#2) .remove() 
#l.remove(20) #remueve el primer elemento que se encuentra en la lista

#3) clear : esta operacion vacia la lista pero la misma sigue existiendo
#4) del : elimina la lista completamente.



#metodos de ordenamiento

l = [50,40,30,30,20,10]
#l.clear()
#print(l)
#help(list)
#print(l)

#l.sort()

#l3 = sorted(l)

#como revertir una lista
#l.reverse()

#buscar posicion de cierto elemento
#posicion = l.index(30)
#contar la cantidad de elementos repetidos
#print(l.count(30))

#como concatenar listas

#l = [10,20,30,40]
#l2 = [100,200,300]
#l3 = l+l2
#print(l3)

#tambien se pueden hacer cosas raras como esta

l4 = [0.1]
l5 = (l4*10)
#print(l5)

l = [100,200,300,400,500]
suma_elementos = sum(l)
maximo_elemento = max(l)
minimo_elemento = min(l)


