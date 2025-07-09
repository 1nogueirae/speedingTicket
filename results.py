"""
Resultados do speeding_ticket_me.py:

Verificando velocidade: 80 km/h
Tudo certo, pode seguir viagem
Verificando velocidade: 110 km/h
Você foi multado em R$100
Verificando velocidade: 130 km/h
Você foi multado em R$200

"""


"""
Resultados do speeding_ticket_chatgpt.py:

Verificando velocidade: 80 km/h
Tudo certo, pode seguir viagem
Verificando velocidade: 110 km/h
Você foi multado em R$100
Verificando velocidade: 130 km/h
Você foi multado em R$200
"""

"""
CONCLUSÕES:

Perguntas orientadoras: 
1. Ambas passaram em todos os testes?
    Sim, ambas as implementações passaram nos mesmos testes, produzindo os mesmos resultados para as mesmas entradas de velocidade.

2. Houve alguma diferença lógica entre as implementações?
    Não, ambas as implementações seguem a mesma lógica de verificação de velocidade e produzem as mesmas saídas, apesar do código do GPT ser ligeiramente diferente no elif, que cobre a condição de velocidade entre 100 e 120 de forma implícita.

3. Qual solução você acha mais eficiente ou legível?
    Ambas as soluções são eficientes e legíveis, mas a implementação do GPT é ligeiramente mais concisa, pois não verifica explicitamente o limite superior de 120 no segundo elif, já que a condição anterior já garante que a velocidade está entre 100 e 120. No entando, considero a minha implementação mais explícita e, portanto, mais fácil de entender para quem lê o código pela primeira vez.

"""

"""
# Após a execução do código, pedi outras duas versões ao ChatGPT:
# 
# 
# Uma versão otimizada que busca melhorar a legibilidade e eficiência.

def limitChecker(velocidade):
    # cada tupla é (limite_inferior, valor_da_multa)
    faixas = [
        (120, 200),
        (100, 100),
    ]
    for limite, multa in faixas:
        if velocidade > limite:
            print(f"Você foi multado em R${multa}")
            return
    print("Tudo certo, pode seguir viagem")

# Uma versão que usa diferentes estruturas de controle.

def limitChecker(velocidade):
    match True:
        case _ if velocidade > 120:
            multa = 200
        case _ if velocidade > 100:
            multa = 100
        case _:
            print("Tudo certo, pode seguir viagem")
            return

    print(f"Você foi multado em R${multa}")
"""

""" 
Em minha opinião, ambas as novas versões ficaram mais difíceis de ler, pois meu entendimento em Python ainda é básico e não consigo compreender bem o uso de certas estruturas, portanto, para mim, a primeira versão é a mais legível, apesar de compreender que para programadores mais experientes, as novas versões podem ser mais eficientes e legíveis.
"""

"""
Pedi para ele gerar testes para a função limitChecker, ele me retoronou o seguinte código:

import unittest
from io import StringIO
import sys

# importe sua função do módulo onde ela está definida
# por exemplo, se estiver em limit_checker.py:
from limit_checker import limitChecker

class TestLimitChecker(unittest.TestCase):
    def capture_output(self, velocidade):

        Captura o output impresso pela função limitChecker para a velocidade dada.
        Retorna a string impressa (sem quebras de linha extras).

        captured = StringIO()
        original_stdout = sys.stdout
        try:
            sys.stdout = captured
            limitChecker(velocidade)
        finally:
            sys.stdout = original_stdout
        return captured.getvalue().strip()

    def test_speed_above_120(self):
        self.assertEqual(
            self.capture_output(130),
            "Você foi multado em R$200"
        )

    def test_speed_between_101_and_120(self):
        self.assertEqual(
            self.capture_output(115),
            "Você foi multado em R$100"
        )

    def test_speed_at_120_boundary(self):
        self.assertEqual(
            self.capture_output(120),
            "Você foi multado em R$100"
        )

    def test_speed_at_100_boundary(self):
        self.assertEqual(
            self.capture_output(100),
            "Tudo certo, pode seguir viagem"
        )

    def test_speed_below_100(self):
        self.assertEqual(
            self.capture_output(90),
            "Tudo certo, pode seguir viagem"
        )

if __name__ == "__main__":
    unittest.main()
"""

"""
Esta versão de testes é muito mais complexa que a que eu criei, pois utiliza biblitocas e compõe um código mais robusto.
"""

"""
Ao pedir para ele analisar a minha função e meus resultados, ele me retornou o seguinte:

###
olha, tua função está funcionando direitinho pras faixas que você testou, mas tem alguns pontos que a gente pode questionar e talvez melhorar:

1. **condição do `elif`**
   você faz `elif speed > 100 and speed <= 120`, mas o `and speed <= 120` é redundante — se já chegou nesse bloco é porque não entrou no `if speed > 120`, então basta `elif speed > 100`. isso simplifica a leitura e evita checagens desnecessárias.

2. **comportamento em fronteiras**

   * exatamente 120 km/h: cai no `elif` (multa de R\$100), que parece o que você espera, certo?
   * exatamente 100 km/h: cai no `else` (“tudo certo”). confirme se esse resultado faz sentido pra você.

   às vezes vale a pena escrever testes explícitos para `speed == 120` e `speed == 100` pra documentar esse comportamento.

3. **valores atípicos**
   pense em como lidar com inputs fora do escopo normal, tipo velocidade negativa ou não numérica. vale a pena validar o parâmetro e, quem sabe, lançar um `ValueError` ou imprimir um aviso de “valor inválido”.

4. **print vs. return**
   se você quiser reutilizar o resultado (por exemplo, em outro código ou em testes unitários sem capturar stdout), talvez prefira que a função **retorne** a string da mensagem em vez de imprimi‑la. aí quem chamar faz o `print(limitChecker(v))` ou armazena o valor.

5. **testes adicionais**
   além das velocidades normais, inclua casos de limites exatos e inputs inesperados. e, se usar `pytest`, dá pra escrever um teste paramatrizado que percorre todas as faixas de uma vez.

---

pra seguir, me diga:

* quer refatorar pra retornar em vez de `print`?
* precisa tratar valores inválidos?
* vou sugerir algo em pytest ou continuo com unittest?
###
"""