print("Analisando e gerando dicionário de dados")
def analisar_dados(lista):
    if not isinstance(lista, list):
        return "Entrada inválida. Por favor, insira uma lista de números."
    if len(lista) == 0:
        return "A lista está vazia. Por favor, insira uma lista com números."
    
    total = len(lista)
    maior = max(lista)
    menor = min(lista)
    soma = sum(lista)
    media = soma / total
    
    return {
        "total": total,
        "maior": maior,
        "menor": menor,
        "soma": soma,
        "media": media
    }