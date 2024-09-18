print("1.  Uso básico de print")
print("Nunca pares de aprender")
print()
print()

print("2. Uso de la coma en print")
print("Nunca", "pares", "de", "aprender")
print("Nunca" + "pares" + "de" + "aprender")
print("Nunca" + " " + "pares" + " " + "de" + " " + "aprender")
print()

print("3. Uso de sep")
print("Nunca", "pares", "de", "aprender", sep=", ")
print()

print("4. Uso de end")
print("Nunca", end=" ")
print("pares de aprender")
print()

print("5. Impresión de variables")
frase = "Nunca pares de aprender"
author = "Jair"
print("Frase:", frase, "Autor:", author)
print()

print("6. Uso de formato con f-strings")
frase = "Nunca pares de aprender"
author = "Jair"
print(f"Frase: {frase}, Autor: {author}")
print()

print("7. Uso de formato con format")
frase = "Nunca pares de aprender"
author = "Jair"
print("Frase: {}, Autor: {}".format(frase, author))
print()

print("8. Impresión con formato específico")
valor = 3.14159
print("Valor: {:.2f}".format(valor))
print()

print("9. Saltos de línea y caracteres especiales")
print("Hola\nmundo")
print('Hola soy \'Jair\'')
print("La ruta de archivo es: C:\\Users\\Usuario\\Desktop\\archivo.txt")
print()