class agenda:
    def __init__(self):
        self.contactos = []
    def display(self):
        if len(self.contactos) == 0:
            print('No hay contactos en la lista.')
        else:
            print('\n----------------------------')
            print('Lista de contactos.')
            print('----------------------------')
            for p in range(len(self.contactos)):
                print(self.contactos[p]['nombre'])
    def menu(self):
        print()
        menu = [
            ['Agenda personal.'],
            ['1. Añadir contacto.'],
            ['2. Lista de contactos.'],
            ['3. Buscar contacto.'],
            ['4. Editar contacto.'],
            ['5. Eliminar contacto.'],
            ['6. Cerrar agenda.']
        ]
        for x in range(len(menu)):
           print(menu[x][0])
    def add(self):
        print('\n----------------------------')
        print('Añadir un nuevo contacto.')
        print('----------------------------')
        nam = input('Ingresa el nombre: ')
        numerou = int(input('Ingresa el número de teléfono: '))
        correo = input('Ingresa el correo: ')
        self.contactos.append({'nombre':nam, 'numero':numerou, 'mail':correo})
    def search(self):
        verifi = True
        print('\n----------------------------')
        print('Buscar un contacto.')
        print('----------------------------')
        search_name = input('Escriba el nombre a buscar: ')
        for x in range(len(self.contactos)):
            if search_name in self.contactos[x]['nombre']:
                print('\nInformación del contacto:')
                print(f"Nombre: {self.contactos[x]['nombre']}")
                print(f"Número de teléfono: {self.contactos[x]['numero']}")
                print(f"Email: {self.contactos[x]['mail']}")
                verifi = False
        if verifi == True:
            print('No se ha encontrado el contacto.')
        return x
    def edit(self):
        agenda.display(self)
        editable = self.search()
        condition = False
        while condition == False:
            try:
                awb = int(input('¿Qué parámetro desea editar?\n1. Nombre.\n2. Número de teléfono.\n3. Correo.\n4. Volver.\n'))
                if awb == 1:
                    xnf = input('Introduzca el nuevo nombre: ')
                    self.contactos[editable]['nombre'] = xnf
                if awb == 2:
                    xnf = int(input('Introduzca el nuevo número: '))
                    self.contactos[editable]['numero'] = xnf
                if awb == 3:
                    xnf = input('Introduzca el nuevo correo: ')
                    self.contactos[editable]['mail'] = xnf
                if awb == 4:
                    condition = True
            except Exception as a:
                print('Ha ocurrido un error de tipo =>', type(a).__name__)
    def delete(self):
        agenda.display(self)
        estable = True
        tri = False
        while estable == True:
            if len(self.contactos) != 0:
                awb = input('\n¿Qué contacto desea eliminar?\nPara salir: 0\n')
                if awb == '0':
                    estable = False
                    break
                else:
                    for x in range(len(self.contactos)):
                        if awb in self.contactos[x]['nombre']:
                            self.contactos.pop(x)
                            agenda.display(self)
                            estable = False
                            tri = True
                            break
                    if tri == False:
                        print('Nombre inválido.')
agendon = agenda()
F = True
while F == True:
    agendon.menu()
    answer = int(input())
    if answer == 1:
        agendon.add()
    elif answer == 2:
        agendon.display()
    elif answer == 3:
        agendon.search()
    elif answer == 4:
        agendon.edit()
    elif answer == 5:
        agendon.delete()
    elif answer == 6:
        F == False
        break
    else:
        continue