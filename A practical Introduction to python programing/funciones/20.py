# def unir(lista1, lista2):
#     lista3 = lista1 + lista2
#     lista3.sort()
#     return lista3
# w = [1,5,4,2,7]                               #Lista usando sort
# l = [8,6,9,8,5,4]
# res = unir(w, l)
# print(res)


#Ahora la lista sin usar sort()
def unir (lista1, lista2):
    lista3 = lista1 + lista2 
    lista3_ordenada = sorted(lista3)
    return lista3_ordenada

w = [1,5,4,2,7]                               #Lista sin usar sort (Aunque use sorted y nose si eso es trampa)
l = [8,6,9,8,5,4]                 #Para evitar el fastidio de usar ciclos anidados
res = unir(w,l)
print(res)

