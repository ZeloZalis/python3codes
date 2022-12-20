#1. Realiza una función llamada area_rectangulo(base, altura) que devuelva el área del rectangulo a
# partir de una base y una altura. Calcula el área de un rectángulo de 15 de base y 10 de altura.
def area_rectangulo(base, altura):
    area = base*altura
    return area
print(f'El área es de {area_rectangulo(15, 10)}cm.')
#2. Realiza una función llamada area_circulo(radio) que devuelva el área de un círculo a partir de un radio.
# Calcula el área de un círculo de 5 de radio:
rd = float(input('Ingrese el radio: '))
def area_circulo(radio):
    import math
    area = math.pi*radio**2
    return area
print(f'El área del circulo es {area_circulo(rd):0.3f}cm')
#3. Realiza una función llamada relacion(a, b) que a partir de dos números cumpla lo siguiente:
# Si el primer número es mayor que el segundo, debe devolver 1.
# Si el primer número es menor que el segundo, debe devolver -1.
# Si ambos números son iguales, debe devolver un 0.
# Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'.
def relacion(a, b):
    if a > b:
        num = 1
    if a < b:
        num = -1
    if a == b:
        num = 0
    return num
a = 5
b = 10
print(f'5 y 10 = {relacion(a, b)}')
print(f'10 y 5 = {relacion(b, a)}')
print(f'5 y 5 = {relacion(a, a)}')
#4. Realiza una función llamada intermedio(a, b) que a partir de dos números, devuelva su punto intermedio.
# Cuando lo tengas comprueba el punto intermedio entre -12 y 24:
def intermedio(a, b):
    num = (a+b)/2
    return num
a = -12
b = 24
print(intermedio(a, b))
#5. Realiza una función llamada recortar(numero, minimo, maximo) que reciba tres parámetros. El primero es el número a recortar,
# el segundo es el límite inferior y el tercero el límite superior.
# La función tendrá que cumplir lo siguiente:
# Devolver el límite inferior si el número es menor que éste
# Devolver el límite superior si el número es mayor que éste.
# Devolver el número sin cambios si no se supera ningún límite.
# Comprueba el resultado de recortar 15 entre los límites 0 y 10.
def recortar(num, min, max):
    if num < min:
        return min
    if num > max:
        return max
    else:
        return num
min = 0
max = 10
num = 15
print(recortar(num, min, max))
#6. Realiza una función separar(lista) que tome una lista de números enteros y devuelva dos listas ordenadas.
# La primera con los números pares y la segunda con los números impares.
def separar(lista):
    par = []
    impar = []
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            par.append(lista[i])
        else:
            impar.append(lista[i])
    par.sort()
    impar.sort()
    print(f'Números pares: {par}')
    print(f'Números impares: {impar}')
lista = [5, 8, 7, 6, 9, 4, 2, 10, 58]
separar(lista)