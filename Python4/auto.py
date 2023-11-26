from vehiculo import Vehiculo

class Auto(Vehiculo):
    def __init__(self, color,ruedas,cilindrada):
        Vehiculo.__init__(self,color,ruedas)
        self.cilindrada=cilindrada
    def __str__(self):
        return super().__str__() + ", Cilindrada: "+str(self.cilindrada)
    
    def mover(self):
        print("Estado del auto: ")
        super().avanzar()
        
    
auto1=Auto("rojo",4,1200)
print(auto1)
auto1.mover()