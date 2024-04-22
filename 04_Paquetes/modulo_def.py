#!/usr/bin/env python3 

""" module.py - Un ejemplo de un módulo en Python """

__counter = 0  #mi variable


def suml(the_list):
    global __counter
    __counter += 1
    the_sum = 0   #segunda variable contadora, inicializada en 0
    for element in the_list:  #ciclo for, iniciando en el primer elemento de lalista
        the_sum += element
    return the_sum   #volvemos a usar resume porque estamos dentro de una función


def prodl(the_list):
    global __counter    
    __counter += 1
    prod = 1   #tercera variable contadora, inicializada en 1
    for element in the_list:
        prod *= element
    return prod


if __name__ == "__main__":  #comparo el nombre de main y una vez se compare y sea True, se inicia la serie de comandos; detecta cuando se ejecuta el archivo de forma independiente.
    print("Yo prefiero ser un módulo, pero puedo realizar algunas pruebas por ti")
    my_list = [i+1 for i in range(5)] #el rango recordemos es 0, 1, 2, 3, 4 
    print(suml(my_list) == 15)  #Comparación función  1
    print(prodl(my_list) == 120) #Comparación funcion 2

