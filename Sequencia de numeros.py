def gerar_sequencia_naturais():
    sequencia = list(range(11))
    return sequencia

def imprimir_sequencia(sequencia):
    print ("A sequencia dos numeros naturais de 0 a 10 é:")
    for numero in sequencia:
        print (numero)

numeros_naturais = gerar_sequencia_naturais()
imprimir_sequencia(numeros_naturais)