from heap import HeapMax

def determinar_prioridad(nombre_general, planeta, descripcion):
    if (nombre_general == "Gran Inquisidor" or
        planeta == "Lothal" or
        "Hera Syndulla" in descripcion):
        return 3  
    elif (nombre_general == "Agente Kallus" or
          "Destructor Estelar" in descripcion or
          "AT-AT" in descripcion):
        return 2  
    else:
        return 1  


def agregar_pedido(cola_prioridad, nombre_general, planeta, descripcion):
    prioridad = determinar_prioridad(nombre_general, planeta, descripcion)
    cola_prioridad.arrive(f"{nombre_general}, {planeta}, {descripcion}", prioridad)


def atender_pedido(cola_prioridad, bitacora):
    pedido_atendido = cola_prioridad.atention()
    if pedido_atendido:
        print(f"Atendiendo pedido: {pedido_atendido[1]}")
        
        if pedido_atendido[0] == 3:
            bitacora.append(pedido_atendido[1])

cola_prioridad = HeapMax()
bitacora = []


pedidos = [
    ("Gran Inquisidor", "Lothal", "Infiltración rebelde detectada"),
    ("Agente Kallus", "Endor", "Necesitamos un Destructor Estelar para contrarrestar"),
    ("General Veers", "Hoth", "Solicito refuerzos para AT-AT"),
    ("General Organa", "Alderaan", "Movimiento rebelde reportado"),
    ("Gran Inquisidor", "Tatooine", "Hera Syndulla está involucrada"),
]

for nombre_general, planeta, descripcion in pedidos:
    agregar_pedido(cola_prioridad, nombre_general, planeta, descripcion)

while True:
    if not cola_prioridad.elements:
        break
    atender_pedido(cola_prioridad, bitacora)

print("\nPedidos en la bitácora para seguimiento:")
for pedido in bitacora:
    print(f"Pedido: {pedido}")