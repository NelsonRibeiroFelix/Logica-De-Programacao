def classificar_valores(valor1, valor2):

  if valor1 < valor2:
    return valor1, valor2
  else:
    return valor2, valor1


valor1 = int(input("Digite o primeiro valor inteiro: "))
valor2 = int(input("Digite o segundo valor inteiro: "))

menor, maior = classificar_valores(valor1, valor2)
print(f"Os valores em ordem crescente são: {menor}, {maior}")