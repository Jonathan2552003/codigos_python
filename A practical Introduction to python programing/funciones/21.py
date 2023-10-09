def busqueda_binaria(lista, valor):
    
    valor_inicial = 0
    valor_final = len(lista)-1
    while valor_inicial <= valor_final:
        valor_medio = (valor_inicial + valor_final)//2
        palabra_media = lista[valor_medio]
        if palabra_media == valor:
            return True                                       #Volverlo a hacer
        if palabra_media < valor: 
            valor_inicial = valor_medio+1
        else: 
            valor_inicial = valor_medio-1
    return False
w = [1,2,3,4,5,6,7,8,9]
l = 10
res = busqueda_binaria(w, l)
print(res)

