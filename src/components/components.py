import tkinter as tk 
from tkinter.font import BOLD
import sys 
import time 

def header(ventana):
    header = tk.Frame(ventana, height = 50, bd = 0, padx = 10, relief = tk.SOLID, bg = "black")
    header.pack(side = "top", fill = tk.X)
    