counter = 0

print("Este módulo imprime una frase si se cumple que __name__ == __main__")
if __name__ == "__main__":
    print("Yo prefiero ser un módulo")
    print(bool(__name__))

else:
    print("Me gusta ser un módulo")

print(__name__)

#Solo puedes informar a tus usuarios que esta es tu variable, que pueden leerla, 
#pero que no deben modificarla bajo ninguna circunstancia.

#Esto se hace anteponiendo al nombre de la variable _ (un guión bajo) o __ (dos guiones bajos),
# pero recuerda, es solo un acuerdo. Los usuarios de tu módulo pueden obedecerlo o no.