def fn_decorate(fn_parametro):
    def fn_interior():

        # imprimir 2 mensajes en la funcion suma y resta
        print("Vamos a realizar un calculo")

        fn_parametro()
        # Acciones adicionales que decoran
        print("Se ha terminado el calculo")

    return fn_interior

@fn_decorate
def suma():
    print(15 + 20)

def resta():
    print(30 - 10)

suma()
resta()