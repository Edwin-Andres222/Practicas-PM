#5 Manejo de información
# Escribir una función que reciba n parámetros de llave valor e imprima la 
# información en formato “{llave}”: “{Valor}”

def funcion(**nparametros): 
    print(type(nparametros)) 
    print(nparametros) 

funcion(llave1="EQUIPO 4", llave2="a", llave3=6500, llave4=9999.99) 