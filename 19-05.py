sumaNotas = 0
cantNotas = int(input("Ingrese la cantidad de notas de este curso:  "))

for i in range(cantNotas):
    notas = int(input(f"Ingrese la nota N{i+1}:  "))
    sumaNotas += notas

promedio = sumaNotas / cantNotas
talleres = int(input("¿A cuantos talleres asistió? R:   "))
decimas = talleres * 0.3

if decimas > 1:
    print("USTED TIENE LA BENDICIÓN DEL PROFESOR!")
else:
    print("USTED NO TIENE LA BENDICIÓN DEL PROFESOR")


notaFinal = promedio + decimas

if notaFinal > 5.0:
    notaFinal = 5.0

print(f"Su nota final es de {notaFinal}")

if notaFinal > 4.0:
    print("APROBADO")
else:
    print("REPROBADO")
