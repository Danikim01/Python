#sets 
#Los sets son mutables
#Todos los elementos en el setdeben ser unicos
#No pueden haber elementos repetidos en el set
#Solo se pueden agregar elemento inmutables: 
#solo se pueden agregar int,float,tuples y strings
#Estructura de dato no ordenado


s = {100,200,300,400}

#agregar elementos

s.add(500)
#print(s)

s1 = {10,20,30,40,50,60}
s2 = {40,50,60,70,80,90}

#Union

s3 = s1.union(s2)
#print(s3)

#Interseccion

s3 = s1.intersection(s2)
#print(s3)

#Diferencia

#obtengo elementos del set s1 que no esten presentes en set2
s3 = s1.difference(s2)
#obtengo elementos del set s2 que no esten presentes en set1
s4 = s2.difference(s1)
#print(s3)
#print(s4)

#Diferencia simetrica
#obtengo todos los elementos de la union de set1 con set2 excepto los repetidos
s3 = s1.symmetric_difference(s2)
#print(s3)


#la funcion update hace la union pero no retorna nada y ademas modifica el set1 original

#s1.update(s2)

#s1.intersection_update(s2)

#s1.difference_update(s2)
#s2.difference_update(s1)
#print(s1,s2)

#s1.symmetric_difference_update(s2)

s1 = {100,200,300,400,500}
s2 = {100,200,300}
#El comando "issubset" determinar si un set esta dentro de otro
#print(s2.issubset(s1))
#El comando "issubset" determinar si un set contiene a otro
#print(s1.issuperset(s2))

l = [100,200,300,400,500,400,500]

s = set(l)

l1 = [100,200,300,400,500]
l2 = [50,100,150,200,250,500,45,35,20,10]

s1 = set(l1)
s2 = set(l2)

s3 = s1.union(s2)

#l3 = list(s3)

#l3.sort()
#print(s3,type(s3))
l3 = sorted(s3)
#print(l3,type(l3))

#Metodos de eliminacion : "pop","remove","discard","clear","del"

##La funcion "pop" elimina un elemento al azar del set y la retorna
#r = s.pop()
#print(r)
##La funcion "remove" elimina un elemento en particular
##Si se elimina un elemento inexistente la funcion devuelve error
print(s)
s.remove(400)
print(s)
##La funcion "discard" tambien elimina un elemento particular
##pero si se quiere eliminar un elemento inexistente no hace ningun cambio
s.discard(100)
print(s)
s.discard("Mi chota es grande")

##La funcion clear vacia el set
s.clear()
print(s)