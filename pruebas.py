
import os 
import sys 
from colored import fg, attr, colored

color_green = fg('green')
color_reset = attr('reset')
color_yellow = fg('yellow')


class Amigo():
    def __init__(self, nombre, dinero, deuda) -> None:
        self.nombre = nombre
        self.dinero = dinero
        self.deuda = deuda


def ingresoAmigos(): 
    """ 
     Ingresa los datos de los amigos y los almacena en una lista de diccionarios 
    """                     
    listaAmigos = [] 
    nombre = input("Ingrese el nombre del amigo (enter para terminar): " + color_yellow)       # Ingresa nombre y cuanto puso 

    while nombre != "":  
        nombresExist = [amigoExist.nombre for amigoExist in listaAmigos]

        if nombre in nombresExist:
            print("Ya pusiste ese, pelele.")
        else:
            cuantoPuso = float(input(color_reset + "Ingrese cuanto puso " + color_yellow + nombre + color_reset + ": " + color_green))
            amigo = Amigo(nombre, cuantoPuso, 0)
            listaAmigos.append(amigo) 

        nombre = input(color_reset + "Ingrese el nombre del amigo (enter para terminar): " + color_yellow) 

    return listaAmigos


def mostrarLista():
    """
    Muestra la lista de amigos y cuanto puso cada uno.
    """
    clear()

    print(color_reset + "Lista de amigos: ")
    for amigo in listaAmigos:
        print(f"El maquinola de " + color_yellow + amigo.nombre + color_reset + "\t puso " + color_green + str(amigo.dinero) + color_reset)

    opc = input("\nDesea modificar algún monto? (S/N): ").lower()

    if opc == "s":
        clear()
        modificarLista()

    clear()

def modificarLista():
    boolNombre = False #Bandera

    while not boolNombre:
        nameSearch = input("Ingrese el amigo: ")
        for i in listaAmigos:
            if nameSearch == i.nombre:
                nuevoMonto = float(input("Ingrese el nuevo monto: "))
                i.dinero = nuevoMonto
                boolNombre = True
                
                verLista = input("Desea ver la lista de nuevo? (S/N): ").lower()
                if verLista == "s":
                    mostrarLista()

        if not boolNombre:
            clear()
            print("Nombre incorrecto, intente de nuevo.")

def clear(): 
    if sys.platform == "linux": 
        os.system("clear") 
    elif sys.platform == "nt": 
        clear()


def calculoCosto(): 
    """ 
    Calcula el costo promedio de la juntada y compara el costo total con la cantidad juntada por los amigos. 
    """ 
    clear() 
    vacaTotal = 0 

    # Suma cuanto puso cada uno 
    for amigo in listaAmigos:                                               
        vacaTotal += amigo.dinero 

    # Calcula el costo de cada uno 
    costoProm = vacaTotal / len(listaAmigos)                               
    return costoProm 


def calculoDeudas(costoProm): 
    """ 
    Calcula deudas y devuelve dos listas de diccionarios, una con los amigos que pusieron de menos (ratas) y una con los amigos que pusieron de más (prestamistas) 
    """ 
    debePlata = [] 
    leDebenPlata = [] 

    for amigo in listaAmigos: 
        if amigo.dinero < costoProm: 
            amigo.deuda = costoProm - amigo.dinero
            debePlata.append(amigo) 

        elif amigo.dinero > costoProm: 
            amigo.deuda = amigo.dinero - costoProm
            leDebenPlata.append(amigo) 

    return debePlata, leDebenPlata 

def pagoDeDeudas(endeudados, prestamistas): 
    """ 
    Indica quien le debe a quien y cuanto 
    """ 
    for rata in endeudados: 
        for prestamista in prestamistas: 
            if rata.deuda != 0 and prestamista.deuda != 0:
                if rata.deuda >= prestamista.deuda: 
                    pago = str(round(prestamista.deuda, 2))
                    rata.deuda -= prestamista.deuda
                    prestamista.deuda = 0 
                else : 
                    pago = str(round(rata.deuda, 2))
                    prestamista.deuda -= rata.deuda
                    rata.deuda = 0 
                
                if len(rata.nombre) >= 4:
                    print(f"El amigo {color_yellow} {rata.nombre} {color_reset} \tle debe pagar a {prestamista.nombre} {color_green} \t $  {pago} {color_reset}")
                else:
                    print(f"El amigo {color_yellow} {rata.nombre} {color_reset} \t\tle debe pagar a {prestamista.nombre} {color_green} \t $  {pago} {color_reset}")



clear()
listaAmigos = ingresoAmigos() 


mostrarLista()

costoPromedio = calculoCosto() 
debe, leDeben = calculoDeudas(costoPromedio) 

pagoDeDeudas(debe, leDeben)