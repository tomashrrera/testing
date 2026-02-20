def calcular_descuento(precio: float, porcentaje: float) -> float:
    """
    Calculamos el precio final tras recibir un descuento.

    Args:
        precio: Precio original (float o int)
        porcentaje: Porcentaje de descuento (0-100)

    Returns:
        float: Precio con descuento aplicado
        str: Mensaje de error si el porcentaje es inválido
    """
    if porcentaje < 0 or porcentaje > 100:
        return "Error: porcentaje inválido"
    return precio * (1 - porcentaje/100)
