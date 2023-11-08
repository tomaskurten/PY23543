diccionario={"Tomas":31,"Ana":22,"Juan":17}
# print(diccionario)
# print(diccionario.keys())
# print(diccionario.values())

# print(diccionario["Tomas"])

for clave in diccionario:
    # print(clave)
    if diccionario[clave]>=18:
        print(clave," es mayor de edad")
    else:
        print(clave," es menor de edad")