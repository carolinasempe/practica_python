#Crea un programa que dado un número N ingresado por el usuario, imprima los
#números del 1 al N pero saltee los múltiplos de 5. Nota: utilizá la sentencia continue
#donde haga falta

numero = int(input("Ingrese un numero: "))

for i in range(0,numero):
    if (i % 5 == 0):
        continue
    print(i)