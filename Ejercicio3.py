#Ejercicio_3
def hunt_in_thedicctionary(diccionario,key):
    try: 
      key=diccionario[key]
      return key
    except KeyError:
        print(" {} no existe en el diccionario".format(key))

hunt_in_thedicctionary({ "españa":"español", "eeuu":"inglés", "italia":"italiano" },"alemania")


    