import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

class mainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x600")
        self.startImg = Image.open("images/finalBg.png")
        self.startImg = self.startImg.resize((1000, 600))
        self.startImgPI = ImageTk.PhotoImage(self.startImg)
        self.label1 = Label(image = self.startImgPI)
        self.label1.image = self.startImgPI
        self.label1.place(x=0,y=0)