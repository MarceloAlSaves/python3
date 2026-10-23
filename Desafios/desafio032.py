print("Funções aprofundadas em Python")
n1 = int(input("Digite um inteiro: "))
n2 = int(input("Digite outro inteiro: "))

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')

print(f'A soma de {n1} + {n2} é igual a {soma(n1, n2)}')
try:
    print(f'A soma de {n1} + {n2} é igual a {soma(n1, n2)}')
except TypeError:
    print("Erro: digite apenas números inteiros.")
else:
    print("Função executada com sucesso.")