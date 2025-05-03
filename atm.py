billetes5000 = 30
billetes10000 = 30
billetes20000 = 30

user1_id = "0001"
user2_id = "0002"
user3_id = "0003"

user1_pass = "1256"
user2_pass = "1267"
user3_pass = "1289"

user1_balance = 37000
user2_balance = 165000
user3_balance = 78000

balance = 0
systemPass = "0"
intentos = 3

user = input(''' 
      DUOC ATM
      INGRESE SU NÚMERO DE USUARIO: ''')

if user == user1_id:
    systemPass = user1_pass
elif user == user2_id:
    systemPass = user2_pass
elif user == user3_id:
    systemPass = user3_pass

while intentos != 0:
    passInput = str(input("INGRESE SU CLAVE SECRETA: "))
    if passInput == systemPass:
        print("ACCESO PERMITIDO!")
        intentos = 0
    else:
        intentos -= 1
        print("CLAVE INCORRECTA. ", intentos, " intentos disponibles.")

if passInput != systemPass and intentos == 0:
    exit()

###################################  FUNCIONANDO HASTA AQUI  ###################################


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
     


#HAY QUE TERMINARLO

