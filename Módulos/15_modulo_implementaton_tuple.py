from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)

#Cadena de implementación de Python
#La parte mayor de la versión de Python.
#La parte menor.
#El número del nivel de parche.