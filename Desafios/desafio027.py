print("Validando dados de entrada")
def validar_entrada(numero):
    if not isinstance(numero, int):
        return "Número inválido. Por favor, insira um número inteiro."
    if numero < 0:
        return "Número inválido. Por favor, insira um número não negativo."
    else:
        return f"O número {numero} é válido."