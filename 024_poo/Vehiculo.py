class Vehiculo():
    largo_chasis = 250
    ancho_chasis = 120
    ruedas = 4
    en_marcha = False

    def arrancar(self):
        self.en_marcha = True
        return self.en_marcha

    def estado(self):
        if self.en_marcha == True:
            return "El vehiculo esta en marcha"
        else:
            return "El vehiculo esta parado"


miVehiculo = Vehiculo()

print("el largo del vehiculo es: ", miVehiculo.largo_chasis)
print("el ancho del vehiculo es: ", miVehiculo.ancho_chasis)
print("La cantidad de ruedas del vehiculo es: ", miVehiculo.ruedas)

print(miVehiculo.estado())

print(miVehiculo.arrancar())
print("El estado del vehiculo", miVehiculo.en_marcha)
print(miVehiculo.estado())