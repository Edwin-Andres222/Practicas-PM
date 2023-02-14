#7 Formateo y conversiones
# Escribir un programa que muestre un menú con 2 opciones la primera opción “1.- Imprimir 
# YYYY/MM/DD” la segunda “2.- Imprimir MM/DD/YYYY” una vez seleccionada la opción imprimir la fecha 
# del día de hoy en el formato seleccionado.
import time
print(""" Hola, Bievenido aun programa mas que imprime la fecha
Opciones:
1. Imprimir YYYY/MM/DD
2. Imprimir DD/MM/YYYY """)

if(int(input('Favor de introducir el numero del formato que desee imprimir :'))==1):
    print (time.strftime("%y/%m/%d"))
else:
    print (time.strftime("%d/%m/%y"))