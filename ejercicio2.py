try:
    cantidad_alumno = int(input('Ingrese la cantidad de Alumnos: '))
    costo_fijo = 4000
    
    if cantidad_alumno >= 100:
        costo_alumno = 65
    elif 50 <= cantidad_alumno <= 99:
        costo_alumno = 70
    elif 30 <= cantidad_alumno <= 40:
        costo_alumno = 95
    costo_total = (cantidad_alumno * costo_alumno)
    print (f'El costo total es de : ${costo_total}')
    if cantidad_alumno <30:
        costo_fijo
        print(f'El costo es : ${costo_fijo}')
except:
    if cantidad_alumno == 0:
        print('Ingrese un numero mayor a 0')
    elif cantidad_alumno == '':
        print('ingrese un numero')