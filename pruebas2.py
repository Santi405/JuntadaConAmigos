def recolectar_datos():
    amigos = {}
    print("Ingrese los datos de los amigos.")
    agregar_mas = True
    
    while agregar_mas:
        nombre = input("Ingrese el nombre del amigo: ")
        monto = float(input(f"Ingrese el monto que {nombre} pagó: "))
        amigos[nombre] = monto
        
        opcion = input("¿Desea agregar otro amigo? (s/n): ").lower()
        if opcion != 's':
            agregar_mas = False
            
    return amigos

def modificar_importe(amigos):
    nombre = input("Ingrese el nombre del amigo cuyo importe desea modificar: ")
    if nombre in amigos:
        monto = float(input(f"Ingrese el nuevo monto que {nombre} pagó: "))
        amigos[nombre] = monto
    else:
        print("El nombre ingresado no está en la lista de amigos.")

def calcular_deudas(amigos):
    total_pagado = sum(amigos.values())
    num_amigos = len(amigos)
    pago_justo = total_pagado / num_amigos
    
    deudas = {amigo: pago_justo - monto for amigo, monto in amigos.items()}
    
    return deudas

def resolver_deudas(deudas):
    acreedores = [(amigo, -deuda) for amigo, deuda in deudas.items() if deuda < 0]
    deudores = [(amigo, deuda) for amigo, deuda in deudas.items() if deuda > 0]
    
    pagos = []
    
    while deudores and acreedores:
        deudor, monto_deudor = deudores.pop()
        acreedor, monto_acreedor = acreedores.pop()
        
        if monto_deudor > monto_acreedor:
            pagos.append((deudor, acreedor, monto_acreedor))
            deudores.append((deudor, monto_deudor - monto_acreedor))
        elif monto_deudor < monto_acreedor:
            pagos.append((deudor, acreedor, monto_deudor))
            acreedores.append((acreedor, monto_acreedor - monto_deudor))
        else:
            pagos.append((deudor, acreedor, monto_deudor))
    
    return pagos

def imprimir_pagos(pagos):
    for deudor, acreedor, monto in pagos:
        print(f"{deudor} debe pagar a {acreedor} un total de ${monto:.2f}")

def main():
    amigos = recolectar_datos()
    
    while True:
        print("\nOpciones:")
        print("1. Modificar el importe de un amigo")
        print("2. Calcular y mostrar deudas")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            modificar_importe(amigos)
        elif opcion == '2':
            deudas = calcular_deudas(amigos)
            pagos = resolver_deudas(deudas)
            imprimir_pagos(pagos)
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
