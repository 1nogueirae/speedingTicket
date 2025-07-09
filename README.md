# 🚓 Speeding Ticket
### Comparando soluções humanas e IA (ChatGPT) em Python

Este repositório contém a implementação de uma atividade do curso técnico do IMD, baseada no estudo de Sarsa et al. (2022), cujo objetivo é exercitar habilidades de programação em Python através da resolução do problema “Multa por velocidade” e a comparação com soluções geradas por inteligência artificial.

## 🧠 Descrição da Atividade

A proposta consiste em:

1. Implementar manualmente uma função com as seguintes regras:
   - Acima de **120 km/h** → imprime: `Você foi multado em R$200`
   - Entre **101 e 120 km/h** → imprime: `Você foi multado em R$100`
   - Até **100 km/h** → imprime: `Tudo certo, pode seguir viagem`

2. Solicitar ao ChatGPT uma solução alternativa, registrando o **prompt utilizado**.

3. Criar um **conjunto de testes** para verificar ambas as soluções, incluindo:
   - Velocidade abaixo de 100
   - Velocidade entre 101 e 119
   - Velocidade acima de 120
   - Casos-limite: 100, 120 e 121

4. **Comparar os resultados dos testes**:
   - Ambas as soluções passaram em todos os testes?
   - Há diferenças na lógica ou na legibilidade?

5. Gerar com o ChatGPT:
   - Uma **versão otimizada** da função
   - Uma versão com **estruturas de controle diferentes**

6. Avaliar com o apoio do ChatGPT:
   - Clareza e eficiência das alternativas
   - Cobertura dos testes gerados automaticamente
   - Comentários críticos sobre a solução manual

---

## 🎯 Objetivos Educacionais

- Exercitar **condicionais** e **estruturas de decisão** em Python
- Praticar **testes automatizados**
- Desenvolver senso crítico sobre **eficiência** e **legibilidade de código**
- Analisar o uso de **IA como apoio no aprendizado de programação**

---

## 🤖 Ferramentas Utilizadas

- Python
- ChatGPT (OpenAI)
- VSCode

---

## 📌 Referência

Sarsa, M., Hellas, A., Leinonen, J., & Vihavainen, A. (2022).
Automatic generation of programming exercises and code explanations with large language models.
arXiv. https://arxiv.org/pdf/2206.11861

---

## ✍️ Autor

Este projeto foi desenvolvido como parte de uma atividade acadêmica.  
**Emanuel Nogueira** – Estudante de C&T e Técnico IMD/UFRN.

---