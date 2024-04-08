import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def calcular_caminho(inicio):
  return [0, 3, 4, 7, 8]

caminhos = calcular_caminho(0)

# Crie uma matriz 3x3 preenchida com zeros
matriz_caminho = np.zeros((3, 3))

# Crie uma figura e um eixo
fig, ax = plt.subplots()

# Mostre a matriz como uma imagem, com os nós do caminho em branco e o resto em preto
ax.imshow(matriz_caminho, cmap='gray_r')

# Desenhe linhas de grade
ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
ax.set_xticks(np.arange(-0.5, 3, 1))
ax.set_yticks(np.arange(-0.5, 3, 1))

# Esconda os rótulos dos eixos
ax.set_xticklabels([])
ax.set_yticklabels([])

# Inicialize a bolinha no ponto de partida
bolinha, = ax.plot([], [], 'o', color='red')

# Função de inicialização para a animação
def init():
    bolinha.set_data([], [])
    return bolinha,

# Função de animação que será chamada sequencialmente
def animate(i):
    if i < len(caminhos):
        no = caminhos[i]
        x, y = divmod(no, 3)
        bolinha.set_data(y, x)
    return bolinha,

# Crie a animação
ani = FuncAnimation(fig, animate, frames=len(caminhos), init_func=init, blit=True, interval=500)

plt.show()
