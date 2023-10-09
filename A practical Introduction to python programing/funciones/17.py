# def primos(n):
#     if n<=1:
#         return "Su numero es invalido"
#     lista = []

#     for i in range(2, n+1):
#         es_primo=True

#         for j in range(2,i):
#             if i%j == 0:
#                 es_primo = False
#                 break
        
#         if es_primo:
#             lista.append(i)
#     return lista    
# w = 10
# res = primos(w)
# print(res)
    
            
def primos(n):
    lista = []
    i = 2
    while n>len(lista):
        es_primo = True
        for j in range(2,i):
            if i%j ==0:
                es_primo = False
                break
        if es_primo == True:                   ###ESTUDIARLO UN RESTOOOO
            lista.append(i)
        i +=1
    return lista
w = 15
res =primos(w)
print(res)
                     
