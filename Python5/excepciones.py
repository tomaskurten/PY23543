while True:
    try:
        num1=int(input("ingrese numero 1 "))
        num2=int(input("ingrese numero 2 (por favor que no sea 0) "))
        resultado=num1/num2
        print(resultado)
        break
    except ZeroDivisionError:
        print("error, 0 no!!")
    except ValueError:
        print("error, tiene que ser un numero!")
    except:
        print("ERROR ocurrió algun error")
    finally:
        print("finally")
    
print("seguimos con el programa")
