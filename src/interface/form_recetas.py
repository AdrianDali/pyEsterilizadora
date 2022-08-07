import tkinter as tk 
from tkinter.font import BOLD 
import utils.generic as utl 
import components.components as cmp

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
        
        #header
        frame_top = tk.Frame(self.ventana, bd= 0 ,height=70, relief= tk.SOLID, bg = "#6a9ff6")
        frame_top.pack(side= "top" , fill = tk.X)
        #cmp.header(self.ventana)

        #FRAME PARA LISTA Y BOTONES DE RECETAS
        frame_left = tk.Frame(self.ventana, bd = 0 , relief= tk.SOLID, width= 40,padx=10, pady=10, bg = "#3a7ff6")
        frame_left.pack(side = "left", expand = tk.NO, fill = tk.BOTH)
        lista = tk.Listbox(frame_left, height= 10,bd = 0, relief = tk.SOLID, bg = "#fcfcfc", fg = "#666a88", font = ('Times', 15, BOLD ))
        lista.pack(side = "top", expand = tk.NO, fill = tk.X)
        lista.insert(tk.END, "Receta 1")
        lista.insert(tk.END, "Receta 2")
        boton_crear = tk.Button(frame_left, text = "Crear", font = ('Times', 15, BOLD ), bg = "green", bd = 0, fg = "#fff")
        boton_crear.pack(side = "top", expand = tk.NO, fill = tk.X)

        boton_editar = tk.Button(frame_left, text = "Editar", font = ('Times', 15, BOLD ), bg = "white", bd = 0, fg = "#fff")
        boton_editar.pack(side = "top", expand = tk.NO, fill = tk.X)

        boton_eliminar = tk.Button(frame_left, text = "Eliminar", font = ('Times', 15, BOLD ), bg = "red", bd = 0, fg = "#fff")
        boton_eliminar.pack(side = "top", expand = tk.NO, fill = tk.X)

        frame_right = tk.Frame(self.ventana, bd= 0 , relief= tk.SOLID, bg = "#3a2ff6")
        frame_right.pack(side = "right", expand = tk.YES, fill = tk.BOTH)
        
        scrollbar = tk.Scrollbar(frame_right , orient = tk.VERTICAL)
        scrollbar.pack(side = "right", fill = tk.Y)

