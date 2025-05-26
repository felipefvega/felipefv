#VARIABLES
usuario1 = None
usuario2 = None
usuario3 = None

password1 = None
password2 = None
password3 = None

#LOGIN
userPass= None
intentos = 0


while True:

    opt = input("""
                     ELIJA UNA OPCIÓN:
                    1) INICIAR SESIÓN
                    2) REGISTRARSE
                    3) SALIR
                    
                    """)
    
    match opt:
        case "1":
            if usuario1 == None and usuario2 == None and usuario3 == None:
                print("NO EXISTE REGISTRO DE USUARIOS. POR FAVOR, REGISTRARSE")
            else: 
                while True:
                    usuarioLogin = input("INGRESE SU USUARIO: ")
                    if usuarioLogin == usuario1:
                        userPass = password1
                        break

                    elif usuarioLogin == usuario2:
                        userPass = password2
                        break
                    elif usuarioLogin == usuario3:
                        userPass = password3
                        break
                    else:
                        print("USUARIO INVÁLIDO, POR FAVOR INTENTE NUEVAMENTE")
                
                while intentos != 3:
                    passwordLogin = input("INGRESE SU CONTRASEÑA: ")
                    if

                      

            
        case "2":

            nuevoUsuario = input("INGRESE EL USER A REGISTRAR: ")
            nuevaContraseña = input("INGRESE CONTRASEÑA A REGISTRAR: ")

            while True:
                nuevaContraseñaVerif = input("INGRESE CONTRASEÑA NUEVAMENTE: ")

                if nuevaContraseñaVerif == nuevaContraseña:
                    print("REGISTRO EXITOSO.")
                    break
                else:
                    print("LAS CONTRASEÑAS INGRESADAS SON DISTINTAS, INTENTAR NUEVAMENTE")
                    
            if usuario1 == None and password1 == None:
                usuario1 = nuevoUsuario
                password1 = nuevaContraseñaVerif
            elif usuario2 == None and password2 == None:
                usuario2 = nuevoUsuario
                password2 = nuevaContraseñaVerif
            elif usuario3 == None and password3 == None:
                usuario3 = nuevoUsuario
                password3 = nuevaContraseñaVerif


            
        case "3":
            break
    