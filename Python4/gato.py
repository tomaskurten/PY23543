from animal import Animal

class Gato(Animal):
    def mover(self):
        print("gato se mueve")
    
    def emitir_sonido(self):
        super().emitir_sonido()
        print("Miau!")
        
    def razguñar(self):
        print("gato razguña")
# gato1=Gato()
# gato1.mover()
# gato1.emitir_sonido()