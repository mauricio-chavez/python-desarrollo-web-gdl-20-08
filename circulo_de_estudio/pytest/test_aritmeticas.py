from aritmeticas import suma, resta, promedio


def test_suma():
    resultado = suma(5, 5)
    assert resultado == 9


def test_resta():
    resultado = resta(5, 4)
    assert resultado == 1


def test_promedio():
    resultado = promedio(5, 5)
    assert resultado == 5
