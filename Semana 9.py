print ("Números del 0 al 10")
for número in range(11):
    print (número)




print ("Múltiplos de 4 entre el 0 al 100")    
for mult in range(0,101,4):
    print (mult)



print ("Temporizador de 5 segundos")
import os
import time
input ("Presione la tecla ENTER para iniciar el temporizador")
for var in range (5,-1,-1):
    print (var)
    time.sleep(1)
    os.system("cls")




print ("Deletreo")
print ("Introduzca una palabra:")
pal=input()
for letras in pal:
    print (letras)




print ("Tablas de multiplicar del 1 al 3")
for tabla in range(1, 4):
	for num in range(1, 13):
		print("%d * %d = %d" % (num,tabla,num*tabla))