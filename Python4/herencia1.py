class Padre: # Superclase
    def __init__(self):
        self.apellido = "Volpin"
    def llevar(self):
        print("Papá me lleva al colegio.")
        
class Hijo(Padre): # Subclase
    def estudiar(self):
        print("Estoy en el colegio.")
        
#main        
hijo1 = Hijo() # Instanciamos hijo1
hijo1.llevar() # Papá me lleva al colegio.
hijo1.estudiar() # Estoy estudiando
print(hijo1.apellido)

# padre1=Padre()
# print(padre1.apellido)