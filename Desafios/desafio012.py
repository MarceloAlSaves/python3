print("palpites para a Mega Sena")
palpites = []
for p in range(0, 6):
    palpites.append(int(input(f"Digite o {p + 1}º palpite: ")))
print("-=" * 30)
print(f"Os palpites foram: {palpites}")
