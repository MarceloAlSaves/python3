print("Cadastro de trabalhadores")
print("-" * 30)
print("Digite os dados do trabalhador:")
trabalhador = {}
trabalhador['nome'] = str(input("Nome: "))
trabalhador['idade'] = int(input("Idade: "))
trabalhador['ctps'] = int(input("Carteira de Trabalho (0 não tem): "))
if trabalhador['ctps'] != 0:
    trabalhador['contratacao'] = int(input("Ano de contratação: "))
    trabalhador['salario'] = float(input("Salário: R$ "))
    trabalhador['aposentadoria'] = (trabalhador['idade'] + ((trabalhador['contratacao'] + 35) - 2024))
print("-=" * 30)
print("Dados do trabalhador:")
for k, v in trabalhador.items():
    print(f" - {k}: {v}")