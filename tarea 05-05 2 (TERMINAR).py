ramos = int(input("INGRESE CANTIDAD DE RAMOS:  "))
promedio = 0

for i in range(ramos):
    print("INGRESE PROMEDIO DE RAMO N",i+1)
    promedio += int(input())

print(promedio)

if promedio > 4.5 and < 5.0