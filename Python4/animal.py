from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def mover(self):
        pass
    
    @abstractmethod
    def emitir_sonido(self):
        print("Animal dice: ")