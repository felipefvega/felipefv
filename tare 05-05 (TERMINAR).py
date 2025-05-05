import time
import msvcrt
import os

#VARIABLES

puntaje = 0
multiplicador = 0


#FUNCIONES

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# CODIGO OFICAL CERTIFICADO
print(""" 
      BIENVENIDO AL SERVICIO DIGITAL DE DUOC BANK INTERCONINENTAL!
      
      A CONTINUACIÓN, SE REALIZARÁ UNA EVALUCIÓN COMERCIAL PARA CALCULAR SU PUNTAJE DE CREDITO""")

time.sleep(2)
clear()

ingreso = input("""SELECCIONE SU RANGO DE INGRESO MENSUAL
                
                1) $500.000 A $1.000.000
                2) $1.000.00 A $1.500.000
                3) $1.500.000 O MÁS
                
                RESPUESTA:  """)

clear()

educacion = input("""
                  SELECCIONE SU NIVEL EDUCACIONAL
                  
                  1) BASICO
                  2) MEDIO
                  3) SUPERIOR)

                   RESPUESTA:  """)

nacionalidad = input("""
                     SELECCIONE SU NACIONALIDAD
                     
                     1) CHILENA
                     2) EXTRANJERA
                     
                     RESPUESTA:  """)

if ingreso == "1":
    puntaje += 300000
elif ingreso == "2":
    puntaje +=
elif puntaje == "3":
    ingreso += 



if educacion == "1":
    multiplicador = 
elif educacion == "2":
    multiplicador = 
elif educacion == "3":
    multiplicador = 


puntaje = ingreso*multiplicador

if nacionalidad == "1":
    puntaje += 300000
elif nacionalidad == "2":
    puntaje += 0

clear()

print("EVALUCION REALIZADA CON ÉXITO!"," SU PUNTAJE DE CRÉDITO ES DE: ",puntaje)


