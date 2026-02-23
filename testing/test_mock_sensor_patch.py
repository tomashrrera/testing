import requests
from unittest import mock


# 1. LA FUNCIÓN REAL (El protagonista)
def devolver_bitstream(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


# 2. EL TEST CON EL AGENTE INFILTRADO (@mock.patch)
@mock.patch('requests.get')
def test_consulta_sensor(mock_get):
    # El guion que queremos que devuelva el doble
    json_esperado = {'status': 'active', 'pulsations': '1001100'}

    # Configuramos el comportamiento del doble de acción
    respuesta_mock = mock_get.return_value
    respuesta_mock.status_code = 200
    respuesta_mock.json.return_value = json_esperado

    # ¡Acción! Llamamos a nuestra función real.
    # El agente infiltrado interceptará el requests.get internamente.
    resultado = devolver_bitstream('http://myservice.org.es')

    # El juez comprueba si todo ha salido según el guion
    assert resultado == json_esperado