print("Função de contador")
def contar(numero):
    return len(str(numero))

numero = float(input("Digite o primeiro numero: "))
print(f"O numero {numero} tem {contar(numero)} caracteres.")
print("Digite o segundo numero: ")
numero2 = float(input())
print(f"O numero {numero2} tem {contar(numero2)} caracteres.")
