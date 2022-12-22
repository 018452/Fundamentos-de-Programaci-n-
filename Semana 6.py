print ("Identificador de mayoría de edad")
print ("Ingrese su edad:")
edad=input()
edad=int(edad)
if edad>=18:
    print ("Usted es mayor de edad")




print ("Números mayores a 10")
print ("Ingrese el número:")
num=input()
num=int(num)
if num>10:
    print (num, "es mayor a 10")
else:
     print (num, "no es mayor a 10")




print ("Números pares o impares")
print ("Introduzca un número:") 
num=input()
num=int(num)
if num%2==0:
    print (num, "es par")
else:
    print (num, "es impar")




print ("Proceso de notas")
print("Ingrese su nota")
nota=input()
nota=int(nota)
if nota>=0 and nota<=10:
    print ("Reprobado")
elif nota>=11 and nota<=13:
    print ("Aprobado")
elif nota>=14 and nota<=16:
    print ("Bien")
elif nota>=17 and nota<=19:
    print ("Sobresaliente")
elif nota==20:
    print ("Perfecto")
else:
    print ("Nota incorrecta")




print ("Número positivo o negativo")
print ("Ingrese el número:")
num=input()
num=int(num)
if num>0:
    print (num, "es un número positivo")
elif num<0:
    print (num, "es un número negativo")
else:
    print ("El número", num, "no es ni negativo ni positivo")