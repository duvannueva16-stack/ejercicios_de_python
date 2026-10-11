pago = float(input("Ingrese el valor del pago: "))
cupo = float(input("Ingrese el cupo disponible: "))
if pago <= cupo:
    print("Transacción aprobada")
else:
    print("Transacción rechazada por cupo insuficiente")
