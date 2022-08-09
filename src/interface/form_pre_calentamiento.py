from pydoc import text
import tkinter as tk
import matplotlib 

matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

from tkinter.font import BOLD
import utils.generic as utl
import time 
import numpy as np

class PreCalentamiento:
    def times(self): 
        current_time = time.strftime("%H:%M:%S")
        self.clock.config(text = current_time)
        self.date.config(text = time.strftime("%d/%m/%Y"))
        self.clock.after(200, self.times)

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Pre Calentamiento")
        #el ancho y alto de la ventana
        #w,h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        #formateo de tuplas
        self.ventana.geometry("%dx%d+0+0" % (1200, 800))
        self.ventana.config(bg= "#ffffff")
        self.ventana.resizable(width = 0, height= 0)

        

        #header
        #------------------------------------------------------
        frame_form_top = tk.Frame(self.ventana,height=50, bd = 0,padx= 10, relief=tk.SOLID, bg = "#ffffff")
        frame_form_top.pack (side = "top", fill= tk.X)
        title = tk.Label(frame_form_top, text = "Sterilization System", font = ('Times', 30 ), bg = "#ffffff", fg = "#000000", pady = 0)
        title.pack(side = "left")

        self.date =tk.Label(frame_form_top, font=('Times',15,BOLD)  ,bg = "#fcfcfc", fg = "#666a88", padx = 25)
        self.date.pack(side = "right")

        self.clock = tk.Label(frame_form_top, font = ('Times', 15, BOLD ), bg = "#6a9ff6", fg = "black", padx = 25, pady=20)
        self.clock.pack(side = "right" )
        self.times()

        text_temperatura = tk.Label(frame_form_top, text = "Temperatura: ", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000")
        text_temperatura.pack(side = "left", padx=80)

        temperatura = tk.Label(frame_form_top, text = "20°C", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000", padx= 0 )
        temperatura.pack(side = "left")
        #TERMINA HEADER
        #----------------------------------------------------------------------------------------------------------------------
        frame_top = tk.Frame(self.ventana, bd= 0 ,height=70, relief= tk.SOLID, bg = "#6a9ff6")
        frame_top.pack(side= "top" , fill = tk.X)
        text_top = tk.Label(frame_top, text = "Pre Head", font = ('Times', 30 ), bg = "red", fg = "#666a88", pady = 0)
        text_top.pack(side = "top" )

        
        #----------------------------------------------------------------------------------------------------------------------
        frame_bottom = tk.Frame(self.ventana, bd= 0 ,relief= tk.SOLID, bg = "#6a9746")
        frame_bottom.pack(side= "top" ,expand= tk.YES,  fill = tk.BOTH)

        frame_monitoreo =  tk.Frame(frame_bottom, bd= 0, height = 300 ,relief= tk.SOLID, bg = "#9a9ff6")
        frame_monitoreo.pack(side= "top" , expand=tk.YES ,  fill = tk.BOTH, padx= 10, pady= 10)

        frame_graficas = tk.Frame(frame_bottom, bd= 0 ,height=300, relief= tk.SOLID, bg = "#1a5ff6")
        frame_graficas.pack(side= "top" , expand = tk.YES ,fill = tk.BOTH ,pady= 10 , padx= 10)

        #----------------------------------------------------------------------------------------------------------------------
        frame_01 = tk.Frame(frame_monitoreo, bd= 0 ,width= 250,  height = 250  ,relief= tk.SOLID, bg = "#4a9ff6")
        frame_01.pack(side= "left",  expand = tk.TRUE , fill = tk.BOTH, padx= 10, pady= 10)
        frame_01.columnconfigure(0, weight=1)
        frame_01.columnconfigure(1, weight=3)
        text_01 = tk.Label(frame_01, text = "Chamber Conditions", font = ('Times', 20 ), bg = "#ffffff", fg = "#000000")
        text_01.grid(row=0, column=0,padx=15,pady=15, sticky=tk.EW )
        text_02 = tk.Label(frame_01, text = "Press: ", font = ('Times', 15 ), bg = "#ffffff", fg = "#000000")
        text_02.grid(row=1, column=0,padx=15,pady=15 , sticky=tk.W )
        text_03 = tk.Label(frame_01, text = "20 KPA", font = ('Times', 15 ), bg = "#ffffff", fg = "#000000")
        text_03.grid(row=1, column=0,padx=15, )
        text_04 = tk.Label(frame_01, text = "2.6 INHGA", font = ('Times', 15 ), bg = "#ffffff", fg = "#000000")
        text_04.grid(row=2, column=0,padx=15,pady=15  )
        text_05 = tk.Label(frame_01, text = "Temp: ", font = ('Times', 15 ), bg = "#ffffff", fg = "#000000")
        text_05.grid(row=3, column=0,padx=15,pady=15 , sticky=tk.W )
        text_06 = tk.Label(frame_01, text = "20°C",font = ('Times', 15 ), bg = "#ffffff", fg = "#000000")
        text_06.grid(row=3, column=0,padx=15,pady=15 ,  )
        #----------------------------------------------------------------------------------------------------------------------
        frame_02 = tk.Frame(frame_monitoreo, bd= 0 ,width= 250,  height = 250  ,relief= tk.SOLID, bg = "#6a2ff6")
        frame_02.pack(side= "left", padx= 15, pady= 10, expand = tk.TRUE , fill = tk.BOTH)
        frame_02.columnconfigure(0, weight=1)
        frame_02.columnconfigure(1, weight=3)
        





        frame_03 = tk.Frame(frame_monitoreo, bd= 0 ,width= 250,  height = 250  ,relief= tk.SOLID, bg = "#6a2ff6")
        frame_03.pack(side= "left", padx= 15, pady= 10, expand = tk.TRUE , fill = tk.BOTH)

        frame_04 = tk.Frame(frame_monitoreo, bd= 0 ,width= 250,  height = 250  ,relief= tk.SOLID, bg = "#6a2ff6")
        frame_04.pack(side= "left", padx= 15, pady= 10, expand = tk.TRUE , fill = tk.BOTH)

        f_grafica = tk.Frame(frame_graficas, bd= 0 ,width= 600,  height = 300  ,relief= tk.SOLID, bg = "#6a2ff6")
        f_grafica.pack(side= "left", padx= 10, pady= 10, expand = tk.TRUE , fill = tk.BOTH)
        fig = Figure(figsize=(8, 4), dpi=100)
        t = np.arange(0, 3, .01)
        fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

        canvas = FigureCanvasTkAgg(fig, f_grafica)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        toolbar = NavigationToolbar2Tk(canvas, f_grafica)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        frame_button = tk.Frame(frame_graficas, bd= 0 ,width= 70,  height = 70 ,relief= tk.SOLID, bg = "#6a5746")
        frame_button.pack(side= "left",expand= tk.TRUE , fill= tk.BOTH, padx= 10, pady= 10)

        button_manual = tk.Button(frame_button, text = "Manual", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000")
        #button_manual.place(x=0, y=0, relwidth=1, relheight=1)
        button_manual.pack(side = "top", fill= tk.X)
        button_graficas = tk.Button(frame_button, text = "Graficas", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000")
        button_graficas.pack(side = "top", fill= tk.X)
        #button_graficas.place(x=0, y=0, relwidth=1, relheight=1)
        button_inicio = tk.Button(frame_button, text = "Cycle Capture", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000")
        button_inicio.pack(side = "top", fill= tk.X)
        #button_inicio.place(x=0, y=0, relwidth=1, relheight=1)
        self.ventana.mainloop()