#Modos:

#r => read
#r+ 
#w => write
#w+
#a => append
#a+

fp = open("archivo.txt","r")
#print(type(fp))

#La funcion archivo.read() devuelve un string con todod el contenido del .txt
#Es como un fgetsalloc

#content = fp.read()
#print(content)
#Observacion:

#si hago nuevamente :

#content = fp.read()

#content no lee un carajo porque el cursor del txt esta al final del archivo
#Leer determinanda cantidad de caracteres:

#content = fp.read(25)
#print(content)

##archiv.readlines() devuelve una lista con el contenido del archivo
#con el cual puedo hacer slicing
#content = fp.readlines()
#print(content,type(content))
#Cada elemento de la linea es hasta el \n del archivo
#print(content[:5])


#archivo.readline() lee linea por linea

content = fp.readline()
print(content,type(content))
print(content[:6],len(content))

content = fp.readline()
print(content)

#content = fp.readline()
#print(content)

##Iterar sobre cada caracter del archivo
#for x in fp:
#	print(x)

##Modo w:

#fp = open("input2.txt","w")
#write sobreescribe todo lo que hay en el .txt por los nuevos caracteres
#especificados. PRECAUCION
#fp.write("Sample text line 1")

#En modo "w" solo se puede escribir pero no leer

##Modo w+
#En este modo se puede leer y escribir a la vez

#fp = open("input2.txt","w+")
#write sobreescribe todo lo que hay en el .txt por los nuevos caracteres
#especificados. PRECAUCION
#fp.write("Sample text line 1")

#content = fp.read()
#print(content)

#Sin embargo, el print no imprime una mierda porque el puntero en el archivo
#esta posicionado al final de todo, para ello tengo:

#tell -> current fp position
#seek -> change fp position

#fp = open("input2.txt","w+")
#print(fp.tell())
#fp.write("Sample text line 1")
#print(fp.tell())
#content = fp.read()
#print(fp.tell())
#print(content)

#Muevo el fp mediante la funcion seek

#seek(offset,position)
#offset : numero de caracteres que quiero mover
#posicion -> 0=>inicio del archivo
#             1=>posicion actual archivo
#             2=>posicion final archivo

#seek(15,0) -> change the fp by 15 char from start of the file
#seek(0,2)  -> change fp by 0 char from end of file

#fp = open("input2.txt","w+")
#print(fp.tell())
#fp.write("Sample text line 1")
#print(fp.tell())
#fp.seek(0,0)
#print(fp.tell())
#content = fp.read()
#print(fp.tell())
#print(content)

#Modo r+
#En este modo puedo leer y escribir a la vez manteniendo el contenido del archivo

#fp = open("archivo.txt","r+")
#content = fp.read()
#print(content)

#fp.write("\n\nSample linea added using python script")

#Modo a, a+
#La posicion del puntero fp esta por defecto al final de todo

#Modo a
#Aca no se puede leer
#Pero se puede usar el modo w
#fp = open("archivo.txt","a")
#print(fp.tell())
#fp.write("\n\nabc")

#Modo a+
#Aca se puede leer
#Aca se puede usar el modo w tambien


#fp = open("archivo2.txt","w+")

#for numero in range(0,400):
#	fp.write("Cantidad de lineas: {}\n".format(numero))

#fp.seek(0,0)

def head(ruta_archivo,numero):
	file = open(ruta_archivo,"r")
	for lineas in range(0,numero+1):
		content = file.readline()
		print(content)

def cantidad_caracteres(string):
	contador = 0
	for caracter in string:
		contador += 1
	return contador

def cantidad_palabras(string):
	lista = string.split(" ")
	return (len(lista))

#head("archivo2.txt",55)

def cp(archivo_lectura,archivo_escritura):
	fp = open(archivo_lectura,"r")
	lineas = fp.readlines()
	cant_bytes = 0

	for substrings in lineas:
		cant_bytes += cantidad_caracteres(substrings)

	fp.seek(0,0)
	content = fp.read(cant_bytes)
	fp2 = open(archivo_escritura,"w")
	fp2.write(content)

#cp("archivo2.txt","archivo_escritura.txt")


def wc(archivo_de_texto):
	archivo = open(archivo_de_texto,"r")
	lineas = (archivo.readlines())
	cant_caracteres = 0
	cant_palabras = 0
	cant_lineas = len(lineas)
	for substrings in lineas:
		cant_caracteres += cantidad_caracteres(substrings)
		cant_palabras += cantidad_palabras(substrings)
	return (cant_lineas,cant_palabras,cant_caracteres)


tupla = wc("archivo2.txt")
#print("Cantidad de lineas: {}, cantidad de palabras:{},cantidad de caracteres :{}".format(tupla[0],tupla[1],tupla[2]))

def gep(archivo_de_texto,string):
	archivo = open(archivo_de_texto,"r")
	lineas = archivo.readlines()
	cantidad_repeticiones = lineas.count(string)
	if(cantidad_repeticiones == 0):
		print("El string no esta en el archivo de texto")
	else:
		for linea in lineas:
			if string == linea:
				print(linea)
		#print("El string '{}' se repite '{}' veces".format(string,cantidad_repeticiones))

#gep("archivo2.txt","Me gusta la papa")


def rot12(archivo_origen,archivo_destino):
	origen = open(archivo_origen,"r")
	destino = open(archivo_destino,"w")
	lineas = origen.readlines()
	for linea_origen in lineas:
		for caracter in linea_origen:
			if(ord(caracter)>= 97 and ord(caracter)<= 122):
				print(chr((ord(caracter)+13)%26))
				destino.write(chr((ord(caracter)+13)%26))


#rot12("archivo2.txt","archivo_destino.txt")


def guardar_datos(archivo_de_texto):
	dic = {}
	archivo = open(archivo_de_texto,"r")
	par_lineas = archivo.readlines()
	
	lista = []
	for value in par_lineas:
		lista.append(value.split(":"))
	for value2 in lista:
		longuitud = len(value2[1])
		string = (value2[1])[:longuitud-1]
		dic[value2[0]] = string
	print(dic)


#guardar_datos("archivo_dicc.txt")

def cargar_datos(archivo_de_texto):
	dic = {}
	archivo = open(archivo_de_texto,"r")
	par_lineas = archivo.readlines()
	
	lista = []
	for value in par_lineas:
		lista.append(value.split(":"))
	for value2 in lista:
		dic_aux = {}
		longuitud = len(value2[1])
		string = (value2[1])[:longuitud-1]
		dic_aux[value2[0]] = string
		dic[value2[0]] = dic_aux
	print(dic)

#cargar_datos("archivo_dicc.txt")