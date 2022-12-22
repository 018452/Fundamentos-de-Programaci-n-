print ("Venta de producto")
print ("Ingresar el nombre del producto:")
var1=input()
print ("Ingresar el precio del producto:")
var2=input()
var2=int(var2)
print ("Ingresar la cantidad del producto:")
var3=input()
var3=int(var3)
imp=var2*var3
dscto=imp*0.05
total=imp-dscto
print ("El nombre del producto es:", var1)
print ("El precio del producto es:", var2)
print ("La cantidad del producto es:", var3)
print ("El importe es:", imp)
print ("El descuento es:", dscto)
print ("El total a pagar es:", total)




print ("Distancia entre dos números")
print ("Ingrese el primer número:")
num1=input()
num1=int(num1)
print ("Ingrese el segundo número:")
num2=input()
num2=int(num2)
print ("Distancia:", abs(num1-num2))




print ("Un número mayor que otro")
print ("Ingrese el primer número:")
var1=input()
var1=int(var1)
print ("Ingrese el segundo número:")
var2=input()
var2=int(var2)
if var1>var2:
    print (var1, "es mayor que", var2)
elif var1<var2:
    print (var1, "es menor que", var2)
else:
    print (var1, "es igual a", var2)




print ("Día de la semana")
print ("Escriba el número de un día de la semana (1-7):") 
día=input()
día=int(día)
if día==1:
    print ("Lunes")
elif día==2:
    print ("Martes")
elif día==3:
    print ("Miércoles")
elif día==4:
    print ("Jueves")
elif día==5:
    print ("Viernes")
elif día==6:
    print ("Sábado")
elif día==7:
    print ("Domingo")
else:
    print ("Día incorrecto")



print ("Días de un mes")
print ("Introduzca el número de un mes del año (1-12):")
mes=input()
mes=int(mes)
if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
    print ("31 días")
elif mes==2:
    print ("28 o 29 días")
elif mes==4 or mes==6 or mes==9 or mes==11:
    print("30 días")
else: 
    print ("Mes incorrecto")