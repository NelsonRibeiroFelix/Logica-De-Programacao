soma_das_notas = 0
total_alunos = 5
for i in range (0, total_alunos):
    nota = float(input(f"Digite sua nota do aluno {i + 1}: "))
    soma_das_notas += nota

media = soma_das_notas / total_alunos
print (f"A media aritimetica da turme é: {media:.2f}")
