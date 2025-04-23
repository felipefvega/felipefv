pa = input("Ingrese una palabra:")
vocales = 0 

for i in pa:
    #print (i)
    if i.lower() in "aeiou":
        vocales = vocales + 1
    

print("La cantidad de vocales es de", vocales)