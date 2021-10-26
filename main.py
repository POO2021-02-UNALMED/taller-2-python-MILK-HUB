class Asiento:
    def __init__(self,color,precio,registro):
        self.color=color
        self.precio=precio
        self.registro=registro

    def cambiarColor(self, color):
        Lista_Colores = ["rojo","verde","amarillo","negro","blanco"]
        if color in Lista_Colores:
            self.color = color



class Auto:
    cantidadCreados = 0
    def __init__(self,modelo,precio,asientos,marca,motor,registro):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.motor=motor
        self.registro=registro

    def cantidadAsientos(self):

        contador=0
        for i in self.asientos:
            if (i!=None):

                contador+=1

        return contador
    
    def verificarIntegridad(self):
        if (self.registro!=self.motor.registro):
            return "Las piezas no son originales"
        else:
            for i in self.asientos:
                if (i!=None and i.registro!=self.registro):
                    return "Las piezas no son originales"
            return "Auto original"           


        
class Motor:
    def __init__(self,numeroCilindros,tipo,registro):
        self.numeroCilindors = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self,NuevoRegistro):
        self.registro = NuevoRegistro
    def asignarTipo(self,tipo):
        Opciones = ["gasolina","electrico"] 
        if tipo in Opciones:
            self.tipo = tipo  











    #def __init__(self,)
     #   pass