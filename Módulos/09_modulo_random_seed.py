from random import random, seed

seed(0)

for i in range(5):
    print(random())


#La función seed() es capaz de directamente establecer la semilla del generador.
#Acá dos de sus variantes:
    
    # seed() - establece la semilla con la hora actual.
    # seed(int_value) - establece la semilla con el valor entero int_value


#El valor de la semilla inicial, establecido durante el inicio del programa,
    #determina el orden en que aparecerán los valores generados.

#El factor aleatorio del proceso puede ser aumentado al establecer la semilla tomando un número de la hora actual
    # - esto puede garantizar que cada ejecución del programa comience desde un valor semilla diferente 
    # (por lo tanto, usará diferentes números aleatorios).