#EXPLICACION Y USO DE WHILE

clave = 1234
intentos = 0

password = int(input("Ingrese su clave: "))

while clave != password or intentos < 3:

    print("Error. Clave incorrecta")
    password = int(input("Ingrese su clave: "))
   
print("Bienvenido")

####PARCHEALO Y TERMINALO