def evaluate(note):
    valoracion = "Aprobado"
    if note < 5:
        valoracion = "Suspenso"

    return valoracion


print("Programa de evaluacion de notas de alumnos")
nota_alumno = input("Introduce la nota del alumno: ")

print(evaluate(int(nota_alumno)))