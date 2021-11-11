
##diccionario = {"key":value}
#es una estructura de datos mutable
#no ordenado
#claves unicas por cada valor (no hay claves duplicadas)
#las claves son inmutables
#las claves pueden ser int, float,str,tuple
d = {"emp_id":101,"name":"ABC","email":"abc@gmail.com"}

##operaciones sobre diccionarios:

#agregar elemento clave-valor
#d["contact_no"] = 123456789
#print(d)
#d["contact_no"] = 888888888
#print(d)

valor_dic = (d["emp_id"])


#print(d.get("emp_id"))
#print(d.get("age")) #Esto retorna "None"

#la funcion get, ademas hace algo raro: busca la clave que le pasas por parametro, si lo encuentra
#retorna el valor asociado a la clave y si lo no encuentra devuelve lo que le pasas por parametro:

#print(d.get("age","La clave no existe ctm"))
#print(d.get("emp_id","asdfjhaskjdfhak"))

#La funcion "setdefault" hace lo siguiente: puede chequear si una clave existe dentro de la tabla de hash
# y si existe retorna ese valor, y si no existe la funcion agrega ese elemento segun un valor que vos definis.
#si no se le especifica ningun valor a la clave a agregar se le agrega "None"

#print(d.setdefault("emp_id"))
#print(d.setdefault("age"))
#print(d)
#print(d.setdefault("age",50))
#print(d)

#iterar sobre diccionarios
#al iterar sobre el diccionario por defecto se iteran sobre 
#las claves del diccionario
#for x in d:
#	print(x)
#pero de esta forma se puede imprimir clave-valor:
#for key in d:
#	print(key,d[key])

d = {}
for value in range(1,11):
	d[value] = value*value


#print(d)

##algunas funciones mas: "keys","values","items"

#accede a las claves de la tabla de hash
l = d.keys()
#print(l,type(l))
#accede a los valores de la tabla de hash
l2 = d.values()
print("Valor de l2 son",l2)
#accede a los par clave-valor de la tabla de hash
l3 = d.items()
#print(l3)

#forma de iterar sobre la tupla clave-valor
#for t in d.items():
#	print(t)

#otras funciones : "zip"

#quiero crear un diccionario en donde l1 son las claves
# y l2 el valor
l1 = [1,1,3,4,5] 
l2 = [1,4,9,16,25]

d = dict(zip(l1,l2))
print("Acaa",d)
#si lo quiero alvere:
d_2 = dict(zip(l2,l1))
print(d_2)

#ahora quiero crear nuevamente un diccionario cuyas claves sean elementos de la lista
l = [1,2,3,4,5]
l2 = [1,4,9,16,25]
#d_3 es un diccionario cuyas claves son 
print("dic.fromkeys(l)")
d_3 = dict.fromkeys(l)
print(d_3)
# y para los valores tengo que especificar que valor le pertenece a cada clave
d_3 = dict.fromkeys(l,0)
#print(d_3)
print("dic.fromkeys(l,l2)")
d3 = dict.fromkeys(l,l2)
print(d3)

#Como "concatenar" diccionarios

d1 = {1:1,2:4,3:9,4:16}
d2 = {5:25,6:36,7:49}

d1.update(d2)
print("Despues del update imprimo d1: {}".format(d1))

d1 = {1:1,2:4,3:9,4:16}

#Metodos para eliminar elementos de un diccionario : "pop","popitem","clear","del"

#la operacion "pop" elimina del diccionario el elemento asociado a la clave ingresada y la devuelve
#r = d1.pop(2)

#la operacion "popitem" devuelve un par clave-valor del diccionario
#cualesquiera y las elimina
r = d1.popitem()
#print(d1,r)

#la operacion "clear" vacia el diccionario
d1.clear()
print(d1)

#la operacion del, elimina el diccionario de la memoria

del d1
#print(d1)

def tuplas_a_diccionario(lista_de_tuplas):
	d = {}
	for index in range(0,len(lista_de_tuplas)-1):
		l = []
		if(lista_de_tuplas[index][0] == lista_de_tuplas[index+1][0]):
			l.append(lista_de_tuplas[index][1])
			l.append(lista_de_tuplas[index+1][1])
		else:
			l.append(lista_de_tuplas[index+1][1])
		if(index==len(lista_de_tuplas)-1):
			d[lista_de_tuplas[index][0]] = l
		else:
			d[lista_de_tuplas[index+1][0]] = l
	return d

listita = [('Hola','Don pepito'),('Hola','Don Juan'),('Buenos','Dias'),('Buenos','Noche'),('Claudio','Koo'),('Claudio','Coreano'),('Hola','asdfasd')]

d = {}
d = tuplas_a_diccionario(listita)
#lista = ['Don pe','Don Juan']
#d["Hola"] = lista
print(d)


s = "Que lindo dia que hace hoy"
l = s.split(" ")

def que_lindo_dia_ctm(string):
	s_lower = string.lower()
	l = s_lower.split(" ")
	dic = {}
	for value in l:
		contador = l.count(value)
		dic[value] = contador
	return dic

dic_aux = que_lindo_dia_ctm(s)
print(dic_aux)

def splitear_string(texto):
	l = [caracter for caracter in texto]
	return (l)

def cuantos_caracteres(texto):
	dic = {}
	l = splitear_string(texto)
	for value in l:
		contador = l.count(value)
		dic[value] = contador
	return dic
	
dic_2 = cuantos_caracteres("ha olaa ao h")
print(dic_2) 



def eliminar_repetidos(lista):
	for elemento in lista:
		if lista.count(elemento) > 1:
			lista.remove(elemento)
	return lista


def asignar_mas_largo(caracter,lista):
	palabra_longuitud = []
	for p in lista:
		if caracter in p:
			palabra_longuitud.append((p,len(p)))
	l = sorted(palabra_longuitud,key=lambda tupla:tupla[1])
	return l[-1][0]


def obtener_cadenas_largas_por_caracter(texto):
	lista = texto.split(" ")
	dic = {}
	lista_caracteres = [caracter for palabra in lista for caracter in palabra]
	lista_caracteres = eliminar_repetidos(lista_caracteres)
	for caracter in lista_caracteres:
		dic[caracter] = asignar_mas_largo(caracter,lista)
	return dic

print(obtener_cadenas_largas_por_caracter('pero que hermoso dia hay'))


