class Auto():
    def desplazamiento(self):
        print("Se desplaza usando 4 ruedas")

class Moto():
    def desplazamiento(self):
        print("Se desplaza usando 2 ruedas")

class Camion():
    def desplazamiento(self):
        print("Se dezplaza usando 6 ruedas")

miVehiculo = Moto()
miVehiculo.desplazamiento()

miVehiculo2 = Auto()
miVehiculo2.desplazamiento()

miVehiculo3 = Camion()
miVehiculo3.desplazamiento()

def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo = Auto()
desplazamientoVehiculo(miVehiculo)