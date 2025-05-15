#1. Função para verificar se um número é positivo, nulo ou negativo:

def positivo_nulo_negativo(numero):
  """
  Verifica se um número é positivo, nulo ou negativo e imprime a mensagem correspondente.

  Args:
    numero: Um número real.
  """
  if numero > 0:
    print("Valor Positivo")
  elif numero == 0:
    print("Valor nulo")
  else:
    print("Valor negativo")

# Programa principal
if __name__ == "__main__":
  num = float(input("Digite um número: "))
  positivo_nulo_negativo(num)