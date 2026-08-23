menu = (input('hola quieres entrar en la calculadora para calcular calculaciones (s/n): ')).lower()

if menu == 's':
     print("bienvenido")
     numero = float(input("Elige un numero w: "))
     numero_2 = float(input("Elige un numero para hacer la operacion: "))
     opciones = (input('que desea hacer, sumar , restar , dividir , multiplicar , salir: ' )).lower()
     while opciones != "salir":
      if opciones == "sumar":
        print(numero + numero_2)
      elif opciones == "restar":
        print(numero - numero_2)
      elif opciones == "multiplicar":
        print(numero * numero_2)
      elif numero_2 == 0 and opciones == "dividir":
          print("no se puede dividir entre 0 w")
      elif opciones == "dividir":
        print(numero / numero_2)
      else:
        print("elige una de las opciones anteriores")
      numero = float(input("Elige un numero w: "))
      numero_2 = float(input("Elige un numero para hacer la operacion: "))
      opciones = (input('que desea hacer, sumar , restar , dividir , multiplicar , salir: ' )).lower()
if opciones == "salir":
    print('chau')
else:
   print('adios')