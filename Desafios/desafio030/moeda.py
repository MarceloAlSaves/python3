def aumentar(preço, taxa):
    """
    Aumenta o preço em uma determinada taxa percentual.
    
    :param preço: O preço original.
    :param taxa: A taxa percentual de aumento.
    :return: O preço aumentado.
    """
    res = preço + (preço * taxa / 100)
    return res

def diminuir(preço, taxa):
    """
    Diminui o preço em uma determinada taxa percentual.
    
    :param preço: O preço original.
    :param taxa: A taxa percentual de diminuição.
    :return: O preço diminuído.
    """
    res = preço - (preço * taxa / 100)
    return res

def dobro(preço):
    """
    Calcula o dobro do preço.
    
    :param preço: O preço original.
    :return: O dobro do preço.
    """
    res = preço * 2
    return res

def metade(preço):
    """
    Calcula a metade do preço.
    
    :param preço: O preço original.
    :return: A metade do preço.
    """
    res = preço / 2
    return res

def moeda(preço, moeda='R$'):
    """
    Formata o preço para o formato monetário.
    
    :param preço: O preço a ser formatado.
    :param moeda: A moeda a ser utilizada (padrão: 'R$').
    :return: O preço formatado.
    """
    return f'{moeda}{preço:.2f}'.replace('.', ',')