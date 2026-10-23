print("ficha de jogador")
def ficha_jogador(nome, gols):
    if nome == "":
        nome = "<desconhecido>"
    if gols == "":
        gols = 0
    return f"O jogador {nome} fez {gols} gol(s) no campeonato."