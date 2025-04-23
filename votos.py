sofia = 0
maykol = 0

votantes = int(input("Ingrese la cantidad de votantes:"))

for i in range(votantes):
    print("Votante N",i+1,", ¿por quién desea votar?")
    print("1) Sofía o 2) Maykol")
    voto = input()

    if voto == "1":
        sofia = sofia + 1
    elif voto == "2":
        maykol = maykol + 1
    
print("Resultados finales:")
print("Votos de Sofia: ",sofia)
print("Votos de Maykol: ",maykol)

if sofia > maykol:
    print("Sofía es la ganadora")
elif maykol > sofia:
    print("Maykol es el ganador")
elif sofia == maykol:
    print("Es un empate")

    #PARCHEADO