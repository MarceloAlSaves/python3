print("Listas com pares e ímpares  ")
valores = []
for cont in range(0, 7):
    valores.append(int(input("Digite um valor: ")))
pares = []
impares = []
for v in valores:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f"Você digitou os valores {valores}")
print(f"Os valores pares digitados foram {pares}")
print(f"Os valores ímpares digitados foram {impares}")      