import os

def clear():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux, macOS, y otros sistemas POSIX
        os.system('clear')


notas = []



while True: 
    print(""" 
        INGRESE LA ACCIÓN A REALIZAR
      1) INGRESAR NOTA
      2) BORRAR NOTA
      3) MOSTRAR NOTAS
      4) SACAR PROMEDIO, NOTA MAYOR Y NOTA MENOR
      5) LIMPIAR REGISTRO DE NOTAS
      6) SALIR""")
    
    elec = input("R:  ")

    match elec:
        case "1":
            clear()
            while True:
                try:
                    nota_input = float(input("INGRESE LA NOTA A ALMACENAR:  "))
                    notas.append(nota_input)
                    print("NOTA ALMACENADA CON ÉXITO!")
                    clear()
                    break
                except ValueError:
                    print("La nota debe estar en formato decimal. Intente nuevamente")
                
        case "2":
            clear()
            if not notas:
                print("NO EXISTEN NOTAS EN EL REGISTRO.")
            else:
                print("ESTAS SON LAS NOTAS ALMACENADAS: ")
                print(*notas, sep=", ")
                while True:
                    try:
                        rem = float(input("INGRESE LA NOTA A ELIMINAR: "))
                        notas.remove(rem)
                        print("NOTA ELIMINADA CON ÉXITO!")
                        clear()
                        break
                    except ValueError:
                        print("No se ha encontrada la nota a eliminar. Intente nuevamente")
        
        case "3":
            clear()
            if not notas:
                clear()
                print("NO EXISTEN NOTAS EN EL REGISTRO.")
            else:
                print("ESTAS SON LAS NOTAS DISPONIBLES: ")
                print(*notas, sep=", ")

        case "4":
            clear()
            if not notas:
                
                print("NO EXISTEN NOTAS EN EL REGISTRO PARA CALCULAR EL PROMEDIO")

            else:
                promedio = sum(notas)/len(notas)
                mayor = max(notas)
                menor = min(notas)
                print("EL PROMEDIO DE LAS NOTAS ES: ",promedio,"."," La nota mayor es ",mayor," y la nota menor es ",menor,".")

            

        case "5":
            if not notas:
                clear()
                print("NO EXISTEN NOTAS EN EL REGISTRO.")
            else:
                clear()
                valid = input("""
                              ¿ESTA SEGURO QUE QUIERE LIMPIAR EL REGISTRO DE NOTAS? 
                              1) SÍ 
                              2) NO

                              R:  """)

                if valid == "1":
                    notas.clear
                    print("REGISTRO ELIMINADO CON ÉXITO!")
                    clear()
                else:
                    clear()

        case "6":
            break

        case _:
            clear()
            print("INGRESE UNA OPCIÓN VÁLIDA")
