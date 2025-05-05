# 1. Função que recebe mensagem e número e a função main que a utiliza
def mostrar_mensagem_e_numero(mensagem, numero):
  """Mostra a mensagem e o número recebidos."""
  print(f"Mensagem: {mensagem}")
  print(f"Número: {numero}")

def main_exercicio1():
  """Função principal para o exercício 1."""
  mensagem_digitada = input("Digite uma mensagem: ")
  numero_digitado = int(input("Digite um número inteiro: "))
  mostrar_mensagem_e_numero(mensagem_digitada, numero_digitado)

# 2. Função para calcular a idade
def calcular_idade(ano_nascimento):
  """Calcula a idade com base no ano de nascimento."""
  ano_atual = 2025  # Considerando o ano atual como 2025
  idade = ano_atual - ano_nascimento
  return idade

def main_exercicio2():
  """Função principal para o exercício 2."""
  ano = int(input("Digite o seu ano de nascimento: "))
  idade_calculada = calcular_idade(ano)
  print(f"Sua idade é: {idade_calculada} anos.")

# 3. Função para somar três valores
def somar_tres_valores(valor1, valor2, valor3):
  """Soma três valores e retorna o resultado."""
  soma = valor1 + valor2 + valor3
  return soma

def main_exercicio3():
  """Função principal para o exercício 3."""
  num1 = int(input("Digite o primeiro valor inteiro: "))
  num2 = int(input("Digite o segundo valor inteiro: "))
  num3 = int(input("Digite o terceiro valor inteiro: "))
  resultado_soma = somar_tres_valores(num1, num2, num3)
  print(f"A soma dos valores é: {resultado_soma}")

# 4. Elaboração e resolução de um problema com função
# Enunciado do problema:
# Crie uma função que receba o valor do raio de um círculo e calcule a sua área.
# A função principal (main) deve ler o valor do raio digitado pelo usuário,
# chamar a função de cálculo da área e exibir o resultado.

import math

def calcular_area_circulo(raio):
  """Calcula a área de um círculo dado o seu raio."""
  area = math.pi * (raio ** 2)
  return area

def main_exercicio4():
  """Função principal para o exercício 4."""
  raio_digitado = float(input("Digite o valor do raio do círculo: "))
  area_calculada = calcular_area_circulo(raio_digitado)
  print(f"A área do círculo com raio {raio_digitado} é: {area_calculada:.2f}")

# Chamando as funções main para executar cada exercício
if __name__ == "__main__":
  print("--- Exercício 1 ---")
  main_exercicio1()
  print("\n--- Exercício 2 ---")
  main_exercicio2()
  print("\n--- Exercício 3 ---")
  main_exercicio3()
  print("\n--- Exercício 4 ---")
  main_exercicio4()