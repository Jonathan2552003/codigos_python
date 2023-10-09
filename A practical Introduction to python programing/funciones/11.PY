#Compara las coincidencias de dos cadenas e imrpime el numero de coincidencias

def coincidencias(cadena1 , cadena2):
    lista1 = cadena1
    lista2 = cadena2
    contador = 0
    for i in lista1:
        for j in lista2:
            if i==j:
                contador+=1
    return contador 

x = input("Ingrese una cadena: ")
y = input("Ingrese otra cadena: ")
re = coincidencias(x,y)
print("El numero de coincidencias es: ", re)