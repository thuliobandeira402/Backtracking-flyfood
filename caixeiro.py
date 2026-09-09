entrada = """6 6
A 0 B 0 C 0
0 D 0 E 0 F
0 0 G 0 H 0
I 0 0 J 0 K
0 L 0 0 0 0
0 0 0 0 0 R
"""
linhas = [linha.strip() for linha in entrada.strip().splitlines() if linha.strip()]
dimensoes = linhas[0].split()
num_linhas = int(dimensoes[0])
num_colunas = int(dimensoes[1])
pontos = {}
matriz = linhas[1:]

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


# MELHORES ROTAS E CUSTO 
menor_custo = float("inf")
melhores_rotas = []

def calculo_manhatan(origem, destino):
    return abs(origem[0] - destino[0]) + abs(origem[1] - destino[1])

def gerar_passeios(cidades):
    resultado = []

    def backtrack(atual, restantes):

        if not restantes:
            global menor_custo, melhores_rotas
            custo_rota_atual = 0
            ponto_atual = origem

            for entrega in atual:
                destino = pontos[entrega]
                custo_rota_atual += calculo_manhatan(ponto_atual, destino)
                ponto_atual = destino

            custo_rota_atual += calculo_manhatan(ponto_atual, origem)

            if custo_rota_atual < menor_custo:
                menor_custo = custo_rota_atual
                melhores_rotas = [atual[:]]

            elif custo_rota_atual == menor_custo:
                melhores_rotas.append(atual[:])

            return

        for i in range(len(restantes)):
            atual.append(restantes[i])
            backtrack(atual, restantes[:i] + restantes[i+1:])
            atual.pop()

    backtrack([], cidades)
    return resultado

gerar_passeios(entregas)

print(  
      f'O menor custo de rota foi: {menor_custo}\n'
      f'As melhores rotas foram: {melhores_rotas}')