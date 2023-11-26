class Vehiculo():
    def __init__(self,color,ruedas):
        self.color=color
        self.ruedas=ruedas
    
    def __str__(self):
        cadena="Color: "+self.color+", Ruedas: "+str(self.ruedas)
        return cadena

    def avanzar(self):
        print("avanzando...")