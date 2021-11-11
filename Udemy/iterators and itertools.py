l = [100,200,300,400,500]
i = iter(l)
#print(i)

#print(next(i))
#print(next(i))

import itertools

l1 = [10,20,30,40,50]
l2 = [100,200,300,400,500]
l3 = [1000,200,3000,4000,5000]

#Crea un itearador de la lista resultante de l1,l2 y l3
i = itertools.chain(l1,l2,l3)
#print(i)
#print(next(i))

#for value in i:
#	print(value)

#Metodo de iteradores para iterar multiples veces la lista
l = [10,20,30,40,50]
count = 0
#Crea un iterador infinito (hay ciclos infinitos - infinitas iteraciones)
for value in itertools.cycle(l):
	if count < 20:
		print(value,count)
	else:
		break
	count+=1

l = [10,20,30,40,50]
count = 0
for value in itertools.repeat(l):
	if count < 20:
		print(value,count)
		for sub_value in value:
			print(sub_value)
	else:
		break
	count+=1

#i es un iterador externo de l.
print("------------------------------------------")

l = [10,20,30,40]

i = iter(l)

#for value in i:
#	print(value)

#### print(next(i))

#Este print me da error (el iterador apunta al ultimo elemento y no hay siguiente)

#Por lo tanto hago lo siguiente para poder resetar el iterador

t = itertools.tee(i)
#print(t,type(t))

#Este t es nuevamente un objeto iterable de tipo tupla

for value in t[0]:
	print(value)

#Si quiero iterar sobre la lista de vuelta:

for value in t[1]:
	print(value)


print("---------------------------------------------------")

l1 = [10,20,30,40,50]
l2 = [100,200,300,400,500]
l3 = [1000,2000,3000,4000,5000]

i = itertools.chain(l1,l2,l3)
#como i es una tupla no puede hacer slicing
#entonces si quiero hacer una slicing de l1+l2+l3 hago:
#especifico : (iterador,ppio,fin)
for value in itertools.islice(i,0,8):
	print(value)

print("---------------------------------------------")

#Si quiero iterar infinitamente sobre el iterador puedo hacer lo siguiente:
#itertools.count(ppio,cada cuando aumenta)
#Tengo que establecer una condicion de corte yo
count = 0
for value in itertools.count(10,5):
	if count>20:
		break
	else:
		print(value)
	count += 1

print("----------------------------------------------------------------")

#En python se pueden hacer permutaciones asi :
#itertools.permutations(iterable,combinaciones)
l = [1,2,3,4,5,6]
print(list(itertools.permutations(l,2)))

#y combinaciones:

print(list(itertools.combinations(l,2)))