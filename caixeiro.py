from gerador_entrada import gerar_entrada
import json
import os

entrada = gerar_entrada()

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

def calcular_tempo(lista_cidades):
    import time
    inicio = time.time()
    gerar_passeios(lista_cidades)
    fim = time.time()
    duracao_minutos = (fim - inicio) / 60
    return f'O Tempo de Execução foi de: {duracao_minutos:.2f} minutos', duracao_minutos

mensagem_tempo, tempo_execucao_minutos = calcular_tempo(entregas)

print(
      f'{mensagem_tempo}\n',
      f'O menor custo de rota foi: {menor_custo}\n'
      f'As melhores rotas foram: {melhores_rotas}')

# SALVAR RESULTADO EM JSON

resultado = {
    "menor_custo": menor_custo,
    "melhores_rotas": [" ".join(rota) for rota in melhores_rotas],
    "tempo_execucao_minutos": f"{round(tempo_execucao_minutos, 2)} minutos"
}

caminho_saida = os.path.join(os.path.dirname(__file__), "rotas.json")
with open(caminho_saida, "w", encoding="utf-8") as arquivo:
    json.dump(resultado, arquivo, ensure_ascii=False, indent=2)