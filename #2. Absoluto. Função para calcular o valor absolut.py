#2. Função para calcular o valor absoluto:

def valor_absoluto(numero):
  """
  Calcula o valor absoluto (módulo) de um número.

  Args:
    numero: Um número.

  Returns:
    O valor absoluto do número.
  """
  if numero >= 0:
    return numero
  else:
    return numero * -1

# Programa principal
if __name__ == "__main__":
  num = float(input("Digite um número: "))
  abs_valor = valor_absoluto(num)
  print(f"O valor absoluto de {num} é {abs_valor}")