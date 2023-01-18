class Persona():
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def descripcion(self):
        print(
            "Nombre: ",
            self.nombre,
            "Edad:",
            self.edad,
            "Nacionalidad",
            self.nacionalidad
        )

class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, nacionalidad_empleado):
        super().__init__(nombre_empleado, edad_empleado, nacionalidad_empleado)
        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion()
        print("Salario",self.salario,
              "Antiguedad",self.antiguedad
              )

Antonio = Persona("Antonio", 55, "Ecuatoriana")
Antonio.descripcion()

#Antonio = Empleado(1500, 15)
Antonio.descripcion()

Manuel = Empleado(1500, 15, "Manuel", 40, "Colombiana")
Manuel.descripcion()

print(isinstance(Manuel, Empleado))
print(isinstance(Manuel, Persona))
print(isinstance(Antonio, Empleado))