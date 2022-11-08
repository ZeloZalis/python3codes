#1. Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos (es suficiente con mostrar true o false):
# Si los dos números son iguales
# Si los dos números son diferentes
# Si el primero es mayor que el segundo
# Si el segundo es mayor o igual que el primero

one = float(input('Introduce el primer número: '))
two = float(input('Introduce el segundo número: '))
print('¿Los números son iguales?')
print(one == two)
print('¿Los números son diferentes?')
print(one != two)
print('¿El primer número es mayor que el segundo?')
print(one > two)
print('¿El segundo número es mayor o igual al primero?')
print(two >= one)
print('------------------------------------')

#2. Utilizando operadores lógicos, determina si una cadena de texto introducida por el usuario tiene una longitud mayor o igual que
# 3 y a su vez es menor que 10 (es suficiene con mostrar True o False).
chain = str(input('Ingresa un texto: '))
print('¿El número de caracteres ingresados es mayor o igual que 3 y menor a 10?')
print(len(chain) >= 3 and len(chain) < 10)
print('------------------------------------')

#3 Realiza un programa que cumpla el siguiente algoritmo utilizando siempre que sea posible operadores en asignación:
# Guarda en una variable numero_magico el valor 12345679 (sin el 8)
# Lee por pantalla otro numero_usuario, especifica que sea entre 1 y 9
# Multiplica el numero_usuario por 9 en sí mismo
# Multiplica el numero_magico por el numero_usuario en sí mismo
# Finalmente muestra el valor final del numero_magico por pantalla
numero_magico = 12345679
numero_usuario = int(input('Ingresa un número entero del 1 al 9: '))
numero_usuario = numero_usuario*9
numero_magico = numero_magico*numero_usuario
print(numero_magico)