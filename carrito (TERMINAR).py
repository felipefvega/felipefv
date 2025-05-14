#


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

              
    
def nombreUsuario():
     usuario = input("INGRESE SU NOMBRE:  ")

def comprar():


                clear()

                while True:
                    eleccion = input("""
                    ESTOS SON LOS ARTÍCULOS DISPONIBLES PARA COMPRAR: 
                    1) PAN BIMBO ($2000)
                    2) MALLA PALTAS 1KG ($3400)
                    3) CLORO GEL 1 LITRO ($1500)
                    4) SALIR
                            
                    RESPUESTA:  """)

                    match eleccion:

                        case "1":
                            subtotal += 2000
                        case "2":
                            subtotal += 3400
                        case "3":
                            subtotal += 1500
                        case "4":
                            break
                        case _:
                            print("INGRESE UNA OPCIÓN VÁLIDA")

def boleta():

    total = subtotal*1.19

    print("SU SUBTOTAL ES DE: ",subtotal)
    print("SU TOTAL ES DE: ", total)


while True:
           
    menu1_op = input(""" 
                BIENVENIDO A DUOCMARKET!
                
                ELIJA LA ACCION A REALIZAR:
                
                1) INGRESAR NOMBRE DE USUARIO
                2) COMPRAR
                3) GENERAR BOLETA
                            
                RESPUESTA: """)

    match menu1_op:
        case "1":
            nombreUsuario()

            seguir = input("""
                      ¿DESEA REALIZAR OTRA OPERACIÓN?
                      
                       1) SÍ
                       2) NO
                           
                           RESPUESTA:  """)
            
            if seguir == "2":
                 break
            else:
                 clear()
           

        case "2":
             comprar()
             seguir()

        case "3":
            boleta()
            seguir()

        case 4:
            break
                
        case _:
            print("INGRESE UNA OPCIÓN VÁLIDA")

