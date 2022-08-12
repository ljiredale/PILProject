import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from pygGame import runGame
class mainWin(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x600")
        self.startImg = Image.open("images\start.png")
        self.startImg = self.startImg.resize((1000, 600))
        self.startImgPI = ImageTk.PhotoImage(self.startImg)
        self.label1 = Label(image = self.startImgPI)
        self.label1.image = self.startImgPI
        self.label1.place(x=0,y=0)
        self.after(10000, lambda: self.runNext())
    def runNext(self):
        self.label1.destroy()
        self.startImg2 = Image.open("images/second.png")
        self.startImg2 = self.startImg2.resize((1000,600))
        self.startImgPI2 = ImageTk.PhotoImage(self.startImg2)
        self.label2 = Label(image = self.startImgPI2)
        self.label2.image = self.startImgPI2
        self.label2.place(x=0,y=0)
        self.after(10000,lambda: self.playFirstGame())
    def playFirstGame(self):
        self.destroy()
        runGame()
        
        