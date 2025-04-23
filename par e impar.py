num = int(input("Ingrese un número:"))
pares = 0
impares = 0

for i in range(num):
    if (i+1) % 2 == 0:
        print("El número ",i+1," es par!")
        pares = pares + 1
        
    else:
        print("El número ",i+1," es impar!")
        impares = impares + 1


print("La cantidad de impares es de ",impares)
print("La cantidad de pares es de ",pares)
