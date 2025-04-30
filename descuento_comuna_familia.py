arancel = 200000
descuento = 0

comuna = int(input("""
      Seleccione su comuna 
      1) La Florida
      2) La Pintana
      3) Puente Alto
      4) San Joaquin
     Respuesta: """))

if comuna == 1:
    descuento += 20
elif comuna == 2:
    descuento += 30
elif comuna == 3:
    descuento += 25
elif comuna == 4:
    descuento += 15
else:
    print("Ingrese una opción válida")


grupo = int(input("""
     Seleccione su grupo familiar
     1) 1
     2) 2 a 4 personas
     3) 5 o más personas
     Respuesta: """))

if grupo == 1:
    descuento += 2
elif grupo == 2:
    descuento += 3
elif grupo == 3:
    descuento += 4
else:
    print("Ingrese una opción válida")


monto_descuento = (descuento/100)*arancel
total_final = (arancel - monto_descuento)

print("El total del descuento es de ",descuento,"%")
print("El total a pagar es de $",total_final)

