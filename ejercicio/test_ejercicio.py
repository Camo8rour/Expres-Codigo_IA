import pytest
from ejercicio import calcular_primos, dividir_numero

def test_calcular_primos_caso_basico():
    """Prueba el caso básico de los primeros números primos"""
    resultado = calcular_primos(5)
    assert resultado == [2, 3, 5, 7, 11]

def test_calcular_primos_cero():
    """Prueba el caso cuando se solicita 0 números primos"""
    resultado = calcular_primos(0)
    assert resultado == []

def test_calcular_primos_negativo():
    """Prueba el caso cuando se ingresa un número negativo"""
    resultado = calcular_primos(-1)
    assert resultado == []

def test_calcular_primos_un_numero():
    """Prueba el caso cuando se solicita solo un número primo"""
    resultado = calcular_primos(1)
    assert resultado == [2]

def test_calcular_primos_orden():
    """Prueba que los números primos estén en orden ascendente"""
    resultado = calcular_primos(10)
    assert resultado == sorted(resultado)

def test_calcular_primos_todos_primos():
    """Prueba que todos los números en el resultado son realmente primos"""
    resultado = calcular_primos(10)
    for num in resultado:
        # Verifica que el número sea primo
        assert all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))

def test_calcular_primos_cantidad_correcta():
    """Prueba que se devuelve la cantidad correcta de números primos"""
    n = 7
    resultado = calcular_primos(n)
    assert len(resultado) == n

def test_dividir_numero_caso_normal():
    """Prueba la división de números válidos"""
    assert dividir_numero(10, 2) == 5.0
    assert dividir_numero(5, 2) == 2.5

def test_dividir_numero_por_cero():
    """Prueba que se lance ZeroDivisionError al dividir por cero"""
    with pytest.raises(ZeroDivisionError) as exc_info:
        dividir_numero(10, 0)
    assert str(exc_info.value) == "No se puede dividir por cero"

def test_dividir_numero_tipo_invalido():
    """Prueba que se lance TypeError con argumentos no numéricos"""
    with pytest.raises(TypeError) as exc_info:
        dividir_numero("10", 2)
    assert str(exc_info.value) == "Ambos argumentos deben ser números"
    
    with pytest.raises(TypeError) as exc_info:
        dividir_numero(10, "2")
    assert str(exc_info.value) == "Ambos argumentos deben ser números" 