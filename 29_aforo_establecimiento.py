personas = int(input("Ingrese el número de personas dentro del local: "))
capacidad = int(input("Ingrese la capacidad máxima: "))
if personas < capacidad:
    print("Ingreso permitido")
else:
    print("Aforo completo, espere afuera")
