import Alumno as Al

# Realizar un programa que contenga el siguiente menú
# 1.- Registro 2.- Inicio de sesión 3.- Salida

z=0
miAlumno = Al.Alumno()
miAlumno.AltaAlumno('Admin','admin','ADMIN','DIOS','MDMD123','Cielo')
tupla = []
tupla.append([miAlumno.Usuario,miAlumno.Password,miAlumno.Rol,miAlumno.Nombre,miAlumno.Curp,miAlumno.Ciudad])
while(z==0):
    mensaje = ""
    b=0
    print("""\tHOLA BIENVENIDO A MI PROGRAMA :D
    \tFAVOR DE SELECCIONAR LA OPCION DESEADA:
    \t1) - REGISTRARSE
    \t2) - INICIAR SESION
    \t3) - SALIR
    """)
    d = int(input("\tCapture opcion\t "))
    if(d == 1):
        miAlumno = Al.Alumno()
        rfc = input("Favor de capturar su RFC")
        for x in tupla:
            if(x[4] == rfc):
                print("Este curp ya existe, no se puede registrar")
                b = 1
                break
        if(b==0):
            a = input("Favor de ingresar el usuario ")
            b = input("Favor de ingresar su contraseña ")
            c = input("Favor de ingresar su nombre ")
            e = input("Favor de introducir su ciudad ")
            mensaje = miAlumno.AltaAlumno(a,b,"Cliente",c,rfc,e)
            tupla.append([miAlumno.Usuario,miAlumno.Password,miAlumno.Rol,miAlumno.Nombre,miAlumno.Curp,miAlumno.Ciudad])
            print(mensaje)
    elif(d==2):
        a = input("Favor de ingresar el usuario ")
        b = input("Favor de ingresar su contraseña ")
        for x in tupla:
            if(x[0]==a and x[1]==b and x[2]=='ADMIN'):
                for n in tupla:
                    print(n)
                break
            if(x[0]==a and x[1]==b):
                print(x)
                break
            else:
                print("USUARIO NO EXISTENTE")
    elif(d==3):
        print("ADIOS, CUIDATE:D")
        z=1
    z = int(input(""" 
    \t \t Desea realizar otra actividad?
    \t\t 0.Si      o       1.No
    """))
