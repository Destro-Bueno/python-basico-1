notas= [5, 7, 4, 5, 8]

soma= 0

for nota in notas:
    soma = soma + nota

media = soma / 5

print("media da Turma: ", media)
print("Notas da Turma: ", max(notas))
print("Notas acima da media:", min(notas))

