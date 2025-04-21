print("Ingrese la cantidad de alumnos")
sumaNotas = 0
promedio = 0
alumnos = int(input())

for i in range(alumnos):
    print("Ingrese la cantidad de notas del alumno N",i+1,":")
    rep = int(input())
    for j in range(rep):
        print("Ingrese la nota N",j+1,":")
        nota = int(input())
        sumaNotas = sumaNotas + nota
    promedio = sumaNotas/rep
    print("El promedio del alumno ",i+1," es",promedio)
    if promedio >= 40:
        print("Usted aprobó")
    else:
        print("Usted quedó pegao")
    sumaNotas = 0
    promedio = 0
