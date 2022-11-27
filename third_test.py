#1. Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:
#- Mostrar una suma de los dos números
#- Mostrar una resta de los dos números (el primero menos el segundo).
#- Mostrar una multiplicación de los dos números
# En caso de introducir una opción inválida, el programa informará de que no es correcta.
val1 = int(input('Introduce el primer número: '))
val2 = int(input('Introduce el segundo número: '))
do = True
while do == True:
    print('¿Qué desea realizar?\n1. Sumar los dos números.\n2. Restar los números.\n3. Multiplicar los números.')
    res = int(input(''))
    if res == 1:
        print(val1 + val2)
        break
    elif res == 2:
        print(val1 - val2)
        break
    elif res == 3:
        print(val1*val2)
        break
    elif res != 1 or res != 2 or res != 3:
        print('Opción inválida.')
#2. Realiza un programa que lea un número impar por teclado.
# Si el usuario no introduce un número impar, debe repetise el proceso hasta que lo introduzca correctamente.
do = True
while do == True:
    valor = int(input('Introduzca un número impar: '))
    if valor % 2 != 0:
        print(f'El número {valor} es impar.')
        break
    elif valor % 2 == 0:
        print('Número inválido.')
#3. Realiza un programa que sume todos los números enteros pares desde el 0 hasta el 100.
sumatoria = 0
for num in range(101):
    if num % 2 == 0:
        sumatoria = sumatoria + num
print(f'La suma total es {sumatoria}')
#4 Realiza un programa que pida al usuario cuantos números quiere introducir.
# Luego lee todos los números y realiza una media aritmética.
tam = int(input('¿Cuántos números desea ingresar?\n'))
pop = []
for i in range(tam):
    pop.append(int(input(f'Ingrese el número en la posición {i+1}: ')))
dx = sum(pop)
print(f'El promedio es ', dx/tam)
#5. Realiza un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso.
# Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:
s = 1
lst = [0, 5, 7, 10]
while s == 1:
    nm1 = int(input('Ingresa un número entero entre 0 y 9: '))
    if nm1 <= 9 and nm1 >= 0:
        if nm1 in lst:
            print('El número ingresado se encuentra en la lista.')
        else:
            print('El número ingresado no se encuentra en la lista.')
        break
    else:
        print('Número fuera de rango.')
#6. Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:
# Todos los números del 0 al 10 [0, 1, 2, ..., 10]
# Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
# Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
# Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
# Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
print(list(range(11)))
print(list(range(-10, 1)))
x = []
for i in range(0, 21):
    if i % 2 == 0:
        x.append(i)
print(x)
d = []
for e in range(-20, 1):
    if e % 2 != 0:
        d.append(e)
print(d)
w = []
for k in range(0, 51):
    if k % 5 == 0:
        w.append(k)
print(w)
#7. Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas,
# pero no debe repetirse ningún elemento en la nueva lista:
lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
lsd = []
for l in range(len(lista_2)):
    if lista_2[l] in lista_1:
        if lista_2[l] in lsd:
            continue
        else:
            lsd.append(lista_2[l])
print(lsd)
