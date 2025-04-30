#Verifique se um número (por exemplo, 7) é par ou ímpar.
numero = 7
if numero % 2 == 0:  # "=" é usado para atribuir valores e / "==" comparar se x é igual a 10
    print("Par")
else:
    print("Ímpar") 

#Dadas duas variáveis a = 5 e b = 10, imprima qual é a maior.
a = 5
b = 10
if a > b:
    print("A é maior")
else: 
    print("B é maior")

#Dada uma variável idade = 18, verifique se a pessoa pode dirigir (idade >= 18).
idade = 18
if idade >= 18:
    print ("é de maior")

#Dada uma string "python", verifique se ela está vazia ou não.
texto = input("Digite um texto ou número: ").strip()  # Remove espaços no início/fim

print(f"Você digitou: '{texto}'")
if texto:
    print("Não está vazia")
else:
    print("Está vazia")
