import random

'''Ejercicio 1: Ejecuta el programa en tu sistema y observa qué números
obtienes.
La función random es solamente una de las muchas que trabajan con números
aleatorios. La función randint toma los parámetros inferior y superior, y
devuelve un entero entre inferior y superior (incluyendo ambos extremos).'''

for i in range(5):
    x = random.randint(5, 10)
    print(x)

