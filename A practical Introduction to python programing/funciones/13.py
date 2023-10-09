#Funcion que las mayusculas las pasa a minusculas y las minusculas a mayusculas
def cambiar_mayusculas(cadena):

    lista = list(cadena)
    lista_contenedora = []
    for char in lista:
        if char.isupper():
            x = char.lower()
            lista_contenedora.append(x)
        elif char.islower():
            x = char.upper()
            lista_contenedora.append(x)
    lista_contenedora = "".join(lista_contenedora)
    return lista_contenedora

m = "hoLA"
res = cambiar_mayusculas(m)
print(res)


