print("Clave correcta")
secreto="2022"
clave=input("Ingrese su clave:")
while clave!=secreto:
    print("Clave incorrecta")
    clave=input("Ingrese su clave:")
print("¡Bienvenido!")




print("Clave correcta: Otra")
secreto="2002"
clave=input("Ingrese su clave:")
while clave!=secreto:
    print("Clave incorrecta")
    otra=input("¿Desea introducir otra clave?(S/N):")
    if otra.upper()=="N":  
        break;
    clave=input("Ingrese su clave:")
if clave==secreto:
    print("¡Bienvenido!")




print("Factorial")
resultado=1
num=int(input("Ingrese un numero:"))
contador=2
while contador <=num:
    resultado=resultado*contador
    contador=contador+1
print("El resultado es:",resultado)




print("Potencia")
base=int(input("Ingrese la base de la potencia:"))
while True:
    exponente=int(input("Ingrese el exponente de la potencia:"))
    if exponente<0:
        print("ERROR: el exponente debe ser positivo")
    if exponente>=0:
        break;
potencia=1
for i in range(1,exponente+1):
    potencia=potencia*base
print("La potencia es:",potencia)   




while True:
    # mostrar menu
    print("Menú de recomendaciones")
    print("   1. Literatura")
    print("   2. Cine")
    print("   3. Música")
    print("   4. Videojuegos")
    print("   5. Salir")
    # ingresar una opcion
    opcion = int(input("Elija una opción (1-5): "))
    # procesar esa opción
    if opcion == 1:
        print("Lecturas recomendables:")
        print(" + Esperándolo a Tito y otros cuentos de fútbol (Eduardo Sacheri)")
        print(" + El juego de Ender (Orson Scott Card)")
        print(" + El sueño de los héroes (Adolfo Bioy Casares)")
    elif opcion == 2:
        print("Películas recomendables:")
        print(" + Matrix (1999)")
        print(" + El último samuray (2003)")
        print(" + Cars (2006)")
    elif opcion == 3:
        print("Discos recomendables:")
        print(" + Despedazado por mil partes (La Renga, 1996)")
        print(" + Búfalo (La Mississippi, 2008)")
        print(" + Gaia (Mago de Oz, 2003)")
    elif opcion == 4:
        print("Videojuegos clásicos recomendables")
        print(" + Día del tentáculo (LucasArts, 1993)")
        print(" + Terminal Velocity (Terminal Reality/3D Realms, 1995)")
        print(" + Death Rally (Remedy/Apogee, 1996)")
    elif opcion == 5:
        print("Gracias, vuelva pronto")
        break;
    else:
        print("Opción no válida")
