print("Números pares")
vec=int(input("¿Cuántos números desea ingresar:")) 
cont = 0;
for var in range(vec):
	num = int(input("Escriba un número:"))
	if num % 2 == 0:
		cont = cont + 1
print("Ha introducido",cont,"números pares.")




print("Números mayores, menores e iguales a 0")
cont_positivos= 0
cont_negativos= 0
cont_ceros= 0
cantidad_num=int(input("¿Cuántos númueros desea ingresar?:"))
for i in range(1,cantidad_num+1):
    print("Número",i,":",end="")
    num=int(input())
    if num>0:
        cont_positivos=cont_positivos+1
    else:
        if num<0: 
            cont_negativos=cont_negativos+1
        else:
            cont_ceros=cont_ceros+1
print("Cantidad de números positivos:",cont_positivos)  
print("Cantidad de números negativos:",cont_negativos)       
print("Cantidad de números iguales a 0:",cont_ceros)




print("Números pares entre dos números")
num1=int(input("Introduzca el primer número:"))
num2=int(input("Introduzca el degundo número:"))
if num1 % 2==1:
    num1=num1+1
for num1 in range(num1, num2+1, 2):
    print(num1," ",end="")




print("Ahorro mensual")
ahorro_acum=0;
for mes in range(1,13):
    cant_mensual=float(input("¿Cuánto ha ahorrado en el mes %d?:"%mes))
    ahorro_acum= ahorro_acum + cant_mensual
    print("En el mes ",mes," lleva ahorrando: ",ahorro_acum)



print("Sueldo semanal")
horas_acum=0;
sueldo_por_hora= float(input("¿Cuánto es su sueldo por hora?:"))
for dia in range (1,7):
    horas= int(input("¿Cuántas horas trabaja el día %d?:"%dia))
    horas_acum= horas_acum + horas
print("Horas acumuladas en la semana:",horas_acum)
print("Sueldo:",horas_acum*sueldo_por_hora)