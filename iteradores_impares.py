# Criar um iterador para los numeros impares

# Limite
limit = 10

# Criar iterador
odd_itter = iter(range(1, limit + 1, 2))

# Usar iterador
for num in odd_itter:
  print(num)