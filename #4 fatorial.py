#4. Função para calcular o fatorial:

def fatorial(n):
  """
  Calcula o fatorial de um número inteiro não negativo.

  Args:
    n: Um número inteiro não negativo.

  Returns:
    O fatorial de n. Retorna 1 se n for 0 ou 1. Retorna None para números negativos.
  """
  if not isinstance(n, int) or n < 0:
    return None  # Fatorial não definido para não inteiros ou negativos
  elif n == 0 or n == 1:
    return 1
  else:
    resultado = 1
    for i in range(2, n + 1):
      resultado *= i
    return resultado

# Programa principal
if __name__ == "__main__":
  num = int(input("Digite um número inteiro não negativo: "))
  fat = fatorial(num)
  if fat is not None:
    print(f"O fatorial de {num} é {fat}")
  else:
    print("Não é possível calcular o fatorial para o valor digitado.")