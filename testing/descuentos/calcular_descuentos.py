def calcular_descuento(precio: float, porcentaje: float) -> float:
    if precio < 0:
        return "Error: precio inválido"

    if porcentaje < 0 or porcentaje > 100:
        return "Error: porcentaje inválido"

    return precio * (1-porcentaje/100)
