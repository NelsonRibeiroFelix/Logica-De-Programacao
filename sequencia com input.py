def gerar_sequencia_inteiros():
    inicio = int(input("Digite o valor inicial da sequencia: "))
    fim = int(input("Digite o valor final da sequencia:"))

    print("\nA sequencia de numeros geradas é:")
    for numero in range(inicio, fim+1):
        print (numero)

gerar_sequencia_inteiros()