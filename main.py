import os 
import sys 
  

def ingresoAmigos(): 
    """ 
     Ingresa los datos de los amigos y los almacena en una lista de diccionarios 
    """                     
    vacaTotal = 0 
    listaAmigos = [] 
  
    nombre = input("Ingrese el nombre del amigo (enter para terminar): ")       # Ingresa nombre y cuanto puso 
    while nombre != "": 
        amigo = {} 
        cuantoPuso = round(float(input(f"Ingrese cuanto puso {nombre}: ")), 2)
        amigo["Nombre"] = nombre 
        amigo["cuantoPuso"] = cuantoPuso 
        listaAmigos.append(amigo) 
        nombre = input("Ingrese el nombre del amigo (enter para terminar): ") 
    return listaAmigos 
  
def calculoCosto(listaAmigos): 
    """ 
    Calcula el costo promedio de la juntada y compara el costo total con la cantidad juntada por los amigos. 
    """ 
    clear() 
    vacaTotal = 0 

  
    for amigo in listaAmigos:                                               # Suma cuanto puso cada uno 
        vacaTotal += amigo["cuantoPuso"] 

    costoProm = vacaTotal / len(listaAmigos)                               # Calcula el costo de cada uno 
    return costoProm 
  
def calculoDeudas(amigos, costoProm): 
    """ 
    Calcula deudas y devuelve dos listas de diccionarios, una con los amigos que pusieron de menos (ratas) y una con los amigos que pusieron de más (prestamistas) 
    """ 
    debePlata = [] 
    leDebenPlata = [] 

    for amigo in amigos: 
        if amigo["cuantoPuso"] < costoProm: 
            amigo["cuantoDebe"] = round((costoProm - amigo["cuantoPuso"]), 2) 
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
            if rata["cuantoDebe"] != 0:
                    if rata["cuantoDebe"] >= prestamista["cuantoLeDeben"]: 
                        print(f"El amigo {rata['Nombre']} le debe pagar a {prestamista['Nombre']} ${prestamista['cuantoLeDeben']}") 
                        rata["cuantoDebe"] -= prestamista["cuantoLeDeben"] 
                        prestamista["cuantoLeDeben"] = 0 
                    else : 
                        print(f"El amigo {rata['Nombre']} le debe pagar a {prestamista['Nombre']} ${rata['cuantoDebe']}") 
                        prestamista["cuantoLeDeben"] -= rata["cuantoDebe"] 
                        rata["cuantoDebe"] = 0 

def clear(): 
    if sys.platform == "linux": 
        os.system("clear") 
    elif sys.platfrom == "nt": 
        clear() 

def mostrarLista(listaAmigos):
    """
    Muestra la lista de amigos y cuanto puso cada uno.
    """
    ver = True
    while ver:
        print("Lista de amigos: ")
        for amigo  in listaAmigos:
            print(f"El maquinola de {amigo['Nombre']} puso {amigo['cuantoPuso']}")

        opc = input("\nDesea modificar algún monto? (S/N): ").lower()
    
        if opc != "s":
            ver = False

        while opc == "s":
            clear()
            compa = input("Ingrese el amigo: ")
            for i in listaAmigos:
                if compa == i["Nombre"]:
                    nuevoMonto = float(input("Ingrese el nuevo monto: "))
                    i["cuantoPuso"] = nuevoMonto
                    opc = "n"
                    
                    v = input("Desea ver la lista de nuevo? (S/N): ")
                    if v != "s":
                        ver == False
            if opc == "s":
                print("Nombre incorrecto, intente de nuevo.")
        
        clear()

clear()
listaAmigos = ingresoAmigos() 

clear()
mostrarLista(listaAmigos)

costoPromedio = calculoCosto(listaAmigos) 
debe, leDeben = calculoDeudas(listaAmigos, costoPromedio) 

pagoDeDeudas(debe, leDeben)