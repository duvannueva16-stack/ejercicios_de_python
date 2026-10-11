saldo = float(input("Ingrese el saldo actual: "))
retiro = float(input("Ingrese el valor a retirar: "))
if retiro > saldo:
    print("Error: Saldo insuficiente")
else:
    print("Retiro exitoso")
