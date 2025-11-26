# En este archivo debes implementar la función

def reloj_arena(m: int, s: str) -> str:
    # TODO: validar altura mayor que 0 e imprimir "Error: La altura debe ser un entero positivo" y salir
    if m <= 0:
        print("Error: La altura debe ser un entero positivo")
        return ""
    # TODO: implementar la lógica para generar el reloj de arena en ASCII
    figura = []
    # Parte superior (incluye centro)
    for i in range(m, 0, -1):
        espacios = m - i
        linea = " " * espacios + s * (2 * i - 1)
        figura.append(linea)

    # Parte inferior (sin repetir la línea central)
    for i in range(2, m + 1):
        espacios = m - i
        linea = " " * espacios + s * (2 * i - 1)
        figura.append(linea)

    # Unir líneas en un solo string final
    return "\n".join(figura)
