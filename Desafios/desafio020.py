print("Um print especial")
def print_especial(texto):
    print("-" * 30)
    print(texto)
    print("-" * 30)

valor = str(input("Digite um texto: "))
print_especial(valor)