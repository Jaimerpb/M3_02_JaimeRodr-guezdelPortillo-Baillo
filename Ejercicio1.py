
#Ejercicio_1,numero=7/0
#consideramos la excepcion(cuando el denominador es igual a 0) para que se siga ejecutando código
def division(numerador,denominador):
    try:
        numero=numerador/denominador
        return numero
    except ZeroDivisionError:
        return "No se puuede dividir entre O"

division(7,0)            


if __name__ =="__main__":
    main()







