#CONVERTIDOR DE TIEMPO:

class Tiempo: 
    def __init__(self, tiempo_en_segundos):
        self.tiempo_en_segundos = tiempo_en_segundos

    def tiempo_en_minutos(self):
        minutos = self.tiempo_en_segundos // 60 #Minutos exactos
        segundos = self.tiempo_en_segundos % 60 #Los segundos que sobraron
        return f"Los {self.tiempo_en_segundos} convetidos a minutos en orden m:s {minutos}:{segundos}"
    
    def tiempo_en_horas(self):
        horas = self.tiempo_en_segundos//3600 #Horas exactas
        minutos = self.tiempo_en_segundos//60 - horas*60
        segundos = self.tiempo_en_segundos % 60
        return f"Los {self.tiempo_en_segundos} convertidos a horas quedan en orden h:m:s {horas}:{minutos}:{segundos}"

w = Tiempo(500)
res_minutos = w.tiempo_en_minutos()
res_horas = w.tiempo_en_horas()
print(res_minutos)
print()
print(res_horas)