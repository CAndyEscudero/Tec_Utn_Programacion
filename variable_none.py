cantidad_ciudades = int(input("Ingrese la cantidad de ciudades: "))
cantidad_tiendas = int(input("Ingrese la cantidad de tiendas por ciudad: "))
cantidad_empleados = int(input("Ingrese la cantidad de empleados por tienda: "))

total_cadenas = 0

for ciudad in range(cantidad_ciudades):
    total_ciudad = 0
    print(f"Ciudad {ciudad + 1}:")
    
    for tienda in range(cantidad_tiendas):
        total_tienda = 0
        print(f"  Tienda {tienda + 1}:")
        
        for empleado in range(cantidad_empleados):
            ventas_empleado = float(input(f"    Ingrese el monto vendido por el empleado {empleado + 1}: "))
            total_tienda += ventas_empleado
        
        print(f"    Total vendido en la tienda {tienda + 1}: ${total_tienda:.2f}")
        total_ciudad += total_tienda
    
    print(f"  Total vendido en la ciudad {ciudad + 1}: ${total_ciudad:.2f}")
    total_cadena += total_ciudad

print(f"Total vendido en la cadena: ${total_cadena:.2f}")
