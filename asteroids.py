import pygame
import sys, os
import tkinter
import random
import time

with open("words.txt") as f:
    lines = f.readlines()
white = (255, 255, 255)
black = (0, 0, 0)
score = 0
class Asteroid():
    def __init__(self):
        self.mcolor = (0, 255, 0)
        self.scolor = (0, 0, 128)  
        self.white = (255, 255, 255)
        self.ast = pygame.image.load("images/rocket.png")
        self.astRect = self.ast.get_rect()
        self.astRect = self.astRect.move([random.randint(200,1600), random.randint(50,100)])
        self.word = lines[random.randint(0,1000)]
        self.word = self.word[:len(self.word)-1]
        self.wordRender = font.render(self.word, True, self.mcolor, self.scolor)
        self.wordRect = self.wordRender.get_rect()
        self.wordRect = self.wordRect.move(self.astRect.bottomleft)
        self.currentWord = self.word
        
        

    def letterInput(self, k):
        if k == self.currentWord[0] and len(self.currentWord) > 1:
            self.currentWord = self.currentWord[1:len(self.currentWord)]
        if len(self.currentWord) == 1 and k == self.currentWord[0]:
            self.stopAc()
    def asteroidMove(self, scr):
        self.astRect = self.astRect.move([0, 2.5])
        self.wordRect = self.wordRect.move([0,2.5])
        scr.blit(self.ast, self.astRect)
        scr.blit(self.wordRender, self.wordRect)


class Scoreboard():
    pass

def wordCheck(word):
    global score
    for i in range(len(asteroids)):
        if asteroids[i].word == word:
            score += 50
            asteroids.pop(i)
            break


pygame.init()
start = time.time()
font = pygame.font.Font('freesansbold.ttf', 32)
clock = pygame.time.Clock()
size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)
bg = pygame.image.load("images/bg.png")
bg = pygame.transform.scale(bg, (1920, 1080))
asteroids = []
curWord = ""
curWordRender = font.render(curWord, True, white, black)
curWordRect = curWordRender.get_rect()
curWordRect = curWordRect.move([900,20])
alpha = ['a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    wordCheck(curWord)
                    curWord = ""
                elif event.key == pygame.K_BACKSPACE:
                    curWord = curWord[:len(curWord)-1]
                elif event.key < 150 and event.key != pygame.K_SPACE:
                    curWord = curWord + alpha[event.key-97]

            
            
    curWordRender = font.render(curWord, True, white, black)
    clock.tick(60)
    screen.blit(bg, (0,0))
    print(time.time() - start)
    if time.time() - start >= 1:
        a = Asteroid()
        asteroids.append(a)
        start = time.time()
    for i in range(len(asteroids)):
        asteroids[i].asteroidMove(screen)
    screen.blit(curWordRender,curWordRect)
    pygame.display.flip()
    
    
    
    