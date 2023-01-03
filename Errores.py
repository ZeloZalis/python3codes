#1. Localiza el error en el siguiente bloque de código.
# Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:
try:
    resultado = 10/0
    print(resultado)
except ZeroDivisionError:
    print(f'No se puede dividir el número entre 0, intente otro número.')
#2. Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que
# el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:
try:
    lista = [1, 2, 3, 4, 5]
    print(lista[10])
except IndexError:
    print('Ha ocurrido un error => Posición en la lista no encontrada, pruebe con otro valor.')
#3. Localiza el error en el siguiente bloque de código.
# Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:
try:
    colores = { 'rojo':'red', 'verde':'green', 'negro':'black' } 
    print(colores['Blanco'])
except KeyError:
    print('Se ha producido un error, debe ingresar un valor que esté en el diccionario.')
#4. Localiza el error en el siguiente bloque de código.
# Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:
try:
    resultado = 15 + "20"
    print(resultado)
except TypeError:
    print('No puedes sumar un entero con una cadena.')
#5. Realiza una función llamada agregar_una_vez(lista, el) que reciba una lista y un elemento.
# La función debe añadir el elemento al final de la lista con la condición de no repetir ningún elemento.
# Además si este elemento ya se encuentra en la lista se debe invocar un error de tipo ValueError que debes capturar y mostrar
# este mensaje en su lugar:
# Error: Imposible añadir elementos duplicados => [elemento].
def agregar_una_vez(lista, el):
    if el in list:
        print(f'Error: Imposible añadir elementos duplicados => {el}.')
    else:
        lista.append(el)
list = [1, 5, -2]
valor1 = int(input('Ingresa un número: '))
agregar_una_vez(list, valor1)
valor2 = int(input('Ingresa un número: '))
agregar_una_vez(list, valor2)
valor3 = input('Ingresa una cadena: ')
agregar_una_vez(list, valor3)
print(list)