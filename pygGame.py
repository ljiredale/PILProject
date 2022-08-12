import pygame
from tkinter import *
import tkinter as tk
import os
import sys
import random
bul = pygame.image.load("images/bullet.png")
ene = pygame.image.load("images/enemy.png")
bullets = []
enemies = []
enemyx = []
enemyy = []
class win(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1920x1080")
        self.configure(bg = "#781F0C")
        self.text = Label(self, text = "You Lost!", font = "Helvetica 24", bg = "#781F0C", fg = "#FFFFFF").place(relx=.5, rely=.1)
        self.butt = Button(self, text = "Click Here to Try Again", command = lambda:self.runAgain(), font = "Helvetica 20", bg = "#000000", fg = "#FFFFFF").place(relx=.4, rely=.5)
    def runAgain(self):
        self.destroy()
        runGame()
def lost():
    t = win()
    t.mainloop()
def bulletShot(x, y):
    bulRect = bul.get_rect()
    bulRect = bulRect.move(x+40,y+50)
    bullets.append(bulRect)
def enemyCreate():
    eneRect = ene.get_rect()
    eneRect = eneRect.move(random.randint(100,1800),random.randint(0,300))
    enemies.append(eneRect)
def runGame():
    pygame.init()
    size = width, height = 1920, 1080
    speed = [2.5,2.5]
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)

    ball = pygame.image.load("images/rocket.png")
    ballrect = ball.get_rect()
    ballrect = ballrect.move(920,700)
    for i in range(10):
        enemyx.append(random.randint(-1,1))
        enemyy.append(random.randint(-1,1))
    count = 0
    while 1:
        count += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bulletShot(ballrect.x, ballrect.y)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                speed[1] = -2.5
            if keys[pygame.K_DOWN]:
                speed[1] = 2.5
            if not keys[pygame.K_UP] and not keys[pygame.K_DOWN]: speed[1]=0

            if keys[pygame.K_RIGHT]:
                speed[0] = 2.5
            if keys[pygame.K_LEFT]:
                speed[0] = -2.5
            if not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]: speed[0] = 0

        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]
        for i in range(len(bullets)): 
            bullets[i] = bullets[i].move([0,-2.5])
        
        t = False
        for i in range(len(bullets)):
            for k in range(len(enemies)):
                if t == False:
                    if bullets[i].colliderect(enemies[k]):
                        bullets.pop(i)
                        enemies.pop(k)
                        t = True
        ktl = False
        for k in range(len(enemies)):
            if ktl == False:
                if enemies[k].colliderect(ballrect):
                    enemies.clear()
                    bullets.clear()
                    lost()

        if len(enemies) == 0 and count > 101:
            return True
                        
                    
        for i in range(len(enemies)):
            if enemies[i].left < 0 or enemies[i].right > width:
                enemyx[i] = -enemyx[i]
            if enemies[i].top < 0 or enemies[i].bottom > height:
                enemyy[i] = -enemyy[i]

        if count == 100:
            for i in range(10):
                enemyCreate()

        screen.fill(black)
        for i in range(len(bullets)):
            screen.blit(bul, bullets[i])
        for i in range(len(enemies)):
            enemies[i] = enemies[i].move(enemyx[i],enemyy[i])
            screen.blit(ene, enemies[i])
        screen.blit(ball, ballrect)
        pygame.display.flip()