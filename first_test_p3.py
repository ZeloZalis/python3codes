#1 Identifica el tipo de dato (int, float, string o list) de los siguientes valores literales:
'hola mundo' #string
[1, 10, 100] #list
-25 #int
1.167 #float
['hola', 'mundo'] #list

#2 Determina mentalmente (sin programar) el resultado que aparecerá por pantalla en las siguientes operaciones con variables.

#a = 10
#b = -5
#c = 'Hola '
#d = [1, 2, 3]

#print(a * 5) = 15
#print(a - b) = 15
#print(c + "Mundo") = 'Hola Mundo'
#print(c * 2) = Error
#print(d[-1]) = [3]
#print(d[1:]) = [2, 3]
#print(d + d) = [1, 2, 3] [1, 2, 3]

#3 El siguiente código pretende realizar una media entre 3 números, pero no funciona correctamente. ¿Eres capaz de identificar el problema y solucionarlo?
numero_1 = 9
numero_2 = 3
numero_3 = 6
media = (numero_1 + numero_2 + numero_3)/3
print('La nota media es', media)
print('-----------------------------------')
#4 A partir del ejercicio anterior, vamos a suponer que cada número es una nota, y lo que queremos es obtener la nota final. El problema es que cada nota tiene un valor porcentual:
#- La primera nota vale 15% del total.
#- La segunda nota vale un 35% del total.
#- La tercera nota vale un 50% del total.
#Desarrolla un programa para calcular perfectamente la nota final:

nota_1 = 10
nota_2 = 7
nota_3 = 4

n1 = (10*15)/100
n2 = (7*35)/100
n3 = (4*50)/100
nt = n1 + n2 + n3
print(f'La nota total es {nt}.')
print('-----------------------------------')
#5 La siguiente matriz (o lista con listas anidadas) debe cumplir una condición, y es que en cada fila el cuarto elemento siempre debe ser el resultado de sumar los tres primeros. ¿Eres capaz de modificar las sumas incorrectas utilizando la técnica del slicing?
matriz = [
    [1, 1, 1, 3],
    [2, 2, 2, 7],
    [3, 3, 3, 9],
    [4, 4, 4, 13]
]
matriz[1][-1] = 6
matriz[3][-1] = 12
print(matriz)
print('-----------------------------------')
#6 Al realizar una consulta en un registro hemos obtenido una cadena de texto corrupta al revés. Al parecer contiene el nombre de un alumno y la nota de un exámen. ¿Cómo podríamos formatear la cadena y conseguir una estructura como la siguiente?
#{Nombre Apellido} ha sacado un {Nota} de nota.
cadena = "zeréP nauJ,01"
cadena = cadena[::-1]
print(f'{cadena[3:]} ha sacado un {cadena[0:2]} de nota.')
print('-----------------------------------')