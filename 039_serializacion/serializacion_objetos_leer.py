import pickle

#todo va en un nuevo fichero se debe copiar la clase para que cargue en el nuevo archivo
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




archivo = open("los_vehiculos", "rb")
mis_vehiculos = pickle.load(archivo)

archivo.close()

for c in mis_vehiculos:
    print(c.estado())


