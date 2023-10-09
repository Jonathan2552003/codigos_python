#VAMOS A HACER EL JUEGO DE PIEDRA PAPEL O TIEJRA

import random 

class Pierda_papel_o_tijera:
    def __init__(self,n):
     
        self.juego = ["piedra", "papel", "tijera"]
        self.numero_de_rondas = n
     
    def ejecucion_juego(self):

        ganadas_jugador = 0 #Aqui vamos a almacenar las partidas ganadas del jugador
        ganadas_computador = 0 #Aqui vamos a almacenar las partidas ganadas del computador

        for i in range(self.numero_de_rondas):

            print(f"Partida numero {i+1}")
            jugador = input("Ingrese una de las 3 opciones, piedra, papel o tijera  ")
            computador = random.choice(self.juego)

            if jugador == computador:
                print(f"Esta ronda quedo empatada porque el computador saco {computador}")

            elif jugador.lower() == "piedra" and computador.lower() == "tijera" or jugador.lower() == "papel" and computador.lower() == "piedra" or jugador.lower() == "tijera" and computador.lower() == "palel":
                ganadas_jugador += 1
                print(f"Felicitaciones, usted gano esta ronda porque el computador saco {computador}")

            else:
                ganadas_computador+=1
                print(f"Lamnetamos que esta ronda la perdio porque el computador saco {computador}")

            
        if ganadas_jugador > ganadas_computador:
            return f"Felicidades, usted gano el juego con {ganadas_jugador} rondas ganadas"
        
        elif ganadas_jugador < ganadas_computador:
            return f"Lamentamos decirle que usted ha peridod el juego con {ganadas_computador} rondas perdidas"
        
        else: 
            return "El juego quedo en un empate"

w = Pierda_papel_o_tijera(3)
res_juego = w.ejecucion_juego()
print(res_juego)

            