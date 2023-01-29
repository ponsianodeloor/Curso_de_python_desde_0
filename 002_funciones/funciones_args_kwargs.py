#args son las habilidades
#kwargs raza, mascota y clase

def crearPersonaje(nombre, *args, **kwargs):
    descripcion = f"###### {nombre.upper()} ####\n\n "
    descripcion += "###### Descripcion del personaje ####\n\n"

    for clave, valor in kwargs.items():
        descripcion += f"{clave}-------->{valor}\n"

    descripcion += "###### Habilidades ###\n\n"

    for skill in args:
        descripcion += f" - {skill}\n"

    return descripcion


personaje = crearPersonaje("Dandelion", "Ataque Fuerte", "Bola de fuego", clase="Mago", raza="No-muerto", mascota="serpiente")
print(personaje)