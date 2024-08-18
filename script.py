def calcular_ganancia(precio_inicial, tipo, tamano):
    if tipo == 'A':
        if tamano == 1:
            ganancia = precio_inicial + 0.20
        elif tamano == 2:
            ganancia = precio_inicial + 0.30
        else:
            raise ValueError("Tamaño inválido para tipo A. Debe ser 1 o 2.")
    elif tipo == 'B':
        if tamano == 1:
            ganancia = precio_inicial - 0.30
        elif tamano == 2:
            ganancia = precio_inicial - 0.50
        else:
            raise ValueError("Tamaño inválido para tipo B. Debe ser 1 o 2.")
    else:
        raise ValueError("Tipo inválido. Debe ser 'A' o 'B'.")
    
    return ganancia

def main():
    try:
        precio_inicial = float(input("Ingrese el precio inicial por kilo de uva: "))
        tipo = input("Ingrese el tipo de uva (A o B): ").upper()
        tamano = int(input("Ingrese el tamaño de la uva (1 o 2): "))
        
        ganancia = calcular_ganancia(precio_inicial, tipo, tamano)
        print(f"La ganancia por kilo de uva es: ${ganancia:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()