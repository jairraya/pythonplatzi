# 1. Doble de los Números
# Dada una lista de números [1, 2, 3, 4, 5], crea una nueva lista que contenga el doble de cada número usando una List Comprehension.

numeros = [1, 2, 3, 4, 5]
dobles = [x * 2 for x in numeros]
print("Dobles:", dobles)


# 2. Filtrar y Transformar en un Solo Paso
# Tienes una lista de palabras ["sol", "mar", "montaña", "rio", "estrella"] y quieres obtener una nueva lista con las palabras que tengan más de 3 letras y estén en mayúsculas.

palabras = ["sol", "mar", "montaña", "rio", "estrella"]
palabras_filtradas = [palabra.upper() for palabra in palabras if len(palabra) > 3]
print("Palabras filtradas y en mayúsculas:", palabras_filtradas)


# 3. Crear un Diccionario con List Comprehension
# Tienes dos listas, una de claves ["nombre", "edad", "ocupación"] y otra de valores ["Juan", 30, "Ingeniero"]. Crea un diccionario combinando ambas listas usando una List Comprehension.

claves = ["nombre", "edad", "ocupación"]
valores = ["Juan", 30, "Ingeniero"]

diccionario = {claves[i]: valores[i] for i in range(len(claves))}
print("Diccionario creado:", diccionario)


# 4. Anidación de List Comprehensions
# Dada una lista de listas (una matriz):

# pythonCopiar código
# matriz = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# Calcula la matriz traspuesta utilizando una List Comprehension anidada.

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpuesta_comprehension = [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]
print("Transpuesta con List Comprehension:", transpuesta_comprehension)


# 5. Extraer Información de una Lista de Diccionarios
# Dada una lista de diccionarios que representan personas:

# pythonCopiar código
# personas = [
#     {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
#     {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
#     {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
#     {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}
# ]
# Extrae una lista de nombres de personas que viven en “Madrid” y tienen más de 30 años.

personas = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
    {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}
]

nombres_madrid = [persona["nombre"] for persona in personas if persona["ciudad"] == "Madrid" and persona["edad"] > 30]
print("Nombres de personas en Madrid mayores de 30 años:", nombres_madrid)
      

# 6. List Comprehension con un else
# Dada una lista de números [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], crea una nueva lista multiplicando por 2 los números pares y dejando los impares como están.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
transformados = [x * 2 if x % 2 == 0 else x for x in numeros]
print("Números transformados:", transformados)
