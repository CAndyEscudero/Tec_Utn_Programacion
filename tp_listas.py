'''
Ejercicio 6: Reescribe el programa que pide al usuario una lista de
números e imprime el máximo y el mínimo de los números al final cuando
el usuario ingresa “hecho”. Escribe el programa para almacenar los
números que el usuario ingrese en una lista, y utiliza las funciones max()
y min() para calcular el máximo y el mínimo después de que el bucle
termine.'''

lista=[]
numeros=0
while numeros!="hecho":
    numeros=input("Ingrese los numeros y al finalizar escriba, 'hecho': ")
    b = numeros
    if numeros!="hecho":
        try:
            numeros = int(b)
            lista.append(numeros)
        except:
            print("entrada no valida")
            continue

print("valor maximo: ", max(lista))
print("valor minimo: ", min(lista))