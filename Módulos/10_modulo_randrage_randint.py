from random import randrange, randint

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))

print(randrange(10), end=' ')
print(randrange(-9, 9), end=' ')
print(randrange(0, 10, 2), end=' ')
print(randint(-10, 10))


#randrange(fin)
#randrange(inico, fin)
#randrange(inicio, fin, incremento)
#randint(izquierda, derecha)

#La última función es equivalente a randrange(izquierda, derecha+1) 
#Genera el valor entero i, el cual cae en el rango [izquierda, derecha] (sin exclusión en el lado derecho).