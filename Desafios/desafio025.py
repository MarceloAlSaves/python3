print("Função para fatorial")
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

print("Digite um número para calcular o fatorial:")
numero = int(input())
resultado = fatorial(numero)
print(f"O fatorial de {numero} é: {resultado}")