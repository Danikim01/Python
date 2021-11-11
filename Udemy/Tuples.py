#tuple:
##inmutable datastructure
##ordener indexing and slicing
t = (10,20,20,20,30,30,40)
#print(t,type(t))
#print(t[0])
#print(t[-1])

#print(t[:3])
#print(t.index(20))
#print(t.count(20))

#las tuplas se usan para pasar datos de una funcion a otra

l = [10,20,30,40,50]

#imprime la posicion de los elementos junto a los elementos
for index,value in enumerate(l):
	print(index,value)
#imprime la posicion de los elementos junto a los elementos pero en una tupla
for x in enumerate(l):
	print(x)
#imprime solo la posicion de los elementos
for x in enumerate(l):
	print(x[0])
#imprime solo los valores de los elementos
for x in enumerate(l):
	print(x[1])

#como convertir una lista a una tupla:

l = [10,20,30,40,50]
t = tuple(l)
print(t,type(t))

#viceversa...

t = ("a","b","c",100)
l = list(t)
print(l,type(l))