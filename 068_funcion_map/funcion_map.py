class Empleado:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return "{} que trabaja como {} y que tiene un salario de $ {}".format(self.name, self.position, self.salary)


def calculoComision(empleado):
    #se suma un 3% adicional
    if empleado.salary < 3000:
        empleado.salary = empleado.salary * 1.03

    return empleado

lista_empleados = [
    Empleado("Ponsiano", "Dev", 1600),
    Empleado("Naun", "Dev", 1100),
    Empleado("Thomas", "Dev Back", 1800),
    Empleado("Mireya", "Geo", 1700),
]

#se calcula comision para los que tienen salario alto y bajo
lista_empleados_comision = map(calculoComision, lista_empleados)

for empleado in lista_empleados_comision:
    print(empleado)


lista_empleados_comision = [calculoComision(x) for x in lista_empleados]
for empleado in lista_empleados_comision:
    print(empleado)