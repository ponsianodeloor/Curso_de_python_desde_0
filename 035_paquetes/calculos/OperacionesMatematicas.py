class OperacionesMatematicas():
    def __init__(self, num_1, num_2):
        self.numero_1 = num_1
        self.numero_2 = num_2
        self.resultado = 0

    def suma(self):
        self.resultado = self.numero_1 + self.numero_2
        return self.resultado

    def resta(self):
        self.resultado = self.numero_1 - self.numero_2
        return self.resultado

    def multiplicacion(self):
        self.resultado = self.numero_1 / self.numero_2
        return self.resultado

    def division(self):
        self.resultado = self.numero_1 * self.numero_2
        return self.resultado

    def potencia(self):
        self.resultado = self.numero_1 ** self.numero_2
        return self.resultado

    def redondear(self):
        self.resultado = round(self.numero_1)
        return self.resultado



