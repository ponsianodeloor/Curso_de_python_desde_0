salario_presidente = int(input("Ingrese el salario del presidente: "))
#print("Salario presidente:", salario_presidente)
print("Salario presidente: " +  str(salario_presidente))

salario_director = int(input("Ingrese el salario del director: "))
print("Salario director:", salario_director)

salario_jefe_de_area = int(input("Ingrese el salario del jefe_de_area: "))
print("Salario jefe_de_area:", salario_jefe_de_area)

salario_administrativo = int(input("Ingrese el salario del administrativo: "))
print("Salario administrativo:", salario_administrativo)

if salario_administrativo < salario_jefe_de_area < salario_director < salario_presidente:
    print("Todo funciona correctamente")
else:
    print("Algo esta fallando en esta empresa")
