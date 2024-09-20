def add(a, b):
  return a + b

def substract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

def calculator():
  while True:
    print("Selecionen uma operação:")
    print("1. Soma")
    print("2. Subtração")
    print("4. Multiplicação")
    print("3. Divisão")
    print("5. Sair")

    option = input("Insira a sua opção (1,2,3,4,5):")

    if option == "5":
      print("Saindo da calculadora.")
      break

    if option in ["1", "2", "3", "4"]:
      num1 = float(input("Insira o primeiro número: "))
      num2 = float(input("Insira o segundo número: "))

      if option == "1":
        print("A soma é:", add(num1, num2))
      elif option == "2":
        print("A subtração é:", substract(num1, num2))
      elif option == "3":
        print("A multiplicação é:", multiply(num1, num2))
      elif option == "4":
        print("A divisão é:", divide(num1, num2))
      
    else:
       print("Opção não válida, tente outra vez.")

calculator()