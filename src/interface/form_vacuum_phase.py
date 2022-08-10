import tkinter as tk 
from tkinter.font import BOLD
import utils.generic as utl
import time

class VacuumPhase: 

    
    
    def times(self): 
        current_time = time.strftime("%H:%M:%S")
        self.clock.config(text = current_time)
        self.date.config(text = time.strftime("%d/%m/%Y"))
        self.clock.after(200, self.times)

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Proceso Esrterilizacion")
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
        text_top = tk.Label(frame_top, text = "Vacuum Phase", font = ('Times', 30 ), bg = "red", fg = "#666a88", pady = 0)
        text_top.pack(side = "top" )
        #----------------------------------------------------------------------------------------------------------------------
        frame_bottom = tk.Frame(self.ventana, bd= 0 ,relief= tk.SOLID, bg = "#6a9746")
        frame_bottom.pack(side= "top" ,expand= tk.YES,  fill = tk.BOTH)
        
        frame_graphic_process = tk.Frame(frame_bottom, bd= 0 ,relief= tk.SOLID, bg = "#6a9ff6")
        frame_graphic_process.pack(side= "top" ,expand= tk.YES,  fill = tk.BOTH , padx=10, pady=10)

        frame_phase_conditions = tk.Frame(frame_bottom, bd= 0 ,height= 250,relief= tk.SOLID, bg = "#1a6ff6")
        frame_phase_conditions.pack(side= "top" ,expand= tk.YES,  fill = tk.BOTH , padx=10, pady=10)
        
        frame_phase = tk.Frame(frame_graphic_process, bd= 0 ,relief= tk.SOLID, bg = "#768266")
        frame_phase.pack(side= "top" ,expand= tk.YES,  fill = tk.BOTH , padx=10, pady=10)

        canvas1 = tk.Canvas( frame_phase,width=300, height=300, bg = "#ffffff")
        canvas1.pack(side= "top" ,expand= tk.YES,  fill = tk.BOTH , padx=10, pady=10)
        canvas1.create_line(10,10,40,300,dash=(10,10), width= 4)
        canvas1.create_line(40,300,90,300,dash=(5,3), width= 4, fill = "red")
        canvas1.create_line(90,300,120,200,dash=(5,3), width= 4, fill = "red")
        canvas1.create_line(120,200,150,300,dash=(5,3), width= 4, fill = "red")
        canvas1.create_line(150,300,170,250,dash=(5,3), width= 4, fill = "red")
        canvas1.create_line(170,250, 220,250,dash=(5,3), width= 4, fill = "red")
        canvas1.create_line(220,250,260,100,dash=(5,3), width= 4, fill = "red")
        canvas1.create_line(260,100,550,100,dash=(5,3), width= 4, fill = "red")
        canvas1.create_line(550,100,590,300,dash=(5,3), width= 4, fill = "red")
        canvas1.create_line(590,300,630,300,dash=(5,3), width= 4, fill = "red")
        canvas1.create_line(630,300,670,50,dash=(5,3), width= 4, fill = "red")
        canvas1.create_line(670,50,710,50,dash=(5,3), width= 4, fill = "red")
        canvas1.create_line(710,50,750,300,dash=(5,3), width= 4, fill = "red")
        canvas1.create_line(750,300,790,300,dash=(5,3), width= 4, fill = "red")
        canvas1.create_line(790,300,830,50,dash=(5,3), width= 4, fill = "red")
        canvas1.create_line(830,50,870,50,dash=(5,3), width= 4, fill = "red")
        canvas1.create_line(870,50,910,300,dash=(5,3), width= 4, fill = "red")
        canvas1.create_line(910,300,950,300,dash=(5,3), width= 4, fill = "red")
        canvas1.create_line(950,300,990,50,dash=(5,3), width= 4, fill = "red")
        #----------------------------------------------------------------------------------------------------------------------

        frame_01 = tk.Frame(frame_phase_conditions, bd= 0 ,width= 250,  height = 250  ,relief= tk.SOLID, bg = "#4a9ff6")
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
        text_06 = tk.Label(frame_01, text = "20 °C",font = ('Times', 15 ), bg = "#ffffff", fg = "#000000")
        text_06.grid(row=3, column=0,padx=15,pady=15 ,  )
        #----------------------------------------------------------------------------------------------------------------------
        frame_02 = tk.Frame(frame_phase_conditions, bd= 0 ,width= 250,  height = 250  ,relief= tk.SOLID, bg = "#6a2ff6")
        frame_02.pack(side= "left", padx= 15, pady= 10, expand = tk.TRUE , fill = tk.BOTH)
        frame_02.columnconfigure(0, weight=1)
        frame_02.columnconfigure(1, weight=3)
        text_07 = tk.Label(frame_02, text = "Phase Especifications", font = ('Times', 20 ), bg = "#ffffff", fg = "#000000")
        text_07.grid(row=0, column=0,padx=15,pady=15, sticky=tk.EW )
        text_08 = tk.Label(frame_02, text = "Temp Setpoint: ", font = ('Times', 15 ), bg = "#ffffff", fg = "#000000")
        text_08.grid(row=1, column=0,padx=15,pady=15 , sticky=tk.W )
        text_09 = tk.Label(frame_02, text = "70 F", font = ('Times', 15 ), bg = "#ffffff", fg = "#000000")
        text_09.grid(row=1, column=0,padx=15,pady=15 , sticky=tk.E  ) 
        text_10 = tk.Label(frame_02, text = "Jacket Offset: ", font = ('Times', 15 ), bg = "#ffffff", fg = "#000000")
        text_10.grid(row=2, column=0,padx=15,pady=15 , sticky=tk.W )
        text_11 = tk.Label(frame_02, text = "0.5 F", font = ('Times', 15 ), bg = "#ffffff", fg = "#000000")
        text_11.grid(row=2, column=0,padx=15,pady=15 , sticky=tk.E  )
        text_12 = tk.Label(frame_02, text = "Jacket S.P: ", font = ('Times', 15 ), bg = "#ffffff", fg = "#000000")
        text_12.grid(row=3, column=0,padx=15,pady=15 , sticky=tk.W )
        text_13 = tk.Label(frame_02, text = "0.5 F", font = ('Times', 15 ), bg = "#ffffff", fg = "#000000")
        text_13.grid(row=3, column=0,padx=15,pady=15 , sticky=tk.E)
        #----------------------------------------------------------------------------------------------------------------------
        
        frame_03 = tk.Frame(frame_phase_conditions, bd= 0 ,width= 250,  height = 250  ,relief= tk.SOLID, bg = "#6a2ff6")
        frame_03.pack(side= "left", padx= 15, pady= 10, expand = tk.TRUE , fill = tk.BOTH)
        frame_03.columnconfigure(0, weight=1)
        frame_03.columnconfigure(1, weight=3)
        text_14 = tk.Label(frame_03, text = "Phase Status", font = ('Times', 20 ), bg = "#ffffff", fg = "#000000")
        text_14.grid(row=0, column=0,padx=15,pady=15, sticky=tk.EW )
        text_15 = tk.Label(frame_03, text = "AIR INBLEED ", font = ('Times', 15 ), bg = "#ffffff", fg = "#000000")
        text_15.grid(row=1, column=0,padx=15,pady=15 , sticky=tk.W )
        text_16 = tk.Label(frame_03, text = "Jacket Temp", font = ('Times', 15 ), bg = "#ffffff", fg = "#000000")
        text_16.grid(row=1, column=0,padx=15,pady=15 , sticky=tk.E  )
        text_17 = tk.Label(frame_03, text = " 88 F", font = ('Times', 15 ), bg = "#ffffff", fg = "#000000")
        text_17.grid(row=2, column=0,padx=15,pady=15 , sticky=tk.W )
        #----------------------------------------------------------------------------------------------------------------------
                
        frame_04 = tk.Frame(frame_phase_conditions, bd= 0 ,width= 250,  height = 250  ,relief= tk.SOLID, bg = "#6a2ff6")
        frame_04.pack(side= "left", padx= 15, pady= 10, expand = tk.TRUE , fill = tk.BOTH)



        self.ventana.mainloop()

