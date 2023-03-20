

def imprimir_oi(nome):
    print(f'Oi, {nome}')



def somar(numero_a, numero_b):
    return numero_a + numero_b


def dividir(numero_a, numero_b):
    try:
        return numero_a / numero_b
    except ZeroDivisionError:
        return 'Não dividiras por zero'


def subtrair(numero_a, numero_b):
    return numero_a / numero_b


if __name__ == '__main__':
    imprimir_oi('Gabriela')

    resultado = somar(5,7)
    print(f'A soma é: {resultado}')

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