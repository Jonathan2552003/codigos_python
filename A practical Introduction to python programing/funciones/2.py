def add(n):

    lista = [] #Lista vacia para empezar a guardar elementos
    palabras = n.split() #Converte las cadenas en lisra separas por palabras
    for palabra in palabras: #La variable palabra se conveirte en cada objeto de la lista recorriendolos todos
        lista.append(palabra + "!") #agrega al final de la lista que definimos mas arriba la palabra mas el signo !
    return lista

entrada_usuario = input("Ingrese una lista   ")
resultado = add(entrada_usuario)
print(resultado) 

                       ####ESTUDIAR MUCHOOOOOOO