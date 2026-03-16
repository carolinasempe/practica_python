#Escribe un programa que solicite al usuario una cantidad de segundos y muestre
#cuántas horas, minutos y segundos equivalen. Por ejemplo, 3661 segundos son 1
#hora, 1 minuto y 1 segundo.

cantidad=int(input("Ingrese una cantidad de segundos: "))

segundos= cantidad % 60
minutos = cantidad // 60
horas = minutos // 60
minutos = minutos % 60

print("Horas: ", horas, ". Minutos: ", minutos, ". Segundos: ", segundos)