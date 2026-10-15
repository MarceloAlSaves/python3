print("Valores únicos na lista")
valores = []
for cont in range(0, 5):
    valores.append(int(input("Digite um valor: ")))
print(f"Você digitou os valores {valores}")
valores_unicos = list(set(valores))
print(f"Os valores únicos digitados foram {valores_unicos}")
