print("Função que descobre o maior numero")
def maior_numero(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
maior = maior_numero(num1, num2)
print(f"O maior numero entre {num1} e {num2} é: {maior}")