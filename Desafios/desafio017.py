print("Unindo dicionários e listas")
if continuar == 'N':
    print("Cadastro encerrado.")

pessoa = dict()
pessoa['nome'] = str(input("Nome: "))
pessoa['idade'] = int(input("Idade: "))
pessoa['sexo'] = str(input("Sexo [M/F]: ")).strip().upper()
pessoa['peso'] = float(input("Peso (kg): "))
pessoa['altura'] = float(input("Altura (m): "))
continuar = str(input("Quer continuar? [S/N]: ")).strip().upper()
print("-=" * 30)
print("Dados da pessoa:")
for k, v in pessoa.items():
    total: pessoa['imc'] = pessoa['peso'] / (pessoa['altura'] ** 2)
print(f" - {k}: {v}")