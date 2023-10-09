def one_away(cadena1, cadena2):
    x =len(cadena1)
    y = len (cadena2)
    contador = 0
    for i in range(len(cadena1)):
        if cadena1[i].lower() != cadena2[i].lower():
            contador += 1
         
    if contador == 1 and x == y:
        return True 
    else: 
        return False
    
w = "Hola"
q = "Hoña"
res = one_away(w, q)
print(res)