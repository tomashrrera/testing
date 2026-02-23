from descuentos.calcular_descuentos import calcular_descuento

class TestCalculadoraDescuentos:

    # FASE 1: Casos base
    def test_descuento_simple (self):
        assert calcular_descuento(100, 10) == 90.0
    # FASE 2: Casos extremos
    def test_sin_descuento (self):
        assert calcular_descuento(100, 0) == 100.0

    def test_descuento_completo (self):
        assert calcular_descuento(100, 100) == 0.0

    # FASE 3: Validación de errores
    def test_porcentaje_negativo (self):
        assert calcular_descuento(100, -10) == "Error: porcentaje inválido"

    def test_porcentaje_mayor_a_100 (self):
        assert calcular_descuento(100, 150) == "Error: porcentaje inválido"

    def test_precio_negativo (self):
        assert calcular_descuento(-50,10) == "Error: precio inválido"

    # FASE 4: Otros
    def test_precio_cero (self):
        assert calcular_descuento(0, 50) == 0.0

    def test_valores_decimales (self):
        resultado = calcular_descuento(99.99, 15)
        assert abs(resultado - 84.99) < 0.01  # Tolerancia para flotantes