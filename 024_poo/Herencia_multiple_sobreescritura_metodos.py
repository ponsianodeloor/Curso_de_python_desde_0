class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.en_marcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.en_marcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print(
            "Marca: ", self.marca, "\n",
            "Modelo", self.modelo, "\n",
            "En marcha", self.en_marcha, "\n",
            "Acelera", self.acelera, "\n",
            "Frena", self.frena, "\n"
        )

class Furgoneta(Vehiculo):
    def carga(self, cargar):
        self.cargado = cargar
        if self.cargado == True:
            return "la furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"

class Moto(Vehiculo):
    maniobrar_en_una_llanta = ""

    def maniobrarUnaLlanta(self):
        self.maniobrar_en_una_llanta = "Voy haciendo caballito"

    def estado(self):
        print(
            "Marca: ", self.marca, "\n",
            "Modelo", self.modelo, "\n",
            "En marcha", self.en_marcha, "\n",
            "Acelera", self.acelera, "\n",
            "Frena", self.frena, "\n",
            "Maniobra una llanta", self.maniobrar_en_una_llanta
        )

class VehiculoElectrico():
    def __init__(self):
        self.autonomia_km = 100

    def cargarEnergia(self):
        self.cargando = True

miMoto = Moto("Honda", "CBR-X")
#miMoto.maniobrarUnaLlanta()
miMoto.estado()
#miMoto.carga() este metodo no esta implementado en la clase heredada
print("--------------- Instancia 2")

miFurgoneta = Furgoneta("Renault", "Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

#herencia multiple considera al contructor de la primera clase indicada
class BicicletaElectrica(Vehiculo, VehiculoElectrico):
    diametro_aros = 0
    def tamanioAros(self):
        self.diametro_aros = 20
        return self.diametro_aros


mi_bicileta_electrica = BicicletaElectrica("Tesla", "XK199")
mi_bicileta_electrica.estado()
print("Tamanio de los aros", mi_bicileta_electrica.tamanioAros())