class vehicles():
    def __init__(self, color, wheels):
        self.color = color
        self.wheels = wheels
class car(vehicles):
    def __init__(self, color, wheels, speed, cylinders):
        super().__init__(color, wheels)
        self.speed = speed
        self.cylinders = cylinders
class bicycle(vehicles):
    def __init__(self, color, wheels, type):
        super().__init__(color, wheels)
        self.type = type
class van(vehicles):
    def __init__(self, color, wheels, load):
        super().__init__(color, wheels)
        self.load = load
class motorcycle(vehicles):
    def __init__(self, color, wheels, speed, cylinders):
        super().__init__(color, wheels)
        self.speed = speed
        self.cylinders = cylinders
def catalogar(list_vehicles):
    i = 0
    o = 0
    for vehicles in list_vehicles:
        if type(vehicles).__name__ == 'car':
            print(f"Clase: {type(vehicles).__name__}\nColor: {vehicles.color}\nCantidad de ruedas: {vehicles.wheels}\nVelocidad: {vehicles.speed}km/h\nCilindros: {vehicles.cylinders}\n")
            i+=1
        if type(vehicles).__name__ == 'bicycle':
            print(f"Clase: {type(vehicles).__name__}\nColor: {vehicles.color}\nCantidad de ruedas: {vehicles.wheels}\nTipo: {vehicles.type}\n")
            o+=1
        if type(vehicles).__name__ == 'van':
            print(f"Clase: {type(vehicles).__name__}\nColor: {vehicles.color}\nCantidad de ruedas: {vehicles.wheels}\nCarga: {vehicles.load}kg\n")
            i+=1
        if type(vehicles).__name__ == 'motorcycle':
            print(f"Clase: {type(vehicles).__name__}\nColor: {vehicles.color}\nCantidad de ruedas: {vehicles.wheels}\nVelocidad: {vehicles.speed}km/h\nCilindros: {vehicles.cylinders}\n")
            o+=1
    print(f'Se han encontrado {i} vehículos con cuatro ruedas, y {o} vehículos con dos ruedas.')
def catalogar_ruedas(ruedas, lista):
    i = 0
    o = 0
    for vehicles in lista:
        if vehicles.wheels == ruedas:
            if type(vehicles).__name__ == 'car':
                print(f"Clase: {type(vehicles).__name__}\nColor: {vehicles.color}\nCantidad de ruedas: {vehicles.wheels}\nVelocidad: {vehicles.speed}km/h\nCilindros: {vehicles.cylinders}\n")
                i+=1
            if type(vehicles).__name__ == 'bicycle':
                print(f"Clase: {type(vehicles).__name__}\nColor: {vehicles.color}\nCantidad de ruedas: {vehicles.wheels}\nTipo: {vehicles.type}\n")
                o+=1
            if type(vehicles).__name__ == 'van':
                print(f"Clase: {type(vehicles).__name__}\nColor: {vehicles.color}\nCantidad de ruedas: {vehicles.wheels}\nCarga: {vehicles.load}kg\n")
                i+=1
            if type(vehicles).__name__ == 'motorcycle':
                print(f"Clase: {type(vehicles).__name__}\nColor: {vehicles.color}\nCantidad de ruedas: {vehicles.wheels}\nVelocidad: {vehicles.speed}km/h\nCilindros: {vehicles.cylinders}\n")
                o+=1
    print(f'Se han encontrado {i} vehículos con cuatro ruedas, y {o} vehículos con dos ruedas.')
#Codigo principal
A1 = car('Rojo', 4, 70, 6)
A2 = bicycle('Rojo', 2, 'Sports')
A3 = van('Blanco', 4, 85)
A4 = motorcycle('Negro', 2, 98, 4)
list_vehicles = [A1, A2, A3, A4]
catalogar(list_vehicles)
catalogar_ruedas(4, list_vehicles)