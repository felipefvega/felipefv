subtotal = 0
    
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
