class Vehiculo():
    def __init__(self):
        self.__largo_chasis = 250
        self.__ancho_chasis = 120
        self.__ruedas = 4
        self.__en_marcha = False

    def arrancar(self, arrancar):
        self.__en_marcha = arrancar

        if self.__en_marcha:
            return "El vehiculo esta en marcha"
        else:
            return "El vehiculo esta parado"

    def estado(self):
        print("EL vehiculo tiene: ", self.__ruedas,
              " ruedas "
              "Un ancho de: ", self.__ancho_chasis,
              " y un largo de ", self.__largo_chasis
              )

miVehiculo = Vehiculo()
print(miVehiculo.arrancar(True))
print(miVehiculo.estado())

print(miVehiculo.arrancar(True))
miVehiculo.estado()

print("---------------Segunda Instancia")

miCarro = Vehiculo()
print(miCarro.arrancar(False))
miCarro.ruedas = 5
miCarro.estado()