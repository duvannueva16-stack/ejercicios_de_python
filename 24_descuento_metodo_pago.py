valor = float(input("Ingrese el valor del producto: "))
metodo = input("Ingrese el método de pago (Efectivo o Tarjeta): ")
if metodo == "Efectivo":
    total = valor * 0.90
    print("Total con 10% de descuento:", total)
else:
    print("Total sin descuento:", valor)
