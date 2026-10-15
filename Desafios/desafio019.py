print("Função que calcula a área")
def calcular_area(base, altura):
    return base * altura

Largura = float(input("Digite a largura: "))
Altura = float(input("Digite a altura: "))
area = calcular_area(Largura, Altura)
print(f"A área do retângulo é: {area}")
