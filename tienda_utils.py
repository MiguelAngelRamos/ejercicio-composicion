def input_con_opcion_de_salida(prompt):
    respuesta = input(prompt)
    # Salir salir SAliR
    if respuesta.lower() == "salir":
        print("Operación cancelada.")
        return None
    return respuesta


def encontrar_por_id(lista, id):
    for element in lista:
        if element.id == id:
            return element
    return None