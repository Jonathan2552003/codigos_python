# def is_sorted(x):
#     lista = list(x)
#     lista_ordenada = sorted(lista)
#     if lista == lista_ordenada:
#         return True
#     else: 
#         return False
# x = "65498"
# res= is_sorted(x)
# print(res)


def is_sorted(lista):
    # Comprueba si la lista está ordenada en orden ascendente
    return lista == sorted(lista)
# Solicitar al usuario que ingrese una lista
entrada = input("Ingresa una lista de números separados por comas: ")
# Convertir la entrada en una lista de enteros
lista1 = [int(x) for x in entrada.split(',')]
# Verificar si la lista está ordenada y mostrar el resultado
if is_sorted(lista1):
    print("True")
else:
    print("False")
