import pickle

class Persona:
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

    def registro(self):
        return ("Se ha registrado una nueva persona:", self.nombre, " ", self.genero, " ", self.edad)

class ListaPersonas:
    personas = []

    def __init__(self):
        lista_de_personas = open("archivo", "ab+")
        lista_de_personas.seek(0)

        try:
            self.personas = pickle.load(lista_de_personas)
            print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
        except:
            print("El fichero esta vacio")
        finally:
            lista_de_personas.close()
            del lista_de_personas

    def agregarPersona(self, p):
        self.personas.append(p)

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

    def guardarPersonasEnArchivo(self):
        lista_de_personas = open("archivo", "wb")
        pickle.dump(self.personas, lista_de_personas)
        lista_de_personas.close()
        del (lista_de_personas)

    def mostrarPersonasEnArchivo(self):
        print("La informacion del fichero externo es la siguiente")
        for p in self.personas:
            print(p)

lista_personas = ListaPersonas()

#gracias al return str se puede obtener los valores de la clase

persona = Persona("Ponsiano", "Masculino", 33)
#print(persona)
lista_personas = ListaPersonas()
lista_personas.agregarPersona(persona)

persona = Persona("Mireya", "Femenino", 33)
lista_personas = ListaPersonas()
lista_personas.agregarPersona(persona)

lista_personas.mostrarPersonas()

lista_personas.guardarPersonasEnArchivo()
lista_personas.mostrarPersonasEnArchivo()