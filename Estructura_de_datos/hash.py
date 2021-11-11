

class Hash:
	def __init__(self):
		self.tabla = {}
	def hash_insertar(self,clave,valor):
		if type(clave) != str:
			return -1
		self.tabla[clave] = valor
		return 0
	def hash_quitar(self,clave):
		valor = self.tabla.get(clave)
		if valor is not None:
			self.tabla.pop(clave)
			return 0
		else:
			return -1
	def hash_obtener(self,clave):
		return self.tabla.get(clave)
	def hash_contiene(self,clave):
		return self.tabla.get(clave) is not None
	def hash_cantidad(self):
		return len(self.tabla.values())
	def hash_con_cada_clave(self,funcion,auxiliar):
		lista = self.tabla.keys()
		cant_recorridos = 0
		for i in lista:
			cant_recorridos += 1
			if(funcion(i,auxiliar)):
				return cant_recorridos
		return cant_recorridos
	def mostrar_tabla(self):
		print(self.tabla)

def funcion(clave,contexto):
	if clave == contexto.auxiliar:
		contexto.extra = clave
		return True
	return False


class Contexto:
	def __init__(self,auxiliar,extra):
		self.auxiliar = auxiliar
		self.extra = extra

Tabla_De_Hash = Hash()
Tabla_De_Hash.hash_insertar("GuauGuau","Perro")
Tabla_De_Hash.hash_insertar("MiauMiau","Gato")
Tabla_De_Hash.hash_insertar("MuuMuu","Vaca")
Tabla_De_Hash.hash_insertar("Megustalapija","Gays")
print("La cantidad de elementos son:",Tabla_De_Hash.hash_cantidad())
print(Tabla_De_Hash.hash_contiene("GuauGuau"))
print(Tabla_De_Hash.hash_contiene("asdfasdljv"))
print("El elemento obtenido es:",Tabla_De_Hash.hash_obtener("MiauMiau"))
Tabla_De_Hash.mostrar_tabla()
a_asignar = None
ctx = Contexto("Megustalapija",a_asignar)
print(Tabla_De_Hash.hash_con_cada_clave(funcion,ctx))
print("El extra ahora es",ctx.extra)

