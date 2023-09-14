from io import open
from pathlib import Path
if not Path('contador.txt').exists():
    with open('contador.txt', 'w+', encoding='utf8') as file:
        file.write('0')
with open('contador.txt', 'r', encoding='utf8') as file:
    num = file.read()
print(f'Número en el fichero: {num}')
bucle = True
while bucle == True:
    arg = input('¿Qué desea realizar con el fichero?\ninc: Incrementar el número.\ndec: Disminuir el número.\n')
    if arg == 'inc' or arg == 'INC':
        with open('contador.txt', 'r', encoding='utf8') as file:
            file_list = file.readline()
            file_list = str(int(file_list[0])+1)
            print(f'El nuevo valor es: {file_list[0]}')
        with open('contador.txt', 'w', encoding='utf8') as file:
            file.write(file_list)
        bucle = False
    elif arg == 'dec' or arg == 'DEC':
        with open('contador.txt', 'r', encoding='utf8') as file:
            file_list = file.readline()
            file_list = str(int(file_list[0])-1)
            print(f'El nuevo valor es: {file_list[0]}')
        with open('contador.txt', 'w', encoding='utf8') as file:
            file.write(file_list)
        bucle = False
    else:
        print(f'El valor continua siendo {num}')
        bucle = False