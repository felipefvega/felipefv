
import time
import msvcrt
import os

monto_agregado = 0
impuesto = 1.19

subtotal = 0
total = 0

#DEFINIENDO FUNCIONES

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def calcularAgregado():
    global monto_agregado
    if producto in ("1","2","3"):
        monto_agregado += 200

    elif producto in ("4","5","6"):
         monto_agregado += 400

    elif producto in ("7","8","9"):
        monto_agregado += 600
    
def calcTotalProductos():
    
    global subtotal

    if producto == "1":
        subtotal += 2000
    elif producto == "2":
        subtotal += 1500
    elif producto == "3":
        subtotal += 2690
    elif producto == "4":
        subtotal += 2790
    elif producto == "5":
        subtotal += 3300
    elif producto == "6":
        subtotal += 6000
    elif producto == "7":
        subtotal += 2990
    elif producto == "8":
        subtotal += 1990
    elif producto == "9":
        subtotal += 4980
    else: "Opción Inválida."

def calcularImpuesto():
    global total
    global impuesto
    if  total < 5000:
        impuesto += 0.3
    elif total > 5000 and producto < 10000:
        impuesto += 0.5
    elif total > 10000:
        impuesto += 0.8




    

catalogo = """TENEMOS LOS SIGUIENTES PRODUCTOS DISPONIBLES

                 
                 - CATEGORÍA 1:
                   1) Pan ($2000)
                   2) Jamón ($1500)
                   3) Mantequilla ($2690)
                 
                 - CATEGORÍA 2

                   4) Pilas ($2790)
                   5) Velas ($3300)
                   6) Linterna ($6000)
            
                  - CATEGORÍA 3

                   7) Shampoo ($2990)
                   8) Jabón ($1990)
                   9) Detergente ($4980)"""
                 

print("""
                 Bienvenido a DUOC MARKET!
                 Se le informa que los montos agregados por categoría se han actualizado:
                 Categoría 1: Agregado de $200 por producto
                 Categoría 2: Agregado de $400 por producto
                 Categoría 3: Agregado de $600 por producto

                 Además se informa que el valor del impuesto varía según el monto total de la boleta:
                 De $0 a $5000: +0.3% de IVA
                 De $5001 a $10000: +0.5% de IVA
                 Y $10000+ : +0.8% de IVA

                 PRESIONE CUALQUIER TECLA PARA CONTINUAR...""")

msvcrt.getch()

clear()

print(catalogo)
producto = input("INGRESE PRODUCTO A LLEVAR: ")

calcTotalProductos()
calcularAgregado()


clear()

while True: 
    
    respuesta = str(input("""
                  ¿DESEA LLEVAR OTRO PRODUCTO?
                          
                    1) SÍ 
                    2) NO

                  RESPUESTA: """))
    
    if respuesta == "2":

      clear()
      break

        
    elif  respuesta == "1":
        clear()
        print(catalogo)
        producto = input("INGRESE PRODUCTO A LLEVAR: ")
        calcTotalProductos()
        calcularAgregado()
        clear()

total = (monto_agregado + subtotal)
calcularImpuesto()
totalFinal = (total*impuesto)

print(" ")
print("Subtotal: $",total)
print(" ")
print("Tu total es de: $",totalFinal," (Impuestos incluidos)")
print("""
      GRACIAS POR COMPRAR EN DUOC MARKET!""")









