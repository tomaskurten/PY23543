from animal import Animal

class Perro(Animal):
    def mover(self):
        print("perro se mueve")
    
    def emitir_sonido(self):
        super().emitir_sonido()
        print("Guau!")
        
# perro1=Perro()
# perro1.mover()
# perro1.emitir_sonido()