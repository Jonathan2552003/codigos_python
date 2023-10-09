class Juego_de_palabras:
    def __init__ (self, lista_de_palabras):
        self.lista_de_palabras = lista_de_palabras

    #def longitud (self) longitud
    #NOSE QUE PUTAS TOCA HACER
    
    def empiezan_con_s(self):
        lista_s = []  #Donde se van a acumular las palabras que empiezan con s
        for char in self.lista_de_palabras:
            if char[0].lower() == "s":
                lista_s.append(char)
        return lista_s
    
    def termina_con_s(self):
        lista_s = [] #Aqui se almacenan las palabras que terminan con s
        for char in self.lista_de_palabras:
            if char[-1].lower() == "s":
                lista_s.append(char)
        return lista_s
    
    def palindromo(self):
        lista_palindromo = []  #Aqui se almacenan las palabras que son palindromos
        for char in self.lista_de_palabras:
            if char.lower() == char.lower() [ : :-1]:
                lista_palindromo.append(char)
        return lista_palindromo
    
    def palabras_con_l(self):
        lista_palabras_con_l = []
        for char in self.lista_de_palabras:
            for i in char.lower():
                if i == "l":
                    lista_palabras_con_l.append(char)
                    break
        return lista_palabras_con_l
    
    def palabras_sin_l(self):
        palabra_sin_l = True
        lista_sin_l = []
        while palabra_sin_l:
            for char in self.lista_de_palabras:
                for i in char.lower():
                    if i == "l":
                        palabra_sin_l = False
                        break
                if palabra_sin_l == True:
                    lista_sin_l.append(char)
        return lista_sin_l




w = Juego_de_palabras(["Sapo", "Perro", "Gato", "sapoperro", "Cacas", "oso", "Lagarto", "lagartija", "llorar"])
res_empieza_con_s = w.empiezan_con_s()
res_termina_con_s = w.termina_con_s()
res_palindromo = w.palindromo()
res_palabras_con_l = w.palabras_con_l()
res_palabras_sin_l = w.palabras_sin_l()
print(res_empieza_con_s)
print()
print(res_termina_con_s)
print()
print(res_palindromo)
print()
print(res_palabras_con_l)
print()
print(res_palabras_sin_l)