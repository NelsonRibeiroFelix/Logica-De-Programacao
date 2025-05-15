#3. Simulação de calculadora com quatro operações:

def adicao(num1, num2):
  """Realiza a operação de adição e mostra o resultado."""
  resultado = num1 + num2
  print(f"{num1} + {num2} = {resultado}")

def subtracao(num1, num2):
  """Realiza a operação de subtração e mostra o resultado."""
  resultado = num1 - num2
  print(f"{num1} - {num2} = {resultado}")

def multiplicacao(num1, num2):
  """Realiza a operação de multiplicação e mostra o resultado."""
  resultado = num1 * num2
  print(f"{num1} x {num2} = {resultado}")

def divisao(num1, num2):
  """Realiza a operação de divisão e mostra o resultado."""
  if num2 == 0:
    print("Erro: Divisão por zero!")
  else:
    resultado = num1 / num2
    print(f"{num1} / {num2} = {resultado}")

# Programa principal
if __name__ == "__main__":
  operador = input("Digite a operação (+, -, x, /): ")
  num1 = float(input("Digite o primeiro valor: "))
  num2 = float(input("Digite o segundo valor: "))

  if operador == '+':
    adicao(num1, num2)
  elif operador == '-':
    subtracao(num1, num2)
  elif operador == 'x':
    multiplicacao(num1, num2)
  elif operador == '/':
    divisao(num1, num2)
  else:
    print("Operador inválido!")