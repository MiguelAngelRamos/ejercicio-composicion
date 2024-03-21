def input_con_opcion_de_salida(prompt):
    respuesta = input(prompt)
    # SAliR
    if respuesta.lower() == "salir":
        print("Operación cancelada.")
        return None
    return respuesta