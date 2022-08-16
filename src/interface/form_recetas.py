import tkinter as tk 
from tkinter import *
from tkinter.font import BOLD 
import utils.generic as utl 
import components.components as cmp
import time

class RecetasMenu:

    #def LabelValues(self):
    #    j = inicio 
    #    for i in range(len(nombres)):
    #        tk.Label(self.second_frame, text = nombres[i], font = ('Times', 15, BOLD ), bg = "#ffffff",
    #         fg = "#000000").grid(row = int(j), column = 2, sticky = tk.E)
    #        j =  j + 1
    #        print(j)

    

    def LabelsUnits(self, nombres, inicio):
        j = inicio 
        for i in range(len(nombres)):
            tk.Label(self.second_frame, text = nombres[i], font = ('Times', 15, BOLD ), bg = "#ffffff",
             fg = "#000000").grid(row = int(j), column = 2, sticky = tk.E)
            j =  j + 1
            print(j)
        

    def Labels(self,nombres,inicio,numeracion):
        j = inicio 
        n = numeracion
      
        for i in range(len(nombres)):
            print("entro ")
            tk.Label(self.second_frame, text = str(n), font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000").grid(row = int(j),
             column = 0, sticky = tk.W)
            tk.Label(self.second_frame, text = nombres[i], font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000").grid(row = int(j),
            column = 1, sticky = tk.W, pady = 5 ,padx=10)
            j =  j + 1
            n = n + 1
            print(j)
            

    def times(self): 
        current_time = time.strftime("%H:%M:%S")
        self.clock.config(text = current_time)
        self.date.config(text = time.strftime("%d/%m/%Y"))
        self.clock.after(200, self.times)


    def __init__(self):
        root = Tk() 
        root.title("Pre Calentamiento")
        root.geometry("1200x800")

        
        #header
        #------------------------------------------------------
        frame_form_top = tk.Frame(root,height=50, bd = 0,padx= 10, relief=tk.SOLID, bg = "#ffffff")
        frame_form_top.pack (side = "top", fill= tk.X)
        title = tk.Label(frame_form_top, text = "Sterilization System", font = ('Times', 30 ), bg = "#ffffff", fg = "#000000", pady = 0)
        title.pack(side = "left")

        self.date =tk.Label(frame_form_top, font=('Times',15,BOLD)  ,bg = "#ffffff", fg = "#666a88", padx = 25)
        self.date.pack(side = "right")

        self.clock = tk.Label(frame_form_top, font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "black", padx = 25, pady=20)
        self.clock.pack(side = "right" )
        self.times()

        text_temperatura = tk.Label(frame_form_top, text = "Temperatura: ", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000")
        text_temperatura.pack(side = "left", padx=80)

        temperatura = tk.Label(frame_form_top, text = "20°C", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000", padx= 0 )
        temperatura.pack(side = "left")
        #TERMINA HEADER
        #----------------------------------------------------------------------------------------------------------------------
        #----------------------------------------------------------------------------------------------------------------------

        #FRAME PARA LISTA Y BOTONES DE RECETAS
        frame_left = tk.Frame(root, bd = 0 , relief= tk.SOLID, width= 40,padx=10, pady=10, bg = "#ffffff")
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
        
        
        
        
        #main frame
        main_frame = Frame(root,bg="#ffffff")
        main_frame.pack( fill=BOTH, expand=True, padx=10, pady=10)
        #canvas
        canvas = Canvas(main_frame,bg = "#ffffff")
        canvas.pack(side = LEFT ,fill=BOTH, expand=True, padx=10, pady=10)
       

        #scroll bar to canvas 
        scroll_bar = Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview, bg="#ffffff")
        scroll_bar.pack(side=RIGHT, fill=Y)
        #configure the canvas 
        canvas.configure(yscrollcommand=scroll_bar.set)

        canvas.bind('<Configure>', lambda e:canvas.configure( scrollregion = canvas.bbox('all')))
        #create another frame inside the canvas 
        self.second_frame = Frame(canvas, bg="#ffffff")
        self.second_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # add thet new frame to a window in the canvas
        canvas.create_window((0,0), window=self.second_frame, anchor='nw')

        #for thing in range(100):
        #    Button(self.second_frame, text=thing, width=10).grid(row=thing, column=0)

        #labe = Label(self.second_frame, text="Pre Calentamiento", font=('Times', 30 ), bg = "#ffffff", fg = "#000000")
        #labe.grid(row=3, column=2)
        #labe2 = Label(self.second_frame, text="Pre Calentamiento", font=('Times', 30 ), bg = "#ffffff", fg = "#000000")
        #labe2.grid(row=3, column=3)
        self.second_frame.columnconfigure(0, weight=1)
        self.second_frame.rowconfigure(200, weight=15)
        
        text11 = tk.Label(self.second_frame, text = "VACUUM", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000")
        text11.grid(row = 0, column = 2, sticky = tk.W)
        #text12 = tk.Label(self.second_frame, text = "1", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000")
        #text12.grid(row = 1, column = 0, sticky = tk.W)
        self.Labels(["Evacuation Pressure: ","Anti-cavitation Pressure: ","Gas Interlock Pressure: ","Pressure Increment: ",
        "Time Increment: ","Fast Increment Tolerance: ","Slow Increment Termination Pressure: ","Print Interval: "], 1,16)
       
       
        parametros01 = tk.Label(self.second_frame, text = "110", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000")
        parametros01.grid(row = 1, column = 2)

        



        #text12 = tk.Label(self.second_frame, text = "F", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000")
        #text12.grid(row = 1, column = 2, sticky = tk.E)
        self.LabelsUnits(["INHGA","INHGA","INHGA","INHG","MM:SS","INHG","INHGA","MM:SS"],1)

        text9 = tk.Label(self.second_frame, text = "LEAK TEST ", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000")
        text9.grid(row = 9, column = 2, sticky = tk.W, pady = 5 ,padx=10)


        self.Labels(["Leak Test Time", "Leak Test Tolerance", "Print Interval"], 10,25)
        self.LabelsUnits(["HH:MM","INHG","MM:SS"],10)

        text13 = tk.Label(self.second_frame, text = "INERT DILUTION", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000") 
        text13.grid(row = 13, column = 2, pady = 5 ,padx=10)


        self.Labels(["# Of Dilution Cycles", "Inert Gas Pressure", "Inert Pressure Increment", "Inert Time Increment", "Inert Fast Increment Tolerance",
         "Evacuation Pressure", "Vacuum Pressure Increment", "Vacuum Time Increment", "Vacuum Fast Inc Tolerance", "Vacuum Slow Inc Termination Pressure",
          "Anti-cavitation pressure", "Hi Pressure", "Print Interval"],14,29)
        self.LabelsUnits(["","INHGA","INHG","MM:SS","INHG","INHGA","INHG","MM:SS","INHG","INHGA","INHGA","INHGA","MM:SS"],14)

        text9 = tk.Label(self.second_frame, text = "HUMIDIFICATION ", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000")
        text9.grid(row = 27, column = 2, sticky = tk.W, pady = 5 ,padx=10)
      
        self.Labels(["Type", "Pressure Rise", "Pressure Increment", "Time Increment", "Fast Increment Tolerance",
         "Maximum Time", "Print Interval"],  28,47)
        self.LabelsUnits(["","INHG","INHG","MM:SS","INHG","HH:MM","MM:SS"],28)


        text27 = tk.Label(self.second_frame, text = "HUMIDITY DWELL ", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000")
        text27.grid(row = 35, column = 2, sticky = tk.W, pady = 5 ,padx=10)

        self.Labels(["Type","Control Pressure", "Control Differential", "Hi Humidity","Lo Humidity", "Maximum Humidity", "Dwell Time", "Print Interval"],36,71)
        self.LabelsUnits(["","INHGA","INHG","INHGA","INHGA","INHGA","HH:MM","MM:SS"],36)

        text36 = tk.Label(self.second_frame, text = "GAS", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000")
        text36.grid(row = 44, column = 2, sticky = tk.W, pady = 5 ,padx=10)
       
        self.Labels(["Gas Pressure","Pressure Increment","Time Increment","Fast Increment Tolerance","Print Interval","Gas by Weight"],45,87)
        self.LabelsUnits(["INHGA","INHG","MM:SS","INHG","MM:SS","LBS"],45)

        text43 = tk.Label(self.second_frame, text = "GAS DWELL", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000")
        text43.grid(row = 51, column = 2, sticky = tk.W, pady = 5 ,padx=10)
        

        self.Labels(["Control Pressure", "Control Differential", "Dwell Time", "Maximum # Makeups", "Long Exposure", "Short Exposure",
         "Hi Pressure", "Lo Pressure", "Hi Pressure Abort", "Emission Control Lead Time", "Print Interval"], 52,94)
        self.LabelsUnits(["INHGA","INHG","HH:MM","","HH:MM","HH:MM","INHGA","INHGA","INHGA","HH:MM","MM:SS"],52)

        text55 = tk.Label(self.second_frame, text = "AFTER VACUUM", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000")
        text55.grid(row = 63, column = 2, sticky = tk.W, pady = 5 ,padx=10)


        self.Labels(["Evacuation Pressure", "Anti-cavitation Pressure", "Air Interlock Pressure", "Pressure Increment", "Time Increment",
         "Fast Increment Tolerance", "Slow Increment Termination Pressure", "Vacumm Hold Time", "Print Interval"],64,107)

        self.LabelsUnits(["INHGA","INHGA","INHGA","INHG","MM:SS","INHG","INHGA","HH:MM","MM:SS"],64)


        text65 = tk.Label(self.second_frame, text = "GAS WASH A ", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000")
        text65.grid(row = 74, column = 2, sticky = tk.W, pady = 5 ,padx=10)

        self.Labels(["#Of Wash Cycles", "Release Type", "Release Pressure","Evacuation Pressure", "Anti-cavitation Pressure", "Hi pressure",
        "Release Pressure Increment", "Release Time Increment", "Release Fast Inc Tolerance", "Release Slow Increment Termination Pressure","Release Hold Time", 
        "Vacuum Pressure Increment", "Vacuum Time Increment", "Vacuum Fast Inc Tolerance", "Vacuum Slow Increment Termination Pressure", "Vacuum Hold Time", "Print Interval"
        ], 75,117)
        
        self.LabelsUnits(["","","INHGA","INHGA","INHGA","INHGA","INHG","MM:SS", "INHG", "INHGA","HH:MM","INHG","MM:SS","INHG","INHGA","HH:MM","MM:SS"],75)


        text66 = tk.Label(self.second_frame, text = "GAS WASH B ", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000")
        text66.grid(row = 93, column = 2, sticky = tk.W, pady = 5 ,padx=10)
        self.Labels(["#Of Wash Cycles", "Release Type", "Release Pressure","Evacuation Pressure", "Anti-cavitation Pressure", "Hi pressure",
        "Release Pressure Increment", "Release Time Increment", "Release Fast Inc Tolerance", "Release Slow Increment Termination Pressure","Release Hold Time", 
        "Vacuum Pressure Increment", "Vacuum Time Increment", "Vacuum Fast Inc Tolerance", "Vacuum Slow Increment Termination Pressure", "Vacuum Hold Time", "Print Interval"
        ], 94,134)

        self.LabelsUnits(["","","INHGA","INHGA","INHGA","INHGA","INHG","MM:SS", "INHG", "INHGA","HH:MM","INHG","MM:SS","INHG","INHGA","HH:MM","MM:SS"],94)


        text67 = tk.Label(self.second_frame, text = "RELEASE", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000")
        text67.grid(row = 111, column = 2, sticky = tk.W, pady = 5 ,padx=10)

        self.Labels(["Relsease Pressure", "Pressure Increment", "Time Increment", "Fast Increment Tolerance",
        "Slow Increment Termination Pressure", "Print Interval"],112,169)

        self.LabelsUnits(["INHGA","INHG","MM:SS","INHG","INHGA","MM:SS"],112)


        root.mainloop()
       



