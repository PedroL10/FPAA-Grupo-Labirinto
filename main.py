import heapq

LIVRE = '0'
OBSTACULO = '1'
INICIO = 'S'
FIM = 'E'

MOVIMENTOS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def heuristica(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def encontrar_posicoes(matriz):
    inicio = fim = None
    for i, linha in enumerate(matriz):
        for j, valor in enumerate(linha):
            if valor == INICIO:
                inicio = (i, j)
            elif valor == FIM:
                fim = (i, j)
    return inicio, fim

def vizinhos(pos, matriz):
    for dx, dy in MOVIMENTOS:
        x, y = pos[0] + dx, pos[1] + dy
        if 0 <= x < len(matriz) and 0 <= y < len(matriz[0]):
            if matriz[x][y] != OBSTACULO:
                yield (x, y)

def reconstruir_caminho(came_from, atual):
    caminho = [atual]
    while atual in came_from:
        atual = came_from[atual]
        caminho.append(atual)
    caminho.reverse()
    return caminho

def a_star(matriz, inicio, fim):
    fila = []
    heapq.heappush(fila, (heuristica(inicio, fim), inicio))
    
    came_from = {}
    g_score = {inicio: 0}
    visitados = set()

    while fila:
        _, atual = heapq.heappop(fila)

        if atual == fim:
            return reconstruir_caminho(came_from, atual)

        if atual in visitados:
            continue
        visitados.add(atual)

        for viz in vizinhos(atual, matriz):
            temp_g_score = g_score[atual] + 1
            if viz not in g_score or temp_g_score < g_score[viz]:
                came_from[viz] = atual
                g_score[viz] = temp_g_score
                f_score = temp_g_score + heuristica(viz, fim)
                heapq.heappush(fila, (f_score, viz))
    
    return None

def exibir_labirinto_com_caminho(matriz, caminho):
    labirinto_copia = [linha.copy() for linha in matriz]
    for x, y in caminho:
        if labirinto_copia[x][y] not in (INICIO, FIM):
            labirinto_copia[x][y] = '*'
    for linha in labirinto_copia:
        print(' '.join(linha))
    print()

def executar_teste(labirinto):
    inicio, fim = encontrar_posicoes(labirinto)
    if not inicio or not fim:
        print("Erro: ponto inicial (S) ou final (E) não encontrado.")
        return

    caminho = a_star(labirinto, inicio, fim)

    if caminho:
        print("Caminho encontrado:")
        print(caminho)
        exibir_labirinto_com_caminho(labirinto, caminho)
    else:
        print("Sem solucao.")

def main():
    testes = [
        [
            ['S', '0', '1', '0', '0'],
            ['0', '0', '1', '0', '1'],
            ['1', '0', '1', '0', '0'],
            ['1', '0', '0', 'E', '1']
        ],
        [
            ['S', '1', '0', '0', 'E'],
            ['0', '1', '0', '1', '1'],
            ['0', '0', '0', '0', '0'],
            ['1', '1', '1', '1', '0']
        ],
        [
            ['S', '1', '1', '1', '1'],
            ['1', '1', '1', '1', '1'],
            ['1', '1', '1', '1', 'E'],
            ['1', '1', '1', '1', '1']
        ],
        [
        ['S', '0', '0', '0', '1', '0', 'E'],
        ['1', '1', '1', '0', '1', '0', '1'],
        ['0', '0', '0', '0', '1', '0', '0'],
        ['0', '1', '1', '1', '1', '1', '0'],
        ['0', '0', '0', '0', '0', '0', '0'],
        ['1', '1', '1', '1', '1', '1', '0'],
        ['0', '0', '0', '0', '0', '0', '0']
]
    ]

    for i, labirinto in enumerate(testes):
        print(f"Teste {i + 1}:")
        executar_teste(labirinto)

if __name__ == '__main__':
    main()
