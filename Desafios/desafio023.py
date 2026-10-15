import random
print("Função que sorteia um numero e soma")

def somar_numeros():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    return num1 + num2

resultado = somar_numeros()
print(f"A soma dos numeros sorteados é: {resultado}")
print("Valores sorteados: ", num1, "e", num2)