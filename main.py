
class Asiento:
    def __init__(self,color,precio,registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        Lista_Colores = ["rojo","verde","amarillo","negro","blanco"]
        if color in Lista_Colores:
            self.color = color



class Auto:
    cantidadCreados = 0
    def __init__(self,modelo,precio,asientos,marca,motor,registro):
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
        mensaje = 'Auto original'

        if self.registro == self.motor.registro :
            for asiento in self.asientos:
                #if isinstance(asiento, list):
                if type(asiento) == Asiento:
                    if asiento.registro != self.registro:
                        mensaje = 'Las piezas no son originales'
        else:
            mensaje = 'Las piezas no son originales'
        
        return mensaje

        
class Motor:
    def __init__(self,numeroCilindros,tipo, registro):
        self.numeroCilindors = numeroCilindros
        self.tipo = tipo
        self.regsitro = registro

    def cambiarRegistro(self,NuevoRegistro):
        self.registro = NuevoRegistro
    def asignarTipo(self,tipo):
        Opciones = ["gasolina","electrico"] 
        if tipo in Opciones:
            self.tipo = tipo  











    #def __init__(self,)
     #   pass