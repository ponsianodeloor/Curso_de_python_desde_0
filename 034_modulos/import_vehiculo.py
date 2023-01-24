from Vehiculo import *

miMoto = Moto("Honda", "CBR-X")
#miMoto.maniobrarUnaLlanta()
miMoto.estado()
#miMoto.carga() este metodo no esta implementado en la clase heredada
print("--------------- Instancia 2")

miFurgoneta = Furgoneta("Renault", "Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

mi_bicileta_electrica = BicicletaElectrica("Tesla", "XK199")
mi_bicileta_electrica.estado()
print("Tamanio de los aros", mi_bicileta_electrica.tamanioAros())