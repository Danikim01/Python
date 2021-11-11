import re

s = "ABCDE1234A"
##Tienen que haber 5 caracteres, seguido de 4 digitos, seguido de 1 caracter
#Verificar:
#5 ocurrencias caraceters - 4 ocurrencias caracteres - 1 caracter

r = re.compile("[A-Z]{5}[0-9]{4}[A-Z]{1}")
#r es regular expression, y la s es donde aplico la verificacion de la misma
l = re.findall(r,s)
#Si la verificacion es valida, el comando anterior devuelve una lista, en caso
#contrario devuelve una lista vacia

#El siguiente patron admite que su primer digito sea un 8 obligatoriamente seguido de 9 numeros.

s = "8123456789"
r = re.compile("^[6-9]{1}[0-9]{9}$")
l = re.findall(r,s)
print(l)


#Ingreso un determinado patron, por ejemplo el formato d euna fecha para que sea verificado
# dd-mm-yyyy
s = "12-05-2018"
r = re.compile("^[0-9]{2}-[0-9]{2}-[0-9]{4}$")
l = re.findall(r,s)
print(l)

##Los caracteres "^" y "$", indican el inicio y el fin del string respectivamente.
#En caso de que de que dichos caracteres se ausenten, la funcion re.findall admitira 
#como valido que se modifique el string "s" cambiando el patron establecido implicitamente sobrepasando el numero 
#de caracteres.

##La funcion re.search() buscara si el string cumple con el patron establecido
#por re.compile(). En caso de que coincida, retorna "re.Match object" y en caso contrario
#retorna None
##La funcion algo.group() retorna el patron que haya validado, siempre y cuando el string s 
#respete el patron. (No retorna una lista)
m = re.search(r,s)
if m:
	print(m.group())
else:
	print("Pattern not found")

#Ahora bien dada la fecha s quiero extraer subgrupos del string, y con eso 
#verificar que fecha, mes o año se haya ingresado al string.

r = re.compile("^([0-9]{2})-([0-9]{2})-([0-9]{4})$")
l = re.findall(r,s)
m = re.search(r,s)

if m:
	print(m.group(0))
	print(m.group(1))
	print(m.group(2))
	print(m.group(3))
else:
	print("Patern not found")

#En caso de que sea un pajero y que no me acuerde de las posiciones de cada grupo, 
#puedo hacer lo siguiente:

r = re.compile("^(?P<dia>[0-9]{2})-(?P<mes>[0-9]{2})-(?P<año>[0-9]{4})$")
l = re.findall(r,s)
m = re.search(r,s)

if m:
	print(m.group(0))
	print(m.group("dia"))
	print(m.group("mes"))
	print(m.group("año"))
else:
	print("Patern not found")

#Otro ejemplo util: numero de telefono
#En este caso quiero señalar al codigo de region como opcional, es decir, 
#dicho codigo puede estar como no estar me da absolutamente igual

s = "+91 8123456789"
r = re.compile("(\+91\s)?[6-9][0-9]{9}")
m = re.search(r,s)
if m:
	print(m.group())
else:
	print("Pattern not found")
