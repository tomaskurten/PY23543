class Padre: # Superclase 1
 def llevar(self):
    print("Papá me lleva al colegio.")
    
class Madre: # Superclase 2
 def programar(self):
    print("Mamá programa en Python.")
    
class Hijo(Padre,Madre): # Subclase
 def amar(self):
    print("Quiero a mis padres")
    
hijo1 = Hijo() # Instanciamos hijo1
hijo1.llevar() # Papá me lleva al colegio.
hijo1.programar()# Mamá programa en Python.
hijo1.amar() 