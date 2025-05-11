# PathFinder - Resolvendo o Labirinto 2D com o Algoritmo A\*

## Introducao

Este projeto implementa o algoritmo A\* para encontrar o menor caminho entre dois pontos em um labirinto 2D. O objetivo e simular o funcionamento de um robo de resgate que precisa sair de um ponto inicial e chegar a um destino, desviando de obstaculos.

## Algoritmo Utilizado

O algoritmo A\* e uma tecnica de busca heuristica que combina duas informacoes:

1. O custo real do caminho ja percorrido (g)
2. Uma estimativa do custo ate o destino (h), calculada aqui pela distancia de Manhattan

Formula: f(n) = g(n) + h(n)

Essa combinacao permite que o algoritmo encontre o menor caminho de forma eficiente.

## Como Executar

1. Certifique-se de ter o Python instalado (versao 3.6 ou superior).
2. Salve o codigo no arquivo `main.py`.
3. No terminal, execute o arquivo com o seguinte comando: python main.py

O programa ira testar diferentes labirintos e mostrar os caminhos encontrados.

## Regras do Labirinto

- O labirinto e representado por uma matriz onde:

  - S representa o ponto de partida
  - E representa o ponto de chegada
  - 0 representa uma celula livre
  - 1 representa um obstaculo

- O robo pode se mover apenas nas direcoes cima, baixo, esquerda e direita
- Cada movimento tem custo 1

## Funcionalidades

- Leitura de diferentes labirintos
- Validacao de existencia dos pontos S e E
- Exibicao do caminho em coordenadas
- Visualizacao do labirinto com o caminho marcado

## Casos Tratados

- Labirinto com caminho possivel
- Labirinto sem solucao
- Labirinto com multiplas rotas (escolhe a menor)
