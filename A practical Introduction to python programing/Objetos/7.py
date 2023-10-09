
import random
class Cubierta_estandar:


    def __init__(self, baraja):
        #Definimoslas barajas como una lista
        self.baraja = baraja
        random.shuffle(self.baraja) #Revuelve las caratas

        #Definimos las baras como la cantidad de elementos de la lista ya que cada elemento es una carta
        cantidad_de_cartas = len(self.baraja)
        mitad = cantidad_de_cartas //2


        #Definimos las cartas que tendra cada jugador
        self.jugador_1 = baraja[mitad:] #El primer jugador tendra la mitad de la baraja hasta el final
        self.jugador_2 = baraja[:mitad]  #El segundo tendra desde el primer elemento hasta la mitad

    def guerra_de_cartas(self):
        ganadas_jugador_1 = [] #Aqui es donde vamos a almacenar las cartas del jugador 1
        ganadas_jugador_2 = [] #Aqui almacenamos las cartas del jugador 

        while self.jugador_1 and self.jugador_2:
            
            carta_jugador_1 = self.jugador_1.pop()
            carta_jugador_2= self.jugador_2.pop()

            if carta_jugador_1 > carta_jugador_2:
                ganadas_jugador_1.append(carta_jugador_1)
            if carta_jugador_1 <carta_jugador_2:
                ganadas_jugador_2.append(carta_jugador_2)

        if len(ganadas_jugador_1) > len(ganadas_jugador_2):
            return "El ganador es el jugador1"

        else: 
            return "El ganador es el jugador2"

w = Cubierta_estandar([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
res_guerra_de_cartas = w.guerra_de_cartas()
print(res_guerra_de_cartas)


