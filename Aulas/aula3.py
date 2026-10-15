print("Dicionário em Python")
aluno = {}
aluno['nome'] = str(input("Nome: "))
aluno['media'] = float(input(f"Média de {aluno['nome']}: "))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprovado'
print("-=" * 30)
for k, v in aluno.items():
    print(f" - {k} é igual a {v}")