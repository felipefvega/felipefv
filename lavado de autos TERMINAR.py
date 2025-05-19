#D.V
total = 0



while True:
    print("""
         BIENVENIDO A DUOC CAR WASH
          
         INGRESE LA ACCIÓN A REALIZAR:
          1) CURSAR PAGO DEL LAVADO
          2) VER VENTAS DIARIAS
          2) SALIR """)
    
    accion= input("R:")
    
    if accion == "1":
        print("""
             ELIJA EL NIVEL DE LAVADO:
              1) FULL ($15000)
              2) STANDARD ($10000)
              3) BASICO ($7000)""")
        lavado = input("R:  ")    
        match lavado:
            case "1":
                total = 15000
            case "2":
                total = 10000
            case "3":
                total = 7000

