
"""
# 1º Prompt utilizado para gerar o código no ChatGPT com Reasoning: :
    Crie uma função chamada medida_velocidade, que recebe um único parâmetro, velocidade, e segue estas condições:
    Se a velocidade for acima de 120, imprima “Você foi multado em R$200”;
    Se a velocidade for acima de 100 e até 120, imprima “Você foi multado em R$100”;
    Caso contrário, imprima “Tudo certo, pode seguir viagem”.
"""


### Código gerado pelo ChatGPT com Reasoning
def limitChecker(velocidade):
    if velocidade > 120:
        print("Você foi multado em R$200")
    elif velocidade > 100:  # isso cobre >100 e até 120
        print("Você foi multado em R$100")
    else:
        print("Tudo certo, pode seguir viagem")
###

### O main foi feito por mim, para testar o código
def main():
    from test_data import LIMIT_CASES
    for speed in LIMIT_CASES[0]:
        print(f"Verificando velocidade: {speed} km/h")
        limitChecker(speed)


main()