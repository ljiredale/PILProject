import pygame
import sys, os
import tkinter
import random
import time
from finalScreen import mainWindow
with open("words.txt") as f:
    lines = f.readlines()
white = (255, 255, 255)
black = (0, 0, 0)
score = 0
class Asteroid(): #Asteroid Class. Gives basic variables 
    def __init__(self):
        self.mcolor = (0, 255, 0)
        self.scolor = (0, 0, 128)  
        self.white = (255, 255, 255)
        self.ast = pygame.image.load("images/rocket.png")
        font = pygame.font.Font('freesansbold.ttf', 32)
        self.astRect = self.ast.get_rect()
        self.astRect = self.astRect.move([random.randint(200,1600), random.randint(50,100)])
        self.word = lines[random.randint(0,1000)]
        self.word = self.word[:len(self.word)-1]
        self.wordRender = font.render(self.word, True, self.mcolor, self.scolor)
        self.wordRect = self.wordRender.get_rect()
        self.wordRect = self.wordRect.move(self.astRect.bottomleft)
        self.currentWord = self.word
        
        

    def letterInput(self, k): #this funtion takes a letter and changes the current word
        if k == self.currentWord[0] and len(self.currentWord) > 1:
            self.currentWord = self.currentWord[1:len(self.currentWord)]
        if len(self.currentWord) == 1 and k == self.currentWord[0]:
            self.stopAc()
    def asteroidMove(self, scr): #this moves the asteroid
        self.astRect = self.astRect.move([0, 2.5])
        self.wordRect = self.wordRect.move([0,2.5])
        scr.blit(self.ast, self.astRect)
        scr.blit(self.wordRender, self.wordRect)
    def check(self): #this will check if it is off the board
        if self.astRect.bottom > 1080:
            return False
        else:return True

def finalScreen(): #this goes onto the final screen
    mWind = mainWindow()
    mWind.mainloop()

class Scoreboard(): #this is to check the score
    def check(self):
        if score >= 500:
            return True

def wordCheck(word, ast): #this is to check if a word equals an asteroid, and if it does it gives points.
    global score
    for i in range(len(ast)):
        if ast[i].word == word:
            
            score += 50
            ast.pop(i)
            break

size = widh, height = 1920, 1080
asteroids = []
curWord = ""
def run(): #this runs it. sets some basic variables and objects for pygame
    pygame.init()
    font = pygame.font.Font('freesansbold.ttf', 32)
    start = time.time()
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
    sc = Scoreboard()
    while True: #while loop for game
        

        for event in pygame.event.get(): #this is loop to check for event in the game.
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        wordCheck(curWord, asteroids)
                        curWord = ""
                    elif event.key == pygame.K_BACKSPACE:
                        curWord = curWord[:len(curWord)-1]
                    elif event.key < 150 and event.key != pygame.K_SPACE:
                        curWord = curWord + alpha[event.key-97]

        if sc.check() == True: 
            pygame.quit()
            finalScreen()
                
        curWordRender = font.render(curWord, True, white, black)
        clock.tick(60)
        screen.blit(bg, (0,0))
        if time.time() - start >= 1:
            a = Asteroid()
            asteroids.append(a)
            start = time.time()
        for i in range(len(asteroids)):
            asteroids[i].asteroidMove(screen)
        for i in range(len(asteroids)):
            if asteroids[i].check() == False:
                pygame.quit()
                sys.exit()
        screen.blit(curWordRender,curWordRect)
        pygame.display.flip()
        
        
