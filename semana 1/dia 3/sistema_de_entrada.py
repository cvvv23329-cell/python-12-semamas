edad = int(input("Ingrese su edad: "))
membresia_gimnasio_67 = input("¿Tiene membresía en el gimnasio? (s/n): ")
if edad >= 16 and membresia_gimnasio_67 == 's':
    print("Puede ingresar al gimnasio.")
else:
    print("No puede ingresar al gimnasio.")