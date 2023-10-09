import random

class Grupo_de_Cartas:
    def __init__(self, cartas=[]):
        self.cartas = cartas
    
    def siguiente_carta(self):
        return self.cartas.pop(0)
    
    def tiene_carta(self):
        return len(self.cartas) > 0
    
    def cantidad(self):
        return len(self.cartas)
    
    def mezclar(self):
        random.shuffle(self.cartas)


class Cartas(Grupo_de_Cartas):
    def __init__(self):

        self.corazones = (1,2,3,4,5,6,7,8,9,10) #Baraja 1 (Lo vamos a majenar cada uno como una tupla)
        self.esapdas = (3,2,1,6,5,4,10,9,8,7)  #Baraja 2  (vamos a manejar cada uno como una tupla)
        self.cartas = [self.corazones, self.esapdas] #Aqui tenemos la baraja creada por corazones y espadas

    def siguiente_2(self):

        for i in self.cartas: #Aqui va a entrar a la lista (osea se va a parar en las tuplas)
        #Ahora tiene que entrar a cada tupla y sacar el maximo elemento 
            if i == self.corazones:
                max(self.corazones)
            
            elif i == self.esapdas:
                max(self.esapdas)

        return f"Las dos cartas superiores de la baraja son {max(self.corazones)} de corazon y {max(self.esapdas)} de epadas"
    
w = Cartas()
res_siguiente2 = w.siguiente_2()
print(res_siguiente2)
            

            







