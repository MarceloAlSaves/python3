print("Funções para votações")
from datetime import date

def votar():
    hoje = date.today()
    ano = hoje.year
    nascimento = int(input("Digite seu ano de nascimento: "))
    idade = ano - nascimento
    if idade < 16:
        print("Você não pode votar.")
    elif (16 <= idade < 18) or (idade > 70):
        print("Seu voto é opcional.")
    else:
        print("Seu voto é obrigatório.")

print("qual é a sua idade?")
votar()
