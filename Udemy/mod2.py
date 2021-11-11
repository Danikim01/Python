import recursividad

l = [100,200,300,400,500]
key = 5000

#print(recursividad.busqueda_binaria(l,key))

#help(recursividad)

#import math
#help(math)

def es_primo(n):
	contador = 0
	for value in range(2,n):
		if(n%value != 0):
			contador+=1
	if(contador == n-2):
		return True
	else:
		return False

def lista_primos(lista):
	l = []
	for value in lista:
		if (es_primo(value)==True):
			l.append(value)
	return l

l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
l_2 = lista_primos(l)
print(l_2)


#Problema : 

#Escribir una función empaquetar para una lista, donde epaquetar significa indicar
#la repetición de valores consecutivos mediante una tupla (valor, cantidad de repeticiones). Por
#ejemplo, empaquetar([1, 1, 1, 3, 5, 1, 1, 3, 3]) debe devolver [(1, 3), (3, 1), (5, 1)
#, (1, 2), (3, 2)].


def empaquetar(lista):
	contador = 1
	l = []
	for index in range(0,len(lista)-1):
		if(lista[index]==lista[index+1]):
			if(index != len(lista)-2):
				contador += 1
			else:
				contador += 1
				l_aux = []
				l_aux.append(lista[index])
				l_aux.append(contador)
				l.append(tuple(l_aux))
		else:
			l_aux = []
			l_aux.append(lista[index])
			l_aux.append(contador)
			l.append(tuple(l_aux))
			contador = 1
	return l

	
lista_empaquetable = [1,1,1,3,5,1,1,3,3,3,3]
lista = empaquetar(lista_empaquetable)
print(lista)



#Ejercicio 9.1. Escribir una función que reciba una lista de tuplas, y que devuelva un diccionario
#en donde las claves sean los primeros elementos de las tuplas, y los valores una lista con los
#segundos.

