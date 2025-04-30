user1_id = "0001"
user2_id = "0002"
user3_id = "0003"

user1_pass = 1256
user2_pass = 1267
user3_pass = 1289

user1_balance = 
user2_balance =
user3_balance =

balance = 0

user = input(''' 
      DUOC ATM
      INGRESE SU NÚMERO DE USUARIO: ''')

if user == user1_id:
    balance = user1_balance
elif user == user2_id:
    balance = user2_balance
elif user == user3_id:
    balance = user3_balance

print(""" 
      ¡BIENVENIDO!
      SELECCIONE LA ACCIÓN A REALIZAR 
      1) RETIRO DE DINERO
      2) CONSULTA DE SALDO """)

task = input("OPCIÓN: ")

if task == 1:
    monto = input("""
          Ingrese el monto a retirar (SOLO MULTIPLOS DE 5000 Y 10000)
          MONTO: """)
    
    if balance < monto:
        print("Saldo insuficiente para realizar la operación")
    if 




