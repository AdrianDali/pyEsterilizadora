import tkinter as tk 
from tkinter.font import BOLD 
import utils.generic as utl 
from interface.form_recetas import RecetasMenu

class MasterPanel:
    def recetas(self):
        self.ventana.destroy()
        RecetasMenu()

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Form Master")
        #el ancho y alto de la ventana
        w,h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        #formateo de tuplas
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg= "#fcfcfc")
        self.ventana.resizable(width = 0, height= 0)

        frame_form_top = tk.Frame(self.ventana,height=50, bd = 0, relief=tk.SOLID, bg = "black")
        #que se expanda en x
        frame_form_top.pack (side = "top", fill= tk.X)

        title = tk.Label(frame_form_top, text = "Sterilization System", font = ('Times', 30 ), bg = "red", fg = "#666a88", pady = 0)
        #que se expanda 
        title.pack(expand= tk.YES, fill = tk.BOTH)
        inicio = tk.Button(self.ventana, text = "Recetas", font = ('Times', 15, BOLD ), bg = "#3a7ff6", bd = 0, fg = "#fff",command=self.recetas )
        inicio.pack(fill= tk.X ,padx =20 , pady = 20)
        self.ventana.mainloop()