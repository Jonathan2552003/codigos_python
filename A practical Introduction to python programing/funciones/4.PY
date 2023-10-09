#Raiz digital
def digitos (numero):
    while numero > 10: #Si el numero es mayor que diez inicie un ciclo (indefinido, hasta que numero <10)
        suma = 0 #Esta es una variable que va a almacenar las suma de los digitos
        while numero > 0: #Si el numero tambien es mayor a cero entre a este otro bucle
            digito = numero % 10 #Creo una variable extra que es digito, es para que me haga las operaciones, el modulo es para sacar el ultimo numero
            suma += digito
            numero//= 10 #Esta linea sirve para eliminar el ultimo digito de la derecha
        numero = suma 
    return suma

n = int(input("Ingrese un numero entero:  "))   #NOSE PORQUE SOLO SOLO LE DEFINO n SI FUNCIONA SI NUNCA USO ESA VARIABLE
res = digitos(n)
print("Su raiz digital es:  ", res)
