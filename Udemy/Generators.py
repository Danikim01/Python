
def printVal(lista):
	for value in lista:
		print(value)

l = [10,20,30,40,50,60]
#printVal(l)

#La funcion fibo genera la sucesion infinita de fibonacci

def fibo():
	first_num = 0
	second_num = 1
	#yield first_num
	yield second_num
	while(True):
		next_val = first_num + second_num
		yield next_val
		first_num,second_num = second_num,next_val

g = fibo()
#print(g)
#print(next(g))
#print(next(g))
#print(next(g))
#print(next(g))
#print(next(g))

##Si por ejemplo quiero los primeros 10 digitos de la serie fibonacci puedo hacer lo siguiente:

for value in range(10):
	print(next(g))

#Si quiero los proximos 20

for value in range(20):
	print(next(g))

#Aplicando esto para el primer ejemplo

def printVal2(lista):
	for value in lista:
		yield value

l = [10,20,30,40,50,60]

#g = printVal2(l)
#print(next(g))
#print(next(g))
#print(next(g))

l = [10,20,30,40,50,60]
l2 = [value**2 for value in l]
l3 = (value**2 for value in l)

for value in range(6):
	print(next(l3))