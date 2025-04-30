#Crie uma lista com os elementos 1, 2, 3 e adicione o número 4 ao final.
lista = [1, 2, 3]  
lista.append(4)    
print(lista)       

#Acesse qualquer elemento da lista ["a", "b", "c"].
lista = ["a", "b", "d", "f", "g", "h", "i", "j", "l", "m", "n", "o", "p", "q", "r", "s"]
elemento = lista[1] #Zero seria o primeiro elemento da lista
print(elemento)

#Remova o primeiro elemento da lista [10, 20, 30] (use del ou método de lista).
lista = [10, 20, 30]
del lista[0]
print(lista)  

#Crie uma lista vazia e verifique se ela está vazia (use if com len()).
lista = []
if len(lista) == 0:
    print("Vazia")