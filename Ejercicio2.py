#Ejercicio_2
#Consideramos la excepción IndexError,para cuando el 
#índice al que se intente acceder este fuera de rango 
def hunt_in_thelist(lista,index):
    try:
        elemento=lista[index]
        return elemento
    except IndexError:
        print("El índice {} está fuera del rango de la lista".format((index)))

hunt_in_thelist([4, 7, 30, 23, 5], 10)

if __name__=="__main__":
    main()










