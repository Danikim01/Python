"""
Docstring: this module cointans binary serach implementation

"""


def factorial(n):
	if n==1:
		return 1
	return n*factorial(n-1)

#print(factorial(6))

def busqueda_binaria(lista,valor):
	"""
	Binary searh: input a list and key
	retun True if key existe else returns False
	"""
	if(len(lista)==0):
		print("No se ha encontrado el valor")
		return False
	else:

		medio = len(lista) // 2

		if(lista[medio]==valor):
			print("Se ha encontrado el valor")
			return True
		else:
			if(valor > lista[medio]):
				return busqueda_binaria(lista[medio+1:],valor)
			else:
				return busqueda_binaria(lista[:medio],valor)

#print(__name__)
if __name__ == '__main__':
	l = [100,200,300,400,500,600,700,800,900]
	valor = 400
	output = busqueda_binaria(l,valor)
	print(output)


def euclides(num1,num2):
	while(num1 != num2):
		if num1 > num2:
			num1 -= num2
		else:
			num2 -= num1
	return num1,num2

numero = euclides(412,184)
#print("El mcd de 412 y 184 es {}".format(numero[0]))

def euclides_recursivo(num1,num2):
	if num1==num2:
		return num1,num2
	elif num1>num2:
		return (num1-num2,num2)
	else:
		return (num1,num2-num1)

numero_2 = euclides(412,184)
print("El mcd es",numero)

def suma_elementos_lista(lista,posicion):
	if posicion==len(lista):
		return 0
	else:
		return lista[posicion]+suma_elementos_lista(lista,posicion+1)

lista = [value for value in range(0,101)]
#print("La lista tiene {} elementos".format(len(lista)))
suma = suma_elementos_lista(lista,0)
#print(suma)

def suma_elementos_lista_2(lista):
	if len(lista)==0:
		return 0
	else:
		r = lista.pop()
	return r+suma_elementos_lista_2(lista)

suma_2 = suma_elementos_lista_2(lista)
print("La suma es",suma_2)


def es_pontencia(n1,n2):
	indice = 1
	n3 = n2
	while(n1>n3):
		 n3 += n2**indice
		 indice += 1
	if(n1 == n3):
		print("Es potencia")
	else:
		print("No es potencia")

#es_pontencia(8,2)

