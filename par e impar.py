num = int(input("Ingrese un número:"))

for i in range(num):
    if (i+1) % 2 == 0:
        print("El número ",i+1," es par!")
    else:
        print("El número ",i+1," es impar!")
