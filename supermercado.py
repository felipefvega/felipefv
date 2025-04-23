subtotal = 0

print("¿Cuantos productos va a llevar?")
cant = int(input())

print('''
      Bienvenido a DuocMarket!
     1) Pan ($2000)
     2) Keta ($10000)
     3) Tusi ($7500)
    ''')

for i in range(cant):

 print("¿Qué producto desea llevar?")
 producto = input()

 if producto == "1":
    subtotal = subtotal + 2000
 elif producto == "2":
    subtotal = subtotal + 10000
 elif producto == "3":
    subtotal = subtotal + 7500


total = subtotal*1.19

print("Su total es de", total)





