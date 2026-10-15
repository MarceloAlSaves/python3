print("Cadastro de jogadores de futebol")
print("-" * 30)
jogador = {}
jogador['nome'] = str(input("Nome: "))
jogador['idade'] = int(input("Idade: "))
jogador['posicao'] = str(input("Posição: "))
jogador['gols'] = int(input("Número de gols: "))
if jogador['gols'] > 0:
    jogador['media_gols'] = jogador['gols'] / jogador['idade']
print("-=" * 30)
print("Dados do jogador:")
for k, v in jogador.items():
    print(f" - {k}: {v}")
