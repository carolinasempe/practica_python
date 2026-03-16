#Escribe un programa que solicite al usuario una lista de palabras. Luego, construí una
#oración uniendo únicamente las palabras que tengan más de 3 letras, separadas por
#espacios. Las palabras cortas deben ser excluidas del resultado final
lista = []
while True:
    palabra = input("Ingrese una palabra: ")
    if palabra == "fin":
        break
    else:
        lista.append(palabra)
oracion = ""
for i in lista:
    if len(i)>3:
        oracion+= i + " "        
print(oracion)