import tkinter as tk 
from tkinter.font import BOLD

from matplotlib.pyplot import margins 
import utils.generic as utl 
#from interface.form_recetas import *
from interface.form_pre_calentamiento import PreCalentamiento
#import components.components as cmp 
import time
class MasterPanel:

    def times(self): 
        current_time = time.strftime("%H:%M:%S")
        self.clock.config(text = current_time)
        self.date.config(text = time.strftime("%d/%m/%Y"))
        self.clock.after(200, self.times)
        
        #self.date.after(200, self.times)

    def recetas(self):
        self.ventana.destroy()
        #RecetasMenu()

    def pre_calentamiento(self):
        self.ventana.destroy()
        PreCalentamiento()

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Form Master")
        #el ancho y alto de la ventana
        w,h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        #formateo de tuplas
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg= "#fcfcfc")
        self.ventana.resizable(width = 0, height= 0)

        frame_form_top = tk.Frame(self.ventana,height=50, bd = 0,padx= 10, relief=tk.SOLID, bg = "black")
        #que se expanda en x
        frame_form_top.pack (side = "top", fill= tk.X)

        title = tk.Label(frame_form_top, text = "Sterilization System", font = ('Times', 30 ), bg = "red", fg = "#666a88", pady = 0)
        title.pack(side = "left")
        
        #cmp.header(self.ventana)
        boton_recetas = tk.Button(self.ventana, text = "Recetas", font = ('Times', 15, BOLD ), bg = "#3a7ff6", bd = 0, fg = "#fff",command=self.recetas )
        boton_recetas.pack(fill= tk.X ,padx =20 , pady = 20)
     

        boton_recetas = tk.Button(self.ventana, text = "Inicio proceso", font = ('Times', 15, BOLD ), bg = "#3a7ff6", bd = 0, fg = "#fff",command=self.pre_calentamiento )
        boton_recetas.pack(fill= tk.X ,padx =20 , pady = 20)

        self.date =tk.Label(frame_form_top, font=('Times',15,BOLD)  ,bg = "#fcfcfc", fg = "#666a88", padx = 5)
        self.date.pack(side = "right")

        self.clock = tk.Label(frame_form_top, font = ('Times', 15, BOLD ), bg = "#6a9ff6", fg = "black", padx = 5)
        self.clock.pack(side = "right" )
        self.times()
        
        text_temperatura = tk.Label(frame_form_top, text = "Temperatura: ", font = ('Times', 15, BOLD ), bg = "#3a8ff8", fg = "#666a88", padx= 60)
        text_temperatura.pack(side = "left")
        temperatura = tk.Label(frame_form_top, text = "20°C", font = ('Times', 15, BOLD ), bg = "#3a8ff8", fg = "#666a88", padx= 0 )
        temperatura.pack(side = "left")

        

        self.ventana.mainloop()
