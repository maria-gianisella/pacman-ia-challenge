# Pac-Man

Este é um clone simples do clássico jogo Pac-Man desenvolvido em Python com a biblioteca Pygame.

## Descrição

O Pac-Man é um jogo clássico de arcade onde o jogador controla um personagem chamado Pac-Man através de um labirinto. O objetivo é comer todas as bolinhas brancas (pontos) espalhadas pelo labirinto enquanto evita ser capturado pelos fantasmas que patrulham o local.

Este projeto é uma implementação simplificada do Pac-Man em que o jogador controla o Pac-Man usando as teclas de seta do teclado. O Pac-Man se move pelo labirinto, comendo bolinhas brancas para ganhar pontos. Existem também frutas bônus espalhadas pelo labirinto, que concedem mais pontos quando comidas.

O projeto utiliza uma variedade de algoritmos de IA para controlar os agentes no jogo Pac-Man, como a busca A* e o algoritmo guloso. Além disso, utiliza os algoritmps de Busca A* e Euclideano para calcular distâncias.

## Funcionalidades

- Controle do Pac-Man através das teclas de seta do teclado.
- Labirinto com obstáculos (paredes) e bolinhas brancas (pontos) para o Pac-Man comer.
- Frutas bônus que aparecem aleatoriamente e concedem mais pontos quando comidas.
- Fantasmas que patrulham o labirinto e perseguem o Pac-Man.
- Interface gráfica simples usando a biblioteca Pygame.

## Requisitos

Para executar este jogo, você precisará ter o Python instalado em seu sistema. Além disso, é necessário instalar a biblioteca Pygame. Você pode instalar o Pygame usando o seguinte comando pip:

```
pip install pygame
```

## Como Jogar

1. Clone ou baixe o repositório para o seu computador.
2. Certifique-se de ter o Python e o Pygame instalados.
3. Navegue até o diretório do projeto e execute o arquivo `pacman.py` usando o Python:

```
python pacman.py
```

4. Use as teclas de seta do teclado para controlar o Pac-Man e tente comer todas as bolinhas brancas para ganhar pontos.
5. Evite os fantasmas, pois ser pego por um resultará em game over.
6. As frutas bônus aparecerão aleatoriamente e concederão mais pontos quando comidas.
