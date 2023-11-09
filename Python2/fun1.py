# def fun1():
#     print("adentro de la funcion")

# fun1()
# print("afuera")

# def sumar(x,y):
#     return x+y

# a=4
# b=9
# c=sumar(a,b)
# print(c)


# parametros por defecto
# print("primero ",end=" ")
# print("segundo")



# def raiz(x,r=2):
#     print(pow(x,1/r))
    
# a=100
# raiz(a,3)


# def fun2(x,y):
#     x=4
#     y=4
#     print(x)
#     print(y)
#     return x,y

# #main    
# a=1
# b=2
# c,d=fun2(a,b)
# print(c)
# print(d)
# # print(a)
# # print(a)


# ##paso por referencia
# def duplicar_lista(lista):
#     for i in range(len(lista)):
#         lista[i]=lista[i]*2
        
# numeros=[1,7,3,1,9]
# palabras=["perro","gato","pato"]

# duplicar_lista(numeros)
# # print()
# # print("segundo llamado: ")
# duplicar_lista(palabras)

# print(numeros)

# print(palabras)


# def fun3(num):
#     if num%2==0:
#        resultado= "par"
#     else:
#         resultado="impar"
#     return resultado
    
# print(fun3(4))


# def calcular(n = 1):
#  tabla = []
#  for i in range(0,11):
#     tabla.append(f"{n}x{i}={n*i}")
#     # tabla.append(n,"x",i,"=",n*i)
#  return tabla


# # Muestra en terminal todas las tablas
# def calcular_todas():
#  for i in range(0,11):
#     print(f"Tabla del {i}:")
#     tabla = calcular(i)
#     for j in tabla:
#         print(j)
#         print("-"*10)
# #Programa principal

# #main
# print(calcular())


# ###lambda
# sumar = lambda x,y: x + y
# print(sumar(4,2))


enteros = [1, 2, 4, 7]
duplica_lista = list(map(lambda x : x * 2, enteros))
print(duplica_lista) 