print("Aprimorando o dicionário de jogadores de futebol")
print("-" * 30)
jogador = {}
jogador['nome'] = str(input("Nome: "))
jogador['idade'] = int(input("Idade: "))
jogador['posicao'] = str(input("Posição: "))
jogador['gols'] = []
partidas = int(input("Número de partidas jogadas: "))
for p in range(partidas):
    jogador['gols'].append(int(input(f"Quantos gols na partida {p + 1}? ")))
jogador['total_gols'] = sum(jogador['gols'])
print("-=" * 30)
print("Dados do jogador:")
for k, v in jogador.items():
    print(f" - {k}: {v}")
    