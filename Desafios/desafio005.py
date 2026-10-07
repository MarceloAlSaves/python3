print("Contando vogais em uma tupla")
palavras = ("aprender", "programar", "linguagem", "python", "curso", "grátis", "estudar", "praticar", "trabalhar", "mercado", "programador", "futuro")
for p in palavras:
    print(f"\nNa palavra {p.upper()} temos ", end="")
    for letra in p:
        if letra in "aeiou":
            print(letra, end=" ")