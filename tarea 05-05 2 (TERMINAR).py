
# 51 a 60: 500
# 61 a 70: 800
# tecnico mas 60
# ingeniera mas 40
# diploado mas 20

ramos = int(input("INGRESE CANTIDAD DE RAMOS:  "))
puntaje = 0
promedio = 0.0

for i in range(ramos):
    print("INGRESE PROMEDIO DE RAMO N°", i+1)
    promedio += float(input())

print("Promedio total:", promedio)

if promedio >= 4.5 and promedio <= 5.0:
    puntaje += 300

elif promedio >= 5.1 and promedio <= 6.0:
    puntaje += 800

elif promedio >= 6.1 and promedio <= 7.0:
    puntaje += 800

print(puntaje)

print(""" 
      SELECCIONE SU TIPO DE CARRERA:
      1) TECNICO
      2) INGENIERIA
      3) DIPLOMADO""")

carrera = input("RESPUESTA: ")

if carrera == "1":
    puntaje += 60
elif carrera == "2":
    puntaje += 40
elif carrera == "3":
    puntaje += 20

print("SU PUNTAJE DE BENEFICIOS ES DE:", puntaje)
