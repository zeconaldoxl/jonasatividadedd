import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Definindo os vértices do cubo em um espaço tridimensional
vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

# Definindo as arestas que conectam os vértices, formando as linhas do cubo
edges = (
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 7), # Modifique
    (6, 7),
    (4, 6), # Modifique
    (0, 4),
    (1, 5),
    (2, 7), # Modifique
    (3, 6)  # Modifique
)

def draw_cube():
    # Iniciando o desenho das linhas
    glBegin(GL_LINES)
    # Desenhando cada aresta do cubo usando os vértices conectados por cada aresta
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])  # Define a posição do vértice atual
    glEnd()  # Finaliza o desenho das linhas

def main():
    # Inicializando o pygame e configurando a janela com buffer duplo e OpenGL
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
    # Configurando a perspectiva da câmera
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    
    # Movendo a câmera para longe do cubo
    glTranslatef(0.0, 0.0, -5)

    # Loop principal do programa
    while True:
        # Gerenciando eventos de saída
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Rotacionando o cubo um pouco em cada frame
        glRotatef(1, 3, 1, 1)
        
        # Limpando a tela e o buffer de profundidade para atualizar a cena
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # Chamando a função que desenha o cubo
        draw_cube()
        
        # Atualizando a tela
        pygame.display.flip()
        
        # Atraso para manter a rotação contínua, mas lenta
        pygame.time.wait(10)

if _name_ == "_main_":
    main()