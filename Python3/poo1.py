class Perro:
    contador=0
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        Perro.contador+=1
        self.id=Perro.contador

    def __del__(self):
        print('El perro fue adoptado')
        Perro.contador-=1

    def __str__(self):
        return "Soy " + str(self.nombre)+ " y tengo: "+ str(self.edad)+ " ID: "+ str(self.id)
    def cumplir(self):   
        self.edad+=1
    
# perro1=Perro("Ron",2)
# # print(perro1.nombre," tiene: ",perro1.edad)
# perro2=Perro("Luna",11)
# # print(perro2.nombre," tiene: ",perro2.edad)
# # print(perro1)
# # # print(perro2)
# # perro1.cumplir()
# # perro1.cumplir()
# # print(perro1)
# print(perro2)
# perro2.edad=9
# print(perro2)

def cargar_mascotas():
    lista=[]
    nombre=input("Ingrese nombre: ")
    while nombre!="":
        edad=int(input("Ingrese edad: "))
        perro=Perro(nombre,edad)
        lista.append(perro)
        nombre=input("Ingrese nombre: ")
    return lista

def mostrar_lista(lista):
    for elem in lista:
        print(elem)
        
mascotas=cargar_mascotas()
# print(mascotas)
mostrar_lista(mascotas)

# print(mascotas[1])
# print(Perro.contador)

del mascotas[1]
mostrar_lista(mascotas)