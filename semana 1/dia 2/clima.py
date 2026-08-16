temperatura = float(input('ingrese su temperatura en grados celsius: '))
if temperatura < 0:
    print("hace frio w")
elif temperatura >= 0 and temperatura <= 14:
    print("estra fresquito")
elif temperatura >= 15 and temperatura <= 24:
    print("esta templado")
elif temperatura >= 25 and temperatura <= 34:
    print("esta caluroso")
else:
    print("hace mucho calor")
