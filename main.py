
class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        Lista_Colores = ["rojo","verde","amarillo","negro","blanco"]
        if color in Lista_Colores:
            self.color = color



class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        cantidadAsientos = 0
        for i in range(0, len(self.asientos)):
            if isinstance(self.asientos[i], Asiento):
                cantidadAsientos += 1
        
        return cantidadAsientos

    def verificarIntegridad(self):
        if self.motor.registro == self.registro:
            for i in range (0,len(self.asientos)):
                if type(self.asientos[i]) == Asiento and self.registro != self.asientos[i].registro:
                    return "Las piezas no son originales"
            return "Auto original"
        else:
            return "Las piezas no son originales"

        
class Motor:
    def __init__(self,numeroCilindros,tipo, registro):
        self.numeroCilindors = numeroCilindros
        self.tipo = tipo
        self.regsitro = registro

    def cambiarRegistro(self,NuevoRegistro):
        self.registro = NuevoRegistro











    #def __init__(self,)
     #   pass