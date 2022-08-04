import tkinter as tk 
from tkinter.font import BOLD 
import utils.generic as utl 

class RecetasMenu:

    def __init__(self):
        
        self.ventana = tk.Tk()
        self.ventana.title("Menu de Recetas")
        #el ancho y alto de la ventana
        w,h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        #formateo de tuplas
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg= "#fcfcfc")
        self.ventana.resizable(width = 0, height= 0)
        