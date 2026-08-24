numeros = [10, 25, 3, 48, 7, 100, 32]

print(f"los numeros son {numeros}")
cantidad = 0
for i in numeros:
    cantidad += 1
print(f"hay {cantidad} numeros")

pares = 0
for i in numeros:
    if i % 2 == 0 :
        pares += 1
print(f"{pares} son numeros pares")

impares = 0
for i in numeros:
    if i % 2 != 0 :
        impares += 1
print(f"{impares} son numeros impares")

mayor = numeros[0]
for i in numeros:
    if i > mayor:
        mayor = i
print(f"el numero mayor es {mayor}")

menor = numeros[0]
for i in numeros:
    if i < menor :
        menor = i
print(f"el numero menor es {menor}")

suma = 0
for i in numeros:
    suma += i
print(f"la suma total de numeros es {suma}")

promedio = suma / cantidad
print(f"el promedio de los datos es {promedio}")
 
numeros_30 = []
for i in numeros:
    if i > 30:
        numeros_30.append(i)
print(numeros_30)
