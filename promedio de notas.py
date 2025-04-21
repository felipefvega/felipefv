#PEDIR NUMERO DE NOTA A USUARIO Y SACAR PROMEDIO
print ("Ingrese la cantidad de notas: ")
rep = int(input())
sumaNotas=0
for i in range(rep):
    print("Ingrese la nota N",i+1,":")
    nota = int(input())
    sumaNotas = int(sumaNotas+nota)

promedio = (sumaNotas/3)

print("Su promedio es de ",promedio,"! ")
