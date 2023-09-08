class motorcycle():
    price = 7500
    def __init__(self, color, plate, brand, model, madedate, maxspeed, weight, gas, wheels, maxigas):
        self.color = color
        self.plate = plate
        self.gas_L = gas
        self.wheels = wheels
        self.brand = brand
        self.model = model
        self.made_date = madedate
        self.max_speed = maxspeed
        self.weight = weight
        self.maxigas = maxigas
    motor = False
    acompañante = False
    def poner_acompañante(self):
        self.acompañante = True
    def quitar_acompañante(self):
        self.acompañante = False
    def turn_engine_on(self):
        if self.motor==False:
            self.motor = True
            print("El vehículo se ha encendido.")
        else:
            print("El vehículo ya está encendido.")
    def turn_engine_off(self):
        if self.motor==True:
            self.motor = False
            print("El vehículo se ha apagado.")
        else:
            print("El vehículo ya está apagado.")
    def info(self):
        print(f'Color: {self.color}.\nMatrícula: {self.plate}.\nGasolina: {self.gas_L} litros.\nRuedas: {self.wheels}.\nMarca: {self.brand}.\nModelo: {self.model}.')
        print(f'Fecha de fabricación: {self.made_date}')
        print(f'Máxima velocidad: {self.max_speed}km/h')
        print(f'Peso: {self.weight}kg')
        print(f'Precio: {self.price}')
        print(f'On/Off: {self.motor}')
        if self.acompañante == True:
            print('La moto tiene acompañante.')
    def consultar_precio(self):
        print(f'El precio de la moto {self.brand} es de {self.price}$.')
    def gas_comprobation(self):
        gasmax = 50
        print(f'<Reporte del depósito de la {self.brand} {self.model}>')
        print('-----------------------------------------------')
        print(f'Cantidad de gasolina en el tanque: {self.gas_L} litros.')
        print(f'Cantidad máxima de carga: {self.maxigas} litros.')
        print(f'Combustible faltante: {self.maxigas-self.gas_L} litros.')
        print('-----------------------------------------------')
    def repostar(self):
        repos = True
        print(f'La moto {self.brand} tiene {self.gas_L} litros en el tanque.')
        while repos == True:
            cantidad = int(input(f'¿Cuántos litros quiere repostar para la {self.brand} {self.model}?\n'))
            if cantidad > (self.maxigas-self.gas_L):
                print(f'La cantidad ingresada supera el límite del tanque ({self.maxigas}).')
            elif cantidad != 0 and cantidad <= (self.maxigas-self.gas_L):
                self.gas_L = self.gas_L+cantidad
                print(f'Se ha repostado con éxito.\nCantidad de gas en el tanque: {self.gas_L} litros.')
                repos = False
            elif cantidad == 0:
                print('Debe ingresar una cantidad válida.')
class AmikoMoto(motorcycle):
    def __init__(self, color, plate, brand, model, madedate, maxspeed, weight, gas, wheels, maxigas):
        super().__init__(color, plate, brand, model, madedate, maxspeed, weight, gas, wheels, maxigas)
        self.acompañante = True
Moto1 = motorcycle(color='red', plate='AB5SDS3-2', brand='Chevrolet', model='Corvette', madedate='02/05/2021', maxspeed=180, weight=2500, gas = 10, wheels = 2, maxigas=17) #Clave
Moto2 = motorcycle('Blue', 'SFD57S-2', 'Mitsubishi', 'Skyline', '25/02/2020', 175, 5200, 0, 2, 20) #Posicional
Moto3 = AmikoMoto(color='White', plate='AS7W43-2', brand='WolsWagen o como se escriba XD', model='Bocho', madedate='02/05/2022', maxspeed=10, weight=2500, gas = 10, wheels = 2, maxigas=12)
Moto3.price = 6700