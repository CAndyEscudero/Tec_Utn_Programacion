# Solicitar entrada del usuario
kg_uvas = int(input("Ingrese los kilos de uva: "))
tipo = input("Ingrese el tipo (A o B): ").upper()
tamano = int(input("Ingrese el tamaño (1 o 2): "))
precio_inicial = float(input("Ingrese el precio inicial por kilo: "))

# Inicializar la variable de ganancia por kilo
ganancia_por_kilo = None

# Determinar la ganancia por kilo
if tipo == "A":
    if tamano == 1:
        ganancia_por_kilo = 0.20
    elif tamano == 2:
        ganancia_por_kilo = 0.30
    else:
        print("Error: Tamaño inválido. Debe ser 1 o 2.")
elif tipo == "B":
    if tamano == 1:
        ganancia_por_kilo = -0.30
    elif tamano == 2:
        ganancia_por_kilo = -0.50
    else:
        print("Error: Tamaño inválido. Debe ser 1 o 2.")
else:
    print("Error: Tipo inválido. Debe ser A o B.")

# Calcular y mostrar la ganancia si es válida
if ganancia_por_kilo is not None:
    precio_final = precio_inicial + ganancia_por_kilo
    total = precio_final * kg_uvas
    print(f"La ganancia total por {kg_uvas} kilos de uva es: ${total:.2f}")