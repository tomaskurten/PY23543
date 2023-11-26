class Mascota: 
    def __init__(self,nombre,raza): 
          self.__nombre = nombre    #oculto este dato
          self.__raza = raza
          self.edad=0
    
    @property
    def nombre(self): #metodo que es una propiedad
        return self.__nombre
    @nombre.setter
    def nombre(self,nombre):
        if nombre !="" and type(nombre)==str:   #creo un control para los datos
            self.__nombre=nombre
        else:
            print("error, nombre tiene que ser str y no vacio")
            
    @property
    def raza(self): #metodo que es una propiedad
        return self.__raza
    @raza.setter
    def raza(self,raza):
        if raza !="" and type(raza)==str:   #creo un control para los datos
            self.__raza=raza
        else:
            print("error, raza tiene que ser str y no vacio")
        
    def __str__(self):
        cadena="El perro "+self.__nombre+", es de raza "+ self.__raza
        return cadena

m1=Mascota("Luna","mestizo")
# m1.raza=1
# m1.raza=""
# # print(m1.__nombre) #creo otra variable distinta
# print(m1.raza)
# m1.raza="callejero"
# print(m1.raza)
m1.nombre=1
m1.nombre="carlos"
print(m1.nombre)