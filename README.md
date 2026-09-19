# FlyFood: Otimização de Rotas para Drones Urbanos 🚁

Este repositório contém a implementação do **FlyFood**, um sistema algorítmico de roteamento para entregas via drones desenvolvido nativamente em Python. O projeto modela o clássico Problema do Caixeiro-Viajante (PCV) num ambiente urbano, com o objetivo de encontrar a rota exata de menor custo energético e preservar a autonomia de voo.

Desenvolvido como parte do Projeto Interdisciplinar (PISI II) do curso de Bacharelado em Sistemas de Informação (BSI) da Universidade Federal Rural de Pernambuco (UFRPE).

---

## 📌 O Problema
A verticalização das cidades sobrecarrega fortemente a logística terrestre. O uso de drones surge como uma alternativa rápida, mas esbarra na limitação crítica da bateria das aeronaves. 

Para contornar isto, o sistema abstrai o mapa da cidade para uma matriz bidimensional, extrai as coordenadas da base de recarga ($R$) e dos pontos de entrega ($P$), e utiliza a **Distância de Manhattan** ($d(P_1, P_2) = |x_1 - x_2| + |y_1 - y_2|$). Esta métrica é essencial, pois reflete os deslocamentos ortogonais reais exigidos por corredores urbanos formados por quarteirões e edifícios.

## ⚙️ Arquitetura e Metodologia
O núcleo de processamento foi construído **100% do zero**, sem qualquer dependência de bibliotecas externas de otimização combinatória ou teoria dos grafos.

* **Abordagem Exata:** Implementação de procura sistemática por **Força Bruta através de Backtracking Recursivo**.
* **Exploração Exaustiva:** A árvore de decisão gera absolutamente todas as permutações possíveis de trajeto (cíclicas, com partida e retorno obrigatório à base).
* **Tratamento de Simetrias:** O código atualiza dinamicamente o menor custo acumulado e guarda casos de empates técnicos (rotas distintas que partilham a mesma distância mínima total).

## 📊 Complexidade Computacional
A análise assintótica do algoritmo desenvolvido revela uma dualidade entre o tempo de processamento e a leveza na alocação de memória:
* **Complexidade Temporal | $\mathcal{O}(n! \cdot n)$:** Comportamento hiperfatorial. A necessidade de avaliar o espaço amostral completo garante a solução matematicamente ótima, mas sacrifica a escalabilidade comercial.
* **Complexidade Espacial | $\mathcal{O}(n)$:** Elevada eficiência de recursos. A pegada de memória é ditada apenas pela profundidade máxima da pilha de recursão.

## 🔬 Testes de Esforço e Desempenho
Os testes empíricos foram conduzidos num ambiente de hardware controlado (Processador AMD Ryzen 5 3600 @ 3.6GHz, 6 Núcleos / 12 Threads, 16GB RAM) para validar o comportamento da complexidade em casos práticos:

| Cenário de Teste | Entregas ($n$) | Rotas Avaliadas | Custo Mínimo | Tempo de Execução |
| :--- | :---: | :---: | :---: | :---: |
| **Pequena Escala (4x4)** | 4 nós | 24 | 14 unidades | **< 0,001 s** |
| **Teste de Esforço (6x6)** | 13 nós | 6.227.020.800 | 28 unidades | **~6h 11m** (371,22 min) |

*Nota de Investigação: No cenário de estresse com 13 nós, o sistema identificou 262 rotas perfeitamente empatadas com o custo mínimo de 28 unidades, confirmando a alta simetria das malhas ortogonais (Manhattan).*

## 🚀 Como Executar
O algoritmo requer apenas uma instalação padrão do Python, não sendo necessária a configuração de ambientes virtuais complexos.

```bash
# Clone este repositório
git clone [https://github.com/thuliobandeira402/Backtracking-flyfood.git](https://github.com/thuliobandeira402/Backtracking-flyfood.git)

# Aceda à diretoria do projeto
cd Backtracking-flyfood

# Execute o script principal (ajuste conforme o seu ficheiro de entrada de matriz)
python main.py
```
## 👨‍💻 Autores
* **Pedro Coutinho** - *pedro.coutinho@ufrpe.br*
* **Renato Rodrigues** - *renato.filho@ufrpe.br*
* **Taryk Melo** - *taryk.melo@ufrpe.br*
* **Thúlio Bandeira** - *thulio.roberto@ufrpe.br*
