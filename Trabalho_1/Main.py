import pygame
from pygame.locals import *

import math

from Player import Player
from Sprite import Sprite
from PygameWrapper import PygameWrapper

#Input do programa
vel = input('!! Escreva a velocidade: ')
graus = input('!! Escreva o angulo: ')
angulo = math.radians(graus)
vox = vel*abs(math.cos(angulo))

def VetorForca(r_, v_, K_, m_):
    rx, ry = r_
    vx, vy = v_
    V = math.sqrt(vx**2 + vy**2)
    return (-K_ * V * vx, 10 * m_ - K_ * V * vy)

def gameLoop():
    # Constantes globais da simulacao
    dt = 1/30.0
    T = 2
    r0 = (0, 1)
    v0 = (vox, vel)
    m = 0.1
    k = 0.1
    rho = 1.2
    A = 0.02
    Cd = 0.1

    # Constantes derivadas
    N = int(T / dt)
    K = 0.5 * rho * A * Cd
    rx, ry = r0
    vx, vy = v0
    Fx, Fy = VetorForca((rx, ry), (vx, vy), K, m)
    ax, ay = Fx /m, Fy / m

    pygameWrapper = PygameWrapper(192*5, 108*5, "Jogo Pygame")

    sprite = Sprite("bola.gif")

    player = Player(0, 450, sprite)
    player.vx, player.vy = vx, vy

    tjx = []
    tjy = []
    tj = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygameWrapper.close()
                raise SystemExit

        # Calcula as aceleracoes
        Fx, Fy = VetorForca((rx, ry), (player.vx, player.vy), K, m)
        ax = Fx / m
        ay = Fy / m

        # Atualiza as velocidades
        player.vx = player.vx + ax * dt
        player.vy = player.vy + ay * dt

        player.x += player.vx
        player.y += player.vy

        if player.x < 0:
            player.vx = 0
        if player.y < 0 or player.y > pygameWrapper.screenHeight-30:
            player.vy = (player.vy*(-0.98))
            if player.y > pygameWrapper.screenHeight-30:
                player.y = pygameWrapper.screenHeight-30
            if player.y < 0:
                player.y = 0
                    
        pygameWrapper.screen.fill((255,255,255))
        pygameWrapper.screen.blit(sprite.image, (player.x, player.y))

        tjx.append(player.x)
        tjy.append(player.y)
        tj += 1

        for i in range(tj):
            pygame.draw.circle(pygameWrapper.screen, (255, 0, 0), [12+int(tjx[i]), 12+int(tjy[i])], 3, 0)

        pygameWrapper.clock.tick(1000/30.0)
        pygame.display.flip() 

def main():
    gameLoop()

if __name__ == "__main__":
    main()
