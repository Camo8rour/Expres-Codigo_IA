import math

def calcular_primos(n):
    if n <= 0:
        return []
    
    # Inicializamos la criba con todos los números marcados como posibles primos
    criba = [True] * (n * 20)  # Usamos un tamaño suficiente para encontrar n primos
    criba[0] = criba[1] = False
    
    # Aplicamos la Criba de Eratóstenes
    for i in range(2, int(len(criba) ** 0.5) + 1):
        if criba[i]:
            # Marcamos todos los múltiplos de i como no primos
            for j in range(i * i, len(criba), i):
                criba[j] = False
    
    # Recolectamos los primeros n números primos
    primos = []
    for i in range(len(criba)):
        if criba[i]:
            primos.append(i)
            if len(primos) == n:
                break
    
    return primos

def dividir_numero(a, b):
    """
    Divide dos números.
    
    Args:
        a: Numerador
        b: Denominador
        
    Returns:
        float: Resultado de la división
        
    Raises:
        ZeroDivisionError: Si el denominador es cero
        TypeError: Si los argumentos no son números
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Ambos argumentos deben ser números")
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b


if __name__ == "__main__":
    try:
        a = 10
        b = 0
        resultado = dividir_numero(a, b)
        print(f"El resultado de la division de {a} entre {b} es: {resultado}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

    print("Hola Mundo")