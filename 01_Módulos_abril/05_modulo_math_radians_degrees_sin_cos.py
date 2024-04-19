from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)


#Además de las funciones circulares (enumeradas anteriormente), el módulo math también contiene un conjunto de sus análogos hiperbólicos:

#sinh(x) → el seno hiperbólico.
#cosh(x) → el coseno hiperbólico.
#tanh(x) → la tangente hiperbólico.
#asinh(x) → el arcoseno hiperbólico.
#acosh(x) → el arcocoseno hiperbólico.
#atanh(x) → el arcotangente hiperbólico.