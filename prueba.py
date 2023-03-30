cedula_cliente = input("\nIntroduce tu numero de cedula\n ->")
while not cedula_cliente.isnumeric():
    cedula_cliente = input("\nIntroduce tu numero de cedula con solo caracteres numericos\n ->")

print (cedula_cliente)



