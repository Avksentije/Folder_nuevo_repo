import math


def sin(x):
    if 2 * x == pi:
        print("1) Resultado de evaluar la función sin(x):")
        return 0.99999999
        
    else:
        return None


pi = 3.14 #Aquí defino el valor de pi
print(sin(pi/2)) #Aquí llamo a la función, con el argumento pi/2, por lo tanto, se evalúa desde la función

print("2) Resultado de los objetos del módulo math:")
print(math.sin(math.pi/2)) #Acá lo que hago es llamar al módulo math y sus objetos
