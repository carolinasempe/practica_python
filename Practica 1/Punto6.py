# Modifica el ejercicio 4 para que, en lugar de imprimir los números, genere dos listas:
# una con los múltiplos de 5 y otra con el resto de los números. Imprimí ambas listas al
# finalizar

# Punto 4:
# Crea un programa que dado un número N ingresado por el usuario, imprima los
# números del 1 al N pero saltee los múltiplos de 5. Nota: utilizá la sentencia continue
# donde haga falta

multiplos_5 = []
resto = []

numero = int(input("Ingrese un numero: "))

for i in range(0,numero):
    if (i % 5 == 0):
        multiplos_5.append(i)
    else:
        resto.append(i)

print(multiplos_5, resto)