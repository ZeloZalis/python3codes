#1. Realiza un programa que siga las siguientes instrucciones:
# Crea un conjunto llamado usuarios con los usuarios Marta, David, Elvira, Juan y Marcos.
# Crea un conjunto llamado administradores con los administradores Juan y Marta.
# Borra al administrador Juan del conjunto de administradores.
# Añade a Marcos como un nuevo administrador, pero no lo borres del conjunto de usuarios.
# Muestra todos los usuarios por pantalla de forma dinámica, además debes indicar cada usuario es administrador o no.
users = {'Marta', 'David', 'Elvira', 'Juan', 'Marcos'}
admin = {'Juan', 'Marta'}
for i in admin:
    if 'Juan' in admin:
        admin.discard('Juan')
        print('Juan ha sido eliminado como administrador.')
        break
for i in users:
    if 'Marcos' in users:
        admin.add('Marcos')
        print('Marcos ha sido añadido como administrador.')
        break
for i in users:
    if i in admin:
        print(f'{i}, administrador.')
    else:
        print(f'{i}, usuario.')
#2. Durante el desarrollo de un pequeño videojuego se te encarga configurar y balancear cada clase de personaje jugable.
# Partiendo que la estadística base es 2, debes cumplir las siguientes condiciones:
# El caballero tiene el doble de vida y defensa que un guerrero.
# El guerrero tiene el doble de ataque y alcance que un caballero.
# El arquero tiene la misma vida y ataque que un guerrero, pero la mitad de su defensa y el doble de su alcance.
# Muestra como quedan las propiedades de los tres personajes.
warrior = {'hp':'2', 'def':'2', 'atk':'4', 'range':'4'}
knight = {'hp':'4', 'def':'4', 'atk':'2', 'range':'2'}
archer = {'hp':'2', 'def':'1', 'atk':'4', 'range':'8'}
print('Warrior:')
for i in warrior:
    print(i,warrior[i])
print('--------------------------')
print('Knight:')
for i in knight:
    print(i,knight[i])
print('--------------------------')
print('Archer:')
for i in archer:
    print(i,archer[i])
#3 Durante la planificación de un proyecto se han acordado una lista de tareas.
# Para cada una de estas tareas se ha asignado un orden de prioridad (cuanto menor es el número de orden, más prioridad).
# ¿Eres capaz de crear una estructura del tipo cola con todas las tareas ordenadas pero sin los números de orden?
from collections import deque
cola = deque({'Limpieza':'3', 'Compra de equipo':'1', 'Aprender a usar el equipo':'1'})
print(cola)

#------------------- Falta Completar ----------------------------