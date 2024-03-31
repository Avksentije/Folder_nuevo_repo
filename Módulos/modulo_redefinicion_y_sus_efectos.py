from math import sin, pi

print("Acá se imprime 1.0, dado que usamos las entidades directamente importadas del módulo: ")
print(sin(pi / 2))

pi = 3.14


print("Al momento de definir la función, usamos la variable que nosotros añadimos al código: pi = 3.14")
print("Por lo tanto, al llamar a la función, obtenemos el Return para True:", "\n(Return 0.9999999): ")
def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


print(sin(pi / 2))



#Línea 01: La instrucción from math import sin, pi importa las funciones sin() y la constante pi del módulo math.

#Línea 03: Imprime el resultado de sin(pi / 2), que usando el valor de pi de la biblioteca math, da como resultado 1.0, que es el valor correcto de seno de pi/2.

#Líneas 05 a 12: Se redefine pi y sin() en el código. pi ahora es 3.14 en lugar de su valor original de math.pi, y sin() ahora tiene una implementación personalizada. Esta redefinición anula las definiciones originales importadas.

#Línea 15: Llama a la función sin() con pi / 2. La función sin() definida localmente devuelve 0.99999999, ya que la condición 2 * x == pi se cumple cuando x es pi / 2. Por lo tanto, esta rama del condicional se ejecuta y devuelve 0.99999999