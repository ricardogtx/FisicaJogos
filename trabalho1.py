import pygame
from pygame.locals import *
from math import sqrt
import math

#Input do programa
vel = input('!! Escreva a velocidade: ')
graus = input('!! Escreva o angulo: ')
angulo = math.radians(graus)
vox = vel*abs(math.cos(angulo))


def VetorForca(r, v):
    rx, ry = r
    vx, vy = v
    V = sqrt(vx**2 + vy**2)
    return (-K * V * vx, 10 * m - K * V * vy)
    
# Constantes globais da simulacao
dt = 1/30.
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
Fx, Fy = VetorForca((rx, ry), (vx, vy))
ax, ay = Fx /m, Fy / m

larguraTela, alturaTela = 192*5, 108*5	
tela = pygame.display.set_mode((larguraTela, alturaTela))
bola = pygame.image.load("bola.gif")
relogio = pygame.time.Clock()

x, y = 0, 450

pygame.init()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()   
            raise SystemExit

    # Calcula as aceleracoes
    Fx, Fy = VetorForca((rx, ry), (vx, vy))
    ax = Fx / m
    ay = Fy / m

    # Atualiza as velocidades
    vx = vx + ax * dt
    vy = vy + ay * dt

    x += vx
    y += vy

    if x < 0:
        vx = 0
    if y < 0 or y > alturaTela-30:
        vy = (vy*(-0.98))
        if y > alturaTela-30:
            y = alturaTela-30
        if y < 0:
            y=0
                
    tela.fill((255,255,255))
    tela.blit(bola, (x, y))
    relogio.tick(1000/30.0)
    pygame.display.flip()
 
