#asignaturas optativas anio 2023

print("Seleccione una asignatura optativa")
asignatura_optativa = input("Escriba su asignatura optativa"
                            ", 1.- Base de datos"
                            ", 2.- Programacion web"
                            ", 3.- Diseno de software: ")

asignatura_optativa = asignatura_optativa.lower()

if asignatura_optativa in ("base de datos", "programacion web", "diseno de software"):
    print("Asignatura seleccionada", asignatura_optativa)
else:
    print("La asignatura escogida no esta contemplada")
