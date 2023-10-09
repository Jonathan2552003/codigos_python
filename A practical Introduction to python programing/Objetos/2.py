class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre 
        self.cantidad = cantidad
        self.precio = precio

    def obtener_precio(self, cantidad_a_comprar):
        if cantidad_a_comprar<10:
            return cantidad_a_comprar*self.precio
        
        elif 10<= cantidad_a_comprar <=99:
            return cantidad_a_comprar*self.precio*0.90
        
        else:
            return cantidad_a_comprar*self.precio*0.80
        
    def realizar_compra(self, stok):
        stok = self.cantidad-cantidad_a_comprar_deseada
        return stok
        
       
producto = Producto("papas", 50, 5000)
cantidad_a_comprar_deseada = 5 
costo = producto.obtener_precio(cantidad_a_comprar_deseada) #Aqui se llama al producto de variable, no al producto de la clase
stok_restante = producto.realizar_compra(cantidad_a_comprar_deseada) #En funciones usabamos w, luego res = nombre de la funcion(w) e imprimiamos res
print("El costo es", costo) 
print("La cantidad que queda en stok es:", stok_restante)
