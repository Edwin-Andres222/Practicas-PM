#2 Manejo y manipulación de elementos de una lista

# Escribir un programa que almacene el abecedario en una lista, 
# elimine de la lista las letras que ocupen 
# posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

lista = ["A","B","C","D","E","F","G","H","I",
"J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

print(len(lista))

for i in range(len(lista), 0 , -1):
    if i % 3 == 0:
        lista.pop(i-1)

print(lista)