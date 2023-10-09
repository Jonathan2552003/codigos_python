class Inversion:
    def __init__(self, p, i):
        self.principal = p
        self.interes = i

    def valor_despues(self,n):
        return self.principal*(1+self.interes)**n 
    
    def __str__(self):
        return f" principal - ${self.principal: .2f}, tasa de interes - {self.interes * 100:.2f}%"

inversion = Inversion(1000, 0.0512)
print(inversion)
print(inversion.valor_despues(5)) #Inversion despues de 5 años

