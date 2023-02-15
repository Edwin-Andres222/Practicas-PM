#4 Entrada de datos y estructuración.
# Revisar su retícula para escribir un programa que cree un diccionario vacío para 
# que el usuario capture las materias y créditos de su semestre preferido (inferior a 8vo) 
# al final imprimir en el formato “{asignatura}” tiene “{créditos}” créditos. 
# Y la suma de todos los créditos del semestre.

reticula = {} 
n = 0 
totalC = 0 
semestre = int(input("Teclee el semestre: ")) 

if semestre <= 2: 
    aux = 6 
else: 
    aux = 7 

while n < aux: 
    n = n + 1 
    nombre = input("Teclee el nombre de la materia " + str(n) + ": ") 
    credit = int(input("Teclee la cantidad creditos: ")) 
    reticula[nombre] = credit
    totalC = totalC + credit 

for llave, valor in reticula.items(): 
    print("\nLa asignatura " + llave + " tiene " + str(valor) + " creditos.") 

print("\nCreditos totales del semestre: " + str(totalC)) 