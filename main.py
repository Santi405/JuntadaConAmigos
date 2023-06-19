import os
import sys

def ingresoAmigos():
    """
    Ingresa los datos de los amigos y los almacena en una lista de diccionarios
    """                    
    vacaTotal = 0
    listaAmigos = []

    nombre = input("Ingrese el nombre del amigo (* para terminar): ")       # Ingresa nombre y cuanto puso
    while nombre != "*":
        amigo = {}
        cuantoPuso = float(input(f"Ingrese cuanto puso {nombre}: "))
        amigo["Nombre"] = nombre
        amigo["cuantoPuso"] = cuantoPuso
        listaAmigos.append(amigo)
        nombre = input("Ingrese el nombre del amigo (* para terminar): ")

    return listaAmigos

def calculoCosto(listaAmigos):
    """
    Calcula el costo promedio de la juntada y compara el costo total con la cantidad juntada por los amigos.
    """
    clear()
    vacaTotal = 0
    costoTotal = int(input("Ingrese el costo total de la juntada: "))       # Ingresa costo total

    for amigo in listaAmigos:                                               # Suma cuanto puso cada uno
        vacaTotal += amigo["cuantoPuso"]

    if vacaTotal != costoTotal:
        clear()
        print("Error, los valores ingresados no son correctos. Ingrese los valores de nuevo.\n")
        ingresoAmigos()

    costoProm = costoTotal / len(listaAmigos)                               # Calcula el costo de cada uno
    return costoProm

def calculoDeudas(amigos, costoProm):
    """
    Calcula deudas y devuelve dos listas de diccionarios, una con los amigos que pusieron de menos (ratas) y una con los amigos que pusieron de más (prestamistas)
    """
    debePlata = []
    leDebenPlata = []

    for amigo in amigos:
        if amigo["cuantoPuso"] < costoProm:
            amigo["cuantoDebe"] = round(costoProm - amigo["cuantoPuso"], 2)
            amigo.pop("cuantoPuso") 
            debePlata.append(amigo)

        elif amigo["cuantoPuso"] > costoProm:
            amigo["cuantoLeDeben"] = round(amigo["cuantoPuso"] - costoProm, 2)
            amigo.pop("cuantoPuso")
            leDebenPlata.append(amigo)

    return debePlata, leDebenPlata
            
def pagoDeDeudas(endeudados, prestamistas):
    """
    Indica quien le debe a quien y cuanto
    """
    for rata in endeudados:
        for prestamista in prestamistas:
            if rata["cuantoDebe"] >= prestamista["cuantoLeDeben"]:
                print(f"El amigo {rata['Nombre']} le debe pagar a {prestamista['Nombre']} ${prestamista['cuantoLeDeben']}")
                rata["cuantoDebe"] -= prestamista["cuantoLeDeben"]
                prestamista["cuantoLeDeben"] = 0
            else:
                print(f"El amigo {rata['Nombre']} le debe pagar a {prestamista['Nombre']} ${rata['cuantoDebe']}")
                prestamista["cuantoLeDeben"] -= rata["cuantoDebe"]
                rata["cuantoDebe"] = 0
                
def clear():
    if sys.platform == "linux":
        os.system("clear")
    elif sys.platfrom == "nt":
        clear()


listaAmigos = ingresoAmigos()
costoPromedio = calculoCosto(listaAmigos)
debe, leDeben = calculoDeudas(listaAmigos, costoPromedio)

pagoDeDeudas(debe, leDeben)

