print("Ingrese su edad: ")
edad = int(input())

if edad <12:
    print("Eres menor un niño")
elif edad >= 12 and edad<18:
    print("Eres mayor un adolescente")
elif edad >= 18 and edad<65:
    print("Eres mayor un adulto")
elif edad > 65:
    print("Eres mayor un adulto mayor")