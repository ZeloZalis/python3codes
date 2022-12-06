#1. Formatea los siguientes valores para mostrar el resultado indicado:
# "Hola Mundo" → Alineado a la derecha en 20 caracteres
# "Hola Mundo" → Truncamiento en el cuarto carácter (índice 3)
# "Hola Mundo" → Alineamiento al centro en 20 caracteres con truncamiento en el segundo carácter (índice 1)
# 150 → Formateo a 5 números enteros rellenados con ceros
# 7887 → Formateo a 7 números enteros rellenados con espacios
# 20.02 → Formateo a 3 números enteros y 3 números decimales
text = 'Hola Mundo'
print(f'{text:>20}')
print(f'{text:.4}')
print(f'{text:^20.2}')
num1 = 150
print(f'{num1:05d}')
num2 = 7887
print(f'{num2:7d}')
num3 = 20.02
print(f'{num3:3.3f}')
#Los demás ejercicios son scripts aparte.