class Empleado:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return "{} que trabaja como {} y que tiene un salario de $ ".format(self.name, self.position, self.salary)

lista_empleados = [
    Empleado("Ponsiano", "Dev", 1600),
    Empleado("Naun", "Dev", 1100),
    Empleado("Thomas", "Dev Back", 1800),
    Empleado("Mireya", "Geo", 1700),
]

salarios_altos = filter(lambda empleado: empleado.salario > 1500, lista_empleados)

for empleado_salario in salarios_altos:
    empleado_salario