def decimal_para_binario(numero_decimal):

    if numero_decimal == 0:
        return "0"

    binario = ""
    while numero_decimal > 0:
        resto = numero_decimal % 2
        binario = str(resto) + binario
        numero_decimal //= 2
    return binario

numero = int(input("Digite um número decimal: "))
binario = decimal_para_binario(numero)
print(f"O número binário de {numero} é: {binario}")

#Ou em forma mais simples usando a funcao "BIN()"

numero = int(input("Digite um número decimal: "))
binario = bin(numero)[2:]  # Remove o prefixo "0b"
print(f"O número binário de {numero} é: {binario}")