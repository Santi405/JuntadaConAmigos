import os 
import sys 
from colored import fg, attr, colored

color_green = fg('green')
color_reset = attr('reset')
color_yellow = fg('yellow')

global listaAmigos

def ingresoAmigos(): 
    """ 
     Ingresa los datos de los amigos y los almacena en una lista de diccionarios 
    """                     
    listaAmigos = [] 
    nombre = input("Ingrese el nombre del amigo (enter para terminar): " + color_yellow)       # Ingresa nombre y cuanto puso 

    while nombre != "":  
        nombresExist = [amigoExist["Nombre"] for amigoExist in listaAmigos]

        if nombre in nombresExist:
            print("Ya pusiste ese, pelele.")
        else:
            cuantoPuso = float(input(color_reset + "Ingrese cuanto puso " + color_yellow + nombre + color_reset + ": " + color_green))
            amigo = {"Nombre": nombre , "cuantoPuso": cuantoPuso}
            listaAmigos.append(amigo) 

        nombre = input(color_reset + "Ingrese el nombre del amigo (enter para terminar): " + color_yellow) 

    return listaAmigos 

def mostrarLista():
    """
    Muestra la lista de amigos y cuanto puso cada uno.
    """
    clear()

    print(color_reset + "Lista de amigos: ")
    for amigo  in listaAmigos:
        print(f"El maquinola de " + color_yellow + amigo['Nombre'] + color_reset + "\t puso " + color_green + str(amigo['cuantoPuso']) + color_reset)

    opc = input("\nDesea modificar algún monto? (S/N): ").lower()

    if opc == "s":
        clear()
        modificarLista()

    clear()

def modificarLista():
    boolNombre = False
    while not boolNombre:
        compa = input("Ingrese el amigo: ")
        for i in listaAmigos:
            if compa == i["Nombre"]:
                nuevoMonto = float(input("Ingrese el nuevo monto: "))
                i["cuantoPuso"] = nuevoMonto
                boolNombre = True
                
                verLista = input("Desea ver la lista de nuevo? (S/N): ").lower()
                if verLista == "s":
                    mostrarLista()

        if not boolNombre:
            clear()
            print("Nombre incorrecto, intente de nuevo.")
            

def calculoCosto(): 
    """ 
    Calcula el costo promedio de la juntada y compara el costo total con la cantidad juntada por los amigos. 
    """ 
    clear() 
    vacaTotal = 0 

    for amigo in listaAmigos:                                               # Suma cuanto puso cada uno 
        vacaTotal += amigo["cuantoPuso"] 

    costoProm = vacaTotal / len(listaAmigos)                               # Calcula el costo de cada uno 
    return costoProm 
  
def calculoDeudas(costoProm): 
    """ 
    Calcula deudas y devuelve dos listas de diccionarios, una con los amigos que pusieron de menos (ratas) y una con los amigos que pusieron de más (prestamistas) 
    """ 
    debePlata = [] 
    leDebenPlata = [] 

    for amigo in listaAmigos: 
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
    """ 
    Indica quien le debe a quien y cuanto 
    """ 
    for rata in endeudados: 
        for prestamista in prestamistas: 
            if rata["cuantoDebe"] != 0 and prestamista["cuantoLeDeben"] != 0:
                if rata["cuantoDebe"] >= prestamista["cuantoLeDeben"]: 
                    pago = str(round(prestamista['cuantoLeDeben'], 2))
                    rata["cuantoDebe"] -= prestamista["cuantoLeDeben"] 
                    prestamista["cuantoLeDeben"] = 0 
                else : 
                    pago = str(round(rata['cuantoDebe'], 2))
                    prestamista["cuantoLeDeben"] -= rata["cuantoDebe"] 
                    rata["cuantoDebe"] = 0 
                
                if len(rata['Nombre']) >= 4:
                    print(f"El amigo {color_yellow} {rata['Nombre']} {color_reset} \tle debe pagar a {prestamista['Nombre']} {color_green} \t $  {pago} {color_reset}")
                else:
                    print(f"El amigo {color_yellow} {rata['Nombre']} {color_reset} \t\tle debe pagar a {prestamista['Nombre']} {color_green} \t $  {pago} {color_reset}")

def clear(): 
    if sys.platform == "linux": 
        os.system("clear") 
    elif sys.platform == "nt": 
        clear() 


clear()
listaAmigos = ingresoAmigos() 


mostrarLista()

costoPromedio = calculoCosto() 
debe, leDeben = calculoDeudas(costoPromedio) 

pagoDeDeudas(debe, leDeben)