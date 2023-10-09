""" ESTE ES UN BLA BLA BLA BLA PARA QUE NO SALGA ERROR ¿OK?"""

def primera_diferencia(cadena1,cadena2):
    if cadena1.lower() == cadena2.lower():
        return "Son iguales"
    

    else: 
        for i in range(len(cadena1)):
            if cadena1[i].lower() != cadena2[i].lower():
                break


        return "La diferencia esta en la posicion", i
            
c = str(input("Ingrese una cadena:   "))
c2= str((input("Ingrese otra cadena:  ")))
difernecia = primera_diferencia(c, c2)
print(difernecia)