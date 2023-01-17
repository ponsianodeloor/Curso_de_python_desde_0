class Vehiculo():
    def __init__(self):
        self.__largo_chasis = 250
        self.__ancho_chasis = 120
        self.__ruedas = 4
        self.__en_marcha = False
        self.__gasolina = "ok"
        self.__aceite = "ok"
        self.__puertas = "cerradas"

    def arrancar(self, arrancar):
        self.__en_marcha = arrancar

        if self.__en_marcha:
            chequeo_interno = self.__chequeoInterno()

        if self.__en_marcha and chequeo_interno:
            return "El vehiculo esta en marcha"
        elif self.__en_marcha and chequeo_interno == False:
            return "Algo ha ido mal en el chequeo no podemos arrancar"

        else:
            return "El vehiculo esta parado"

    def estado(self):
        print("EL vehiculo tiene: ", self.__ruedas,
              " ruedas "
              "Un ancho de: ", self.__ancho_chasis,
              " y un largo de ", self.__largo_chasis
              )

    def __chequeoInterno(self):
        print("Realizando chequeo interno")
        if self.__gasolina == "ok" and self.__aceite == "ok" and self.__puertas == "cerradas":
            return True
        else:
            return False

miVehiculo = Vehiculo()
print(miVehiculo.arrancar(True))
print(miVehiculo.estado())

print(miVehiculo.arrancar(True))
miVehiculo.estado()
#miVehiculo.chequeoInterno()
print("---------------Segunda Instancia")

miCarro = Vehiculo()
print(miCarro.arrancar(False))
miCarro.ruedas = 5
miCarro.estado()
#miCarro.chequeoInterno()