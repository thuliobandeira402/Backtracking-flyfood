entrada = """4 5
0 0 0 0 D
0 A 0 0 0
0 0 0 0 C
R 0 B 0 0
"""
linhas = [linha.strip() for linha in entrada.strip().splitlines() if linha.strip()]
dimensoes = linhas[0].split()
num_linhas = int(dimensoes[0])
num_colunas = int(dimensoes[1])
pontos = {}
matriz = linhas[1:]
entrega_rotas = {}
menor_custo = float("inf")

for i in range(num_linhas):
    valores = matriz[i].split()
    for j in range(num_colunas):
        simbolo = valores[j]
        if simbolo != '0':
            pontos[simbolo] = (i, j)

origem = pontos.pop('R')
print(pontos)
entregas = list(pontos.keys())
print(entregas)


def gerar_passeios(cidades):
    resultado = []

    def backtrack(atual, restantes):
        if not restantes:
            resultado.append(atual[:])
            return
        for i in range(len(restantes)):
            atual.append(restantes[i])
            backtrack(atual, restantes[:i] + restantes[i+1:])
            atual.pop()

    backtrack([], cidades)
    return resultado

rotas = gerar_passeios(entregas)

def calculo_manhatan(origem, destino):
    return abs(origem[0] - destino[0]) + abs(origem[1] - destino[1])

for rota in rotas:
    custo_total = 0
    ponto_atual = origem
    for entrega in rota:
        destino = pontos[entrega]
        custo_total += calculo_manhatan(ponto_atual, destino)
        ponto_atual = destino
    custo_total += calculo_manhatan(ponto_atual, origem)
    if custo_total < menor_custo:
        menor_custo = custo_total
    rota_tupla = tuple(rota)
    entrega_rotas[rota_tupla] = custo_total
    print(f"Rota: {rota}, Custo total: {custo_total}")

rotas_minimas = [k for k, v in entrega_rotas.items() if v == menor_custo]

print(f"Rotas com o menor valor: {rotas_minimas}")
print(f"Menor valor: {menor_custo}")
