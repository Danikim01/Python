l = [100,200,300,400,500]
l2 = []


#for value in l:
#	l2.append(value*value)


#Puedo resolver este mismo problema usando ¿comprehension?

l2 = [value*value for value in l]
#print(l2)

l = [10,20,25,30,35,60,65,70,85]
l2 = [value for value in l if value%2 == 0]
print(l2)

l = ['abc','abcd','abcde','zzzzzz']
l2 = [len(value) for value in l]
#print(l2)

#Obtener una list de tuplas

l2 = [(value1,value2) for value1 in range(1,5) for value2 in range(100,103)]
#print(l2)

l = [[1,2,3],[4,5,6],[7,8,9]]
l2 = []
for value in l:
	for val2 in value:
		l2.append(val2)
print(l2)

#hacer lo mismo con comprehension

l3 = [val2 for value in l for val2 in value]
#print(l3)

l = [100,105,110,115,120]
#"even","odd"

l2 = ["Even" if value%2 == 0 else "Odd" for value in l]
#print(l2)


##Set Comprehension

#Si quiero un diccionario asi 1:1, 2:4, 3:9, 4:1

dic = {}

#Para ello, puedo hacer lo siguiente:

for x in range(1,11):
	dic[x] = x*x
#print(dic)

#o puedo hacer esto si me apetece:

d = {x:x**2 for x in range(1,11)}
print("d es",d)

#Quiero hacer un diccionario de cada caracter con su valor en numero ascii:

d = {chr(ascii_value):ascii_value for ascii_value in range(97,123)}
#print(d)

#Swap keys - values de d:
#Una forma es : 
d_aux = {}
for key,value in d.items():
	#print("La clave es",key,"y el valor es",value)
	d_aux[value] = key	
#print(d_aux)
#Otra forma es 

d2 = {value:key for key,value in d.items()}
print(d2)


