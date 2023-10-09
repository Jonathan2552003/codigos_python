class Administrador_de_contraseñas:
    def __init__(self, contraseñas_anteriores,ultima_contraseña):
        self.contraseña_anterior = contraseñas_anteriores #Aqui se almacenan las contraseñas
        self.ultima_contraseña = ultima_contraseña   #Esta es la variable de la ultima contraseña


    def obtener_contraseñas(self):
        if self.contraseña_anterior: #Si hay contraseñas anteriores
            contraseña_actual = self.contraseña_anterior.pop()
            return contraseña_actual
        else: 
            return "No hay contraseñas anteriores"
        
    def establecer_contraseña(self,nueva_contraseña):
        self.nueva_contraseña = input("Ingrese una nueva contraseña:  ")
        for contraseña in self.contraseña_anterior:
            if nueva_contraseña == contraseña:
                return "Ingrese una contraseña que no haya usado antes"
            
            self.ultima_contraseña = nueva_contraseña
            return self.ultima_contraseña

contraseñas = Administrador_de_contraseñas(["30268685", "8717"], "8717")
actual_contraseña = contraseñas.obtener_contraseñas()
restablecer = contraseñas.establecer_contraseña("Su contraseña se actualizo de forma correcta")
print(actual_contraseña)
print()
print(restablecer)