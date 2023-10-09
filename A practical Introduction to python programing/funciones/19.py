def verbose(numero):
    if numero == 0:
        return "cero"

    unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    especiales = ["diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve"]
    decenas = ["", "diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
    centenas = ["", "ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]

    def convertir_miles(n):
        if n == 1:
            return "mil"
        else:
            return convertir(n) + " mil"

    def convertir_millones(n):
        return convertir(n) + " millones"

    def convertir_millar(n):
        return convertir(n) + " mil"

    def convertir(n):
        if n < 10:
            return unidades[n]
        elif n < 20:
            return especiales[n - 10]
        elif n < 100:
            decena = n // 10
            unidad = n % 10
            if unidad == 0:
                return decenas[decena]
            else:
                return decenas[decena] + " y " + unidades[unidad]
        elif n < 1000:
            centena = n // 100
            resto = n % 100
            if centena == 1 and resto == 0:
                return "cien"
            elif resto == 0:
                return centenas[centena]
            else:
                return centenas[centena] + " " + convertir(resto)
        elif n < 10000:
            millar = n // 1000
            resto = n % 1000
            if millar == 1:
                return "mil " + convertir_miles(resto)
            elif resto == 0:
                return convertir_millar(millar)
            else:
                return convertir_millar(millar) + " " + convertir_miles(resto)
        elif n < 10**6:
            miles = n // 1000
            resto = n % 1000
            return convertir_miles(miles) + " " + convertir_millar(resto)
        elif n < 10**9:
            millones = n // 10**6
            resto = n % 10**6
            return convertir_millones(millones) + " " + convertir_millar(resto)
        elif n < 10**12:
            millardos = n // 10**9
            resto = n % 10**9
            return convertir_millones(millardos) + " " + convertir_millar(resto)
        elif n < 10**15:
            billones = n // 10**12
            resto = n % 10**12
            return convertir(billones) + " billones " + convertir_millar(resto)
        else:
            return "Número demasiado grande"

    return convertir(numero)

# Ejemplo de uso:
w = 123456
nombre = verbose(w)
print(nombre)


