import pytest

from main import somar, dividir


def teste_somar():
    # 1 - Configura
    numero_a = 8
    numero_b = 7
    resultado_esperado = 15

    # 2 - Executa
    resultado_obtido = somar(numero_a, numero_b)

    # 3 - Valida
    assert resultado_obtido == resultado_esperado


def test_dividir_positivo():
    # configura
    numero_a = 6
    numero_b = 2
    resultado_esperado = 3

    # executa
    resultado_obtido = dividir(numero_a, numero_b)

    # Valida
    assert resultado_obtido == resultado_esperado


def test_dividir_negativo():
    # configura
    numero_a = 6
    numero_b = 0
    resultado_esperado = 'Não dividiras por zero'

    # executa
    resultado_obtido = dividir(numero_a, numero_b)

    # Valida
    assert resultado_obtido == resultado_esperado


lista_de_valores = [
    (8, 7, 15),
    (20, 30, 50),
    (25, 0, 25),
    (-5, 12, 7)
]


@pytest.mark.parametrize('numero_a, numero_b, resultando_esperado,', lista_de_valores)
def teste_somar_leitura_de_lista(numero_a, numero_b, resultado_esperado):
    # 1 - Configura

    # 2 - Executa
    resultado_obtido = somar(numero_a, numero_b)

    # 3 - Valida
    assert resultado_obtido == resultado_esperado
