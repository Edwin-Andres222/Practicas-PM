def RecibirNumero(num): 
    Dic = {'1': "Uno", '2': "Dos", '3': "Tres", '4': "Cuatro", '5': "Cinco", '6': "Seis", '7': "Siete", '8': "Ocho", '9': "Nueve", '10': "Diez", '11': "Once", '12': "Doce", '13': "Trece",  '14': "Catorce", '15': "Quince", '16': "Dieciseis", '17': "Diecisiete", '18': "Dieciocho", '19': "Diecinueve", '20': "Veinte", '0': "Cero"} 
    print(Dic.get(str(num))) 
RecibirNumero(input("Teclee un numero del 0 al 20: "))