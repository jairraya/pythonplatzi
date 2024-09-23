try:
  divisor = int(input("Insira um núnero divisor: "))
  result = 100 / divisor
  print(result)

except ZeroDivisionError as e:
  print("Error: O divisor não pode ser zero")
  print("Ocorreu um erro: ",e)

except ValueError as e:
  print("Error: Você precisa inserir um número válido")
  print("Ocorreu um erro: ",e)