import os


def ingresoAmigos():
    """
    Ingresa los datos de los amigos y los almacena
    """                    
    vacaTotal = 0
    listaAmigos = []

    nombre = input("Ingrese el nombre del amigo (* para terminar): ")       # Ingresa nombre y cuanto puso
    while nombre != "*":
        amigo = {}
        cuantoPuso = float(input("Ingrese cuanto puso: "))
        amigo["Nombre"] = nombre
        amigo["cuantoPuso"] = cuantoPuso
        listaAmigos.append(amigo)
        nombre = input("Ingrese el nombre del amigo (* para terminar): ")

    os.system("cls")
    costoTotal = int(input("Ingrese el costo total de la juntada: "))       # Ingresa costo total

    for amigo in listaAmigos:                                               # Suma cuanto puso cada uno
        vacaTotal += amigo["cuantoPuso"]

    if vacaTotal != costoTotal:
        os.system("cls")
        print("Error, los valores ingresados no son correctos. Intentelo de nuevo.\n")
        ingresoAmigos()

    costoProm = costoTotal / len(listaAmigos)                               # Calcula el costo de cada uno
    return listaAmigos, costoProm

def calculoDeudas(amigos, costoProm):
    debePlata = []
    leDebenPlata = []

    for amigo in amigos:
        if amigo["cuantoPuso"] < costoProm:
            amigo["cuantoDebe"] = costoProm - amigo["cuantoPuso"]
            amigo.pop("cuantoPuso")
            debePlata.append(amigo)

        elif amigo["cuantoPuso"] > costoProm:
            amigo["cuantoLeDeben"] = amigo["cuantoPuso"] - costoProm
            amigo.pop("cuantoPuso")
            leDebenPlata.append(amigo)

    return debePlata, leDebenPlata
            
def pagoDeDeudas(endeudados, prestamistas):
    print(endeudados)
    print(prestamistas)
    for amigo in endeudados:
        for prestamista in prestamistas:
            if amigo["cuantoDebe"] >= prestamista["cuantoLeDeben"]:  # Si debe 800 y le deben 400
                print("El amigo " + str(amigo["Nombre"]), end="")
                print(" le debe pagar a " + str(prestamista["Nombre"]) + " la cantidad de " + str(prestamista["cuantoLeDeben"]))
                amigo["cuantoDebe"] -= prestamista["cuantoLeDeben"]
                prestamista["cuantoLeDeben"] = 0
                
            

                
                


def main():
    amigos, cP = ingresoAmigos()
    debe, leDeben = calculoDeudas(amigos, cP)
    pagoDeDeudas(debe, leDeben)

main()
