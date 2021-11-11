#map
#filter
#lambda

#Map (es bastante parecido al tema puntero a funcion)
#Map se usa para realizar una operacion particular a cada elemento de un objeto iterable, es 
#como un iterador interno.

def sqr(num1):
	return num1**2

l = [10,20,30,40,50,60]
result = map(sqr,l)
#result es un objeto iterable en si mismo pero no retorna algo en particular
print("El resultado es",result)

#for value in result
#	print(value)

result_list = list(map(sqr,l))
#print(result_list)

l1 = [100,200,300,400,500]
l2 = [10,20,30,40,50]

def add(num1,num2):
	return num1+num2

resultante = list(map(add,l1,l2))
#print(resultante)

#Si quiero "filtrar" ciertos elementos de un objeto iterable
#Puedo usar la funcion "filter".

def check_num(num1):
	return num1%2==0

l = [100,115,120,130,140]
result = list(filter(check_num,l))
#print(result)

#Lambda (si no reutilizan las funcinoes y las mismas con muy pequeñas se usa lambda de la siguiente forma)

l = [10,20,30,40,50,60]
result = list(map(lambda num1:num1**2,l))
print("resultado de la funcion map es",result,type(result))

l = [100,115,120,130,140]
result = list(filter(lambda num1:num1%2==0,l))
print("resultado de la funcion filter es",result,type(result))

#Otra forma famosa de usar funciones lambda es 
#para ordenar un diccionario segun los valores (no segun las claves)
#de menor a mayor

d = {1:50,2:40,3:30,4:20,5:10}

l = dict(sorted(d.items(),key=lambda x:x[1]))
print(l)

#Otro ejemplo
l2 = [(5,'efavsfv'),(4,'cvasvaw'),(3,'awrr'),(2,'dvwr'),(1,'bvcb')]
l3 = sorted(l2,key=lambda x:x[1])
print(l3)

lista_de_tupla = [(4, 1),(9, 6),(13, 3)] 
maximo = max(lista_de_tupla,key=lambda tupla:tupla[1])
print(lista_de_tupla,"El maximo es ",maximo)
lista = [0 for valor in range(0,maximo[1]+1)]
print(lista)


d = {1:50,2:40,3:30,4:20,5:10}
def con_cada_clave(dic,funcion,auxiliar):
	lista = dic.keys()
	cant_recorridos = 0
	for i in lista:
		cant_recorridos += 1
		if(funcion(i,auxiliar)):
			return cant_recorridos
	return cant_recorridos

def funcion(clave,auxiliar):
	return clave == auxiliar

print(con_cada_clave(d,funcion,3))