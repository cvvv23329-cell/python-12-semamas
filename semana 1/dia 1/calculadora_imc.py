altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kg: "))
imc = peso / (altura **2)
if imc < 18.5:
    print("come mas")
elif imc >= 18.5 and imc < 24.9:
    print("tas bien")
elif imc >= 25 and imc < 29.9:
    print("tas gordo")
elif imc >= 30 and imc < 34.9:
    print("tas obeso")
elif imc >= 35 and imc < 39.9:
    print("tas muy obeso")
elif imc >= 40:
    print("tas extremadamente obeso")
