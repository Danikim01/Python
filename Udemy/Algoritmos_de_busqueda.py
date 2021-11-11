
def busqueda_binaria_aux(lista,inicio,fin,elemento):
	if len(lista) == 0:
		lista.append(elemento)
		return len(lista)-1;
	if inicio > fin:
		for index,valor in enumerate(lista):
			if valor > elemento:
				lista.insert(index,elemento)
				return index
			if index == len(lista)-1 and elemento > valor:
				lista.append(elemento)
				return len(lista)-1;
	medio = (inicio+fin)//2
	if lista[medio] == elemento:
		return medio
	elif lista[medio]<elemento:
		return busqueda_binaria_aux(lista,medio+1,fin,elemento)
	else:
		return busqueda_binaria_aux(lista,inicio,medio-1,elemento)


def busqueda_binaria(lista,elemento):
	return busqueda_binaria_aux(lista,0,len(lista)-1,elemento)

