print ("Perímetro y área de un rectángulo")
print ("Ingrese la medida de la base:")
base=input()
base=int(base)
print ("Ingrese la medida de la altura:")
altura=input()
altura=int(altura)
per=(base+altura)*2
area=base*altura
print ("El perímetro es:", per)
print ("El área es:", area)




print ("Saludo")
print ("Ingrese su nombre de usuario")
nomprod=input()
print ("Bienvenido", nomprod)




print ("Operaciones básicas")
print ("Ingresar el primer valor:")
var1=input()
var1=int(var1)
print ("Ingresar el segundo valor:")
var2=input()
var2=int(var2)
sum=var1+var2
res=var1-var2
mult=var1*var2
div=var1//var2
print ("La suma es:", sum)
print ("La resta es:", res)
print ("La multiplicación es:", mult)
print ("La división es:", div)




print ("El promedio de tres números")
print ("Ingrese el primer valor:")
var1=input()
var1=int(var1)
print ("Ingrese el segundo valor:")
var2=input()
var2=int(var2)
print ("Ingrese el tercero valor:")
var3=input()
var3=int(var3)
sum=var1+var2+var3
prom=sum//3
print ("El promedio de los tres números es:", prom)




print ("Convertidor de minutos a horas")
print ("Ingrese la cantidad de minutos:")
min=input()
min=int(min)
hora=min//60
minu=min%60
print (hora, "horas y", minu, "minutos.")

