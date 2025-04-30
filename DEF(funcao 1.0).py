def funcao(zero):
    print("mostre a funcao requisitada:", zero)
def funcao2(n1,n2):
    print("mostre a funcao: ", n1, n2)

#main
# primeira forma de chamar a funcao sem dar a variavel

# chamando a funcao com um "input"
v1 = int(input("de o valor da funcao: "))
v2 = int(input("de o valor da funcao: "))

funcao(v1)
funcao(v2)

funcao2(v1,v2)