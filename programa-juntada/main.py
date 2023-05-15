def ingresoAmigos():
    listaAmigos = []

    nombre = input("Ingrese el nombre del amigo (* para terminar): ")
    while nombre != "*":
        cuantoPuso = float(input("Ingrese cuanto puso: "))
        listaAmigos.append((nombre,cuantoPuso))
        nombre = input("Ingrese el nombre del amigo (* para terminar): ")

    return listaAmigos

def cuantoDebe(amigos):
    pusoMenos = []
    pusoMas = []
    costoTotal = int(input("Ingrese el costo total de la juntada: "))
    costoProm = costoTotal / len(amigos)
    for amigo in amigos:
        if amigo[1] < costoProm:
            pusoMenos.append((amigo[0], costoProm - amigo[1]))
        elif amigo[1] > costoProm:
            pusoMas.append((amigo[0], amigo[1] - costoProm))
        else:
            print(f"{amigo[0]} puso justo, un capo.")

def main():
    amigos = ingresoAmigos()
    cuantoDebe(amigos)

main()
