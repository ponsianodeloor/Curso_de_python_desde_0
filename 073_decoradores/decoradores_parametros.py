def fn_decorate(fn_parametro):
    def fn_interior(*args, **kwargs):

        # imprimir 2 mensajes en la funcion suma y resta
        print("Vamos a realizar un calculo")

        fn_parametro(*args, **kwargs)
        # Acciones adicionales que decoran
        print("Se ha terminado el calculo")

    return fn_interior

@fn_decorate
def suma(n1, n2, n3):
    print(n1 + n2 + n3)

def resta(n1, n2):
    print(n1 - n2)

@fn_decorate
def potencia(base, exponente):
    print(pow(base, exponente))

suma(7, 5, 8)
resta(12, 10)

#se usa con **kwargs
potencia(base=5, exponente=3)