  print("Jogo de Dados")
from random import randint
from time import sleep
jogador = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
ranking = []
print("Valores sorteados:")
for k, v in jogador.items():
    print(f" - O {k} tirou {v} no dado.")
    sleep(1)
ranking = sorted(jogador.items(), key=lambda item: item[1], reverse=True)
print("-=" * 30)
print("== RANKING DOS JOGADORES ==")
for i, v in enumerate(ranking):
    print(f"   {i + 1}º lugar: {v[0]} com {v[1]}.")
    sleep(1)