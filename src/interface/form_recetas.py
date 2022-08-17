import tkinter as tk
from tkinter import *
from tkinter.font import BOLD
import utils.generic as utl
import components.components as cmp
import time
from model.proceso import DBProceso


class RecetasMenu:

    

    def LabelsUnits(self, nombres, inicio):
        j = inicio
        for i in range(len(nombres)):
            tk.Label(self.second_frame, text=nombres[i], font=('Times', 15, BOLD), bg="#ffffff",
                     fg="#000000").grid(row=int(j), column=2, sticky=tk.E)
            j = j + 1
            print(j)

    def Labels(self, nombres, inicio, numeracion):
        j = inicio
        n = numeracion

        for i in range(len(nombres)):
            print("entro ")
            tk.Label(self.second_frame, text=str(n), font=('Times', 15, BOLD), bg="#ffffff", fg="#000000").grid(row=int(j),
                                                                                                                column=0, sticky=tk.W)
            tk.Label(self.second_frame, text=nombres[i], font=('Times', 15, BOLD), bg="#ffffff", fg="#000000").grid(row=int(j),
                                                                                                                    column=1, sticky=tk.W, pady=5, padx=10)
            j = j + 1
            n = n + 1
            print(j)

    def times(self):
        current_time = time.strftime("%H:%M:%S")
        self.clock.config(text=current_time)
        self.date.config(text=time.strftime("%d/%m/%Y"))
        self.clock.after(200, self.times)

    def __init__(self):
        root = Tk()
        root.title("Pre Calentamiento")
        root.geometry("1200x800")

        # header
        # ------------------------------------------------------
        frame_form_top = tk.Frame(
            root, height=50, bd=0, padx=10, relief=tk.SOLID, bg="#ffffff")
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="Sterilization System", font=(
            'Times', 30), bg="#ffffff", fg="#000000", pady=0)
        title.pack(side="left")

        self.date = tk.Label(frame_form_top, font=(
            'Times', 15, BOLD), bg="#ffffff", fg="#666a88", padx=25)
        self.date.pack(side="right")

        self.clock = tk.Label(frame_form_top, font=(
            'Times', 15, BOLD), bg="#ffffff", fg="black", padx=25, pady=20)
        self.clock.pack(side="right")
        self.times()

        text_temperatura = tk.Label(frame_form_top, text="Temperatura: ", font=(
            'Times', 15, BOLD), bg="#ffffff", fg="#000000")
        text_temperatura.pack(side="left", padx=80)

        temperatura = tk.Label(frame_form_top, text="20°C", font=(
            'Times', 15, BOLD), bg="#ffffff", fg="#000000", padx=0)
        temperatura.pack(side="left")
        # TERMINA HEADER
        # ----------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------

        # FRAME PARA LISTA Y BOTONES DE RECETAS
        frame_left = tk.Frame(root, bd=0, relief=tk.SOLID,
                              width=40, padx=10, pady=10, bg="#ffffff")
        frame_left.pack(side="left", expand=tk.NO, fill=tk.BOTH)
        lista = tk.Listbox(frame_left, height=10, bd=0, relief=tk.SOLID,
                           bg="#fcfcfc", fg="#666a88", font=('Times', 15, BOLD))
        lista.pack(side="top", expand=tk.NO, fill=tk.X)
        lista.insert(tk.END, "Receta 1")
        lista.insert(tk.END, "Receta 2")
        boton_crear = tk.Button(frame_left, text="Crear", font=(
            'Times', 15, BOLD), bg="green", bd=0, fg="#fff")
        boton_crear.pack(side="top", expand=tk.NO, fill=tk.X)

        boton_editar = tk.Button(frame_left, text="Editar", font=(
            'Times', 15, BOLD), bg="white", bd=0, fg="#fff")
        boton_editar.pack(side="top", expand=tk.NO, fill=tk.X)

        boton_eliminar = tk.Button(frame_left, text="Eliminar", font=(
            'Times', 15, BOLD), bg="red", bd=0, fg="#fff")
        boton_eliminar.pack(side="top", expand=tk.NO, fill=tk.X)

        # main frame
        main_frame = Frame(root, bg="#ffffff")
        main_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)
        # canvas
        canvas = Canvas(main_frame, bg="#ffffff")
        canvas.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

        # scroll bar to canvas
        scroll_bar = Scrollbar(main_frame, orient=VERTICAL,
                               command=canvas.yview, bg="#ffffff")
        scroll_bar.pack(side=RIGHT, fill=Y)
        # configure the canvas
        canvas.configure(yscrollcommand=scroll_bar.set)

        canvas.bind('<Configure>', lambda e: canvas.configure(
            scrollregion=canvas.bbox('all')))
        # create another frame inside the canvas
        self.second_frame = Frame(canvas, bg="#ffffff")
        self.second_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # add thet new frame to a window in the canvas
        canvas.create_window((0, 0), window=self.second_frame, anchor='nw')

        # for thing in range(100):
        #    Button(self.second_frame, text=thing, width=10).grid(row=thing, column=0)

        # labe = Label(self.second_frame, text="Pre Calentamiento", font=('Times', 30 ), bg = "#ffffff", fg = "#000000")
        #labe.grid(row=3, column=2)
        # labe2 = Label(self.second_frame, text="Pre Calentamiento", font=('Times', 30 ), bg = "#ffffff", fg = "#000000")
        #labe2.grid(row=3, column=3)
        self.second_frame.columnconfigure(0, weight=1)
        self.second_frame.rowconfigure(200, weight=15)

        text11 = tk.Label(self.second_frame, text="VACUUM", font=(
            'Times', 15, BOLD), bg="#ffffff", fg="#000000")
        text11.grid(row=0, column=2, sticky=tk.W)
        # text12 = tk.Label(self.second_frame, text = "1", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000")
        #text12.grid(row = 1, column = 0, sticky = tk.W)
        self.Labels(["Evacuation Pressure: ", "Anti-cavitation Pressure: ", "Gas Interlock Pressure: ", "Pressure Increment: ",
                     "Time Increment: ", "Fast Increment Tolerance: ", "Slow Increment Termination Pressure: ", "Print Interval: "], 1, 16)

        

        # text12 = tk.Label(self.second_frame, text = "F", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000")
        #text12.grid(row = 1, column = 2, sticky = tk.E)
        self.LabelsUnits(["INHGA", "INHGA", "INHGA", "INHG",
                         "MM:SS", "INHG", "INHGA", "MM:SS"], 1)

        text9 = tk.Label(self.second_frame, text="LEAK TEST ", font=(
            'Times', 15, BOLD), bg="#ffffff", fg="#000000")
        text9.grid(row=9, column=2, sticky=tk.W, pady=5, padx=10)

        self.Labels(["Leak Test Time", "Leak Test Tolerance",
                    "Print Interval"], 10, 25)
        self.LabelsUnits(["HH:MM", "INHG", "MM:SS"], 10)

        text13 = tk.Label(self.second_frame, text="INERT DILUTION", font=(
            'Times', 15, BOLD), bg="#ffffff", fg="#000000")
        text13.grid(row=13, column=2, pady=5, padx=10)

        self.Labels(["# Of Dilution Cycles", "Inert Gas Pressure", "Inert Pressure Increment", "Inert Time Increment", "Inert Fast Increment Tolerance",
                     "Evacuation Pressure", "Vacuum Pressure Increment", "Vacuum Time Increment", "Vacuum Fast Inc Tolerance", "Vacuum Slow Inc Termination Pressure",
                     "Anti-cavitation pressure", "Hi Pressure", "Print Interval"], 14, 29)
        self.LabelsUnits(["", "INHGA", "INHG", "MM:SS", "INHG", "INHGA",
                         "INHG", "MM:SS", "INHG", "INHGA", "INHGA", "INHGA", "MM:SS"], 14)

        text9 = tk.Label(self.second_frame, text="HUMIDIFICATION ", font=(
            'Times', 15, BOLD), bg="#ffffff", fg="#000000")
        text9.grid(row=27, column=2, sticky=tk.W, pady=5, padx=10)

        self.Labels(["Type", "Pressure Rise", "Pressure Increment", "Time Increment", "Fast Increment Tolerance",
                     "Maximum Time", "Print Interval"],  28, 47)
        self.LabelsUnits(["", "INHG", "INHG", "MM:SS",
                         "INHG", "HH:MM", "MM:SS"], 28)

        text27 = tk.Label(self.second_frame, text="HUMIDITY DWELL ", font=(
            'Times', 15, BOLD), bg="#ffffff", fg="#000000")
        text27.grid(row=35, column=2, sticky=tk.W, pady=5, padx=10)

        self.Labels(["Type", "Control Pressure", "Control Differential", "Hi Humidity",
                    "Lo Humidity", "Maximum Humidity", "Dwell Time", "Print Interval"], 36, 71)
        self.LabelsUnits(["", "INHGA", "INHG", "INHGA",
                         "INHGA", "INHGA", "HH:MM", "MM:SS"], 36)

        text36 = tk.Label(self.second_frame, text="GAS", font=(
            'Times', 15, BOLD), bg="#ffffff", fg="#000000")
        text36.grid(row=44, column=2, sticky=tk.W, pady=5, padx=10)

        self.Labels(["Gas Pressure", "Pressure Increment", "Time Increment",
                    "Fast Increment Tolerance", "Print Interval", "Gas by Weight"], 45, 87)
        self.LabelsUnits(
            ["INHGA", "INHG", "MM:SS", "INHG", "MM:SS", "LBS"], 45)

        text43 = tk.Label(self.second_frame, text="GAS DWELL", font=(
            'Times', 15, BOLD), bg="#ffffff", fg="#000000")
        text43.grid(row=51, column=2, sticky=tk.W, pady=5, padx=10)

        self.Labels(["Control Pressure", "Control Differential", "Dwell Time", "Maximum # Makeups", "Long Exposure", "Short Exposure",
                     "Hi Pressure", "Lo Pressure", "Hi Pressure Abort", "Emission Control Lead Time", "Print Interval"], 52, 94)
        self.LabelsUnits(["INHGA", "INHG", "HH:MM", "", "HH:MM",
                         "HH:MM", "INHGA", "INHGA", "INHGA", "HH:MM", "MM:SS"], 52)

        text55 = tk.Label(self.second_frame, text="AFTER VACUUM", font=(
            'Times', 15, BOLD), bg="#ffffff", fg="#000000")
        text55.grid(row=63, column=2, sticky=tk.W, pady=5, padx=10)

        self.Labels(["Evacuation Pressure", "Anti-cavitation Pressure", "Air Interlock Pressure", "Pressure Increment", "Time Increment",
                     "Fast Increment Tolerance", "Slow Increment Termination Pressure", "Vacumm Hold Time", "Print Interval"], 64, 107)

        self.LabelsUnits(["INHGA", "INHGA", "INHGA", "INHG",
                         "MM:SS", "INHG", "INHGA", "HH:MM", "MM:SS"], 64)

        text65 = tk.Label(self.second_frame, text="GAS WASH A ", font=(
            'Times', 15, BOLD), bg="#ffffff", fg="#000000")
        text65.grid(row=74, column=2, sticky=tk.W, pady=5, padx=10)

        self.Labels(["#Of Wash Cycles", "Release Type", "Release Pressure", "Evacuation Pressure", "Anti-cavitation Pressure", "Hi pressure",
                     "Release Pressure Increment", "Release Time Increment", "Release Fast Inc Tolerance", "Release Slow Increment Termination Pressure", "Release Hold Time",
                     "Vacuum Pressure Increment", "Vacuum Time Increment", "Vacuum Fast Inc Tolerance", "Vacuum Slow Increment Termination Pressure", "Vacuum Hold Time", "Print Interval"
                     ], 75, 117)

        self.LabelsUnits(["", "", "INHGA", "INHGA", "INHGA", "INHGA", "INHG", "MM:SS",
                         "INHG", "INHGA", "HH:MM", "INHG", "MM:SS", "INHG", "INHGA", "HH:MM", "MM:SS"], 75)

        text66 = tk.Label(self.second_frame, text="GAS WASH B ", font=(
            'Times', 15, BOLD), bg="#ffffff", fg="#000000")
        text66.grid(row=93, column=2, sticky=tk.W, pady=5, padx=10)
        self.Labels(["#Of Wash Cycles", "Release Type", "Release Pressure", "Evacuation Pressure", "Anti-cavitation Pressure", "Hi pressure",
                     "Release Pressure Increment", "Release Time Increment", "Release Fast Inc Tolerance", "Release Slow Increment Termination Pressure", "Release Hold Time",
                     "Vacuum Pressure Increment", "Vacuum Time Increment", "Vacuum Fast Inc Tolerance", "Vacuum Slow Increment Termination Pressure", "Vacuum Hold Time", "Print Interval"
                     ], 94, 134)

        self.LabelsUnits(["", "", "INHGA", "INHGA", "INHGA", "INHGA", "INHG", "MM:SS",
                         "INHG", "INHGA", "HH:MM", "INHG", "MM:SS", "INHG", "INHGA", "HH:MM", "MM:SS"], 94)

        text67 = tk.Label(self.second_frame, text="RELEASE", font=(
            'Times', 15, BOLD), bg="#ffffff", fg="#000000")
        text67.grid(row=111, column=2, sticky=tk.W, pady=5, padx=10)

        self.Labels(["Relsease Pressure", "Pressure Increment", "Time Increment", "Fast Increment Tolerance",
                     "Slow Increment Termination Pressure", "Print Interval"], 112, 169)

        self.LabelsUnits(
            ["INHGA", "INHG", "MM:SS", "INHG", "INHGA", "MM:SS"], 112)

        con = DBProceso()
        ren = con.select_proceso()
        print(ren)
        # print(DBProceso.select_proceso)
        
        valor16 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor16.insert(0, ren[0])
        valor16.grid(row=1, column=2, padx=100)

        valor17 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor17.insert(0, ren[1])
        valor17.grid(row=2, column=2, padx=100)

        valor18 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000")
        valor18.insert(0, ren[2])
        valor18.grid(row=3, column=2, padx=100)

        valor19 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor19.insert(0, ren[3])
        valor19.grid(row=4, column=2, padx=100)

        valor20 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor20.insert(0, ren[4])
        valor20.grid(row=5 ,column=2, padx=100)

        valor21 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor21.insert(0, ren[5])
        valor21.grid(row=6, column=2, padx=100)

        valor22 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor22.insert(0, ren[6])
        valor22.grid(row=7, column=2, padx=100)

        valor23 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor23.insert(0, ren[7])
        valor23.grid(row=8, column=2, padx=100)

        valor25 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor25.insert(0, ren[8])
        valor25.grid(row=10, column=2, padx=100)
        
        valor26 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor26.insert(0, ren[9])
        valor26.grid(row=11, column=2, padx=100)

        valor27 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor27.insert(0, ren[10])
        valor27.grid(row=12, column=2, padx=100)

        valor29 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor29.insert(0, ren[11])
        valor29.grid(row=14, column=2, padx=100)

        valor30 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor30.insert(0, ren[12])
        valor30.grid(row=15, column=2, padx=100)

        valor31 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor31.insert(0, ren[13])
        valor31.grid(row=16, column=2, padx=100)

        valor32 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor32.insert(0, ren[14])
        valor32.grid(row=17, column=2, padx=100)

        valor33 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor33.insert(0, ren[15])
        valor33.grid(row=18, column=2, padx=100)

        valor34 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor34.insert(0, ren[16])
        valor34.grid(row=19, column=2, padx=100)

        valor35 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor35.insert(0, ren[17])
        valor35.grid(row=20, column=2, padx=100)

        valor36 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor36.insert(0, ren[18])
        valor36.grid(row=21, column=2, padx=100)

        valor37 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor37.insert(0, ren[19])
        valor37.grid(row=22, column=2, padx=100)

        valor38 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor38.insert(0, ren[20])
        valor38.grid(row=23, column=2, padx=100)

        valor39 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor39.insert(0, ren[21])
        valor39.grid(row=24, column=2, padx=100)

        
        valor40 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor40.insert(0, '0')
        valor40.grid(row=25, column=2, padx=100)

  

        valor41 = tk.Entry(self.second_frame, width=20,bg="#ff8fff", fg="#000000") 
        valor41.insert(0, ren[23])
        valor41.grid(row=26, column=2, padx=100)


        valor47 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor47.insert(0, ren[24])
        valor47.grid(row=28, column=2, padx=100)

        valor48 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor48.insert(0, ren[25])
        valor48.grid(row=29, column=2, padx=100)

        valor49 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor49.insert(0, ren[26])
        valor49.grid(row=30, column=2, padx=100)

        valor50 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor50.insert(0, ren[27])
        valor50.grid(row=31, column=2, padx=100)

        valor51 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor51.insert(0, ren[28])
        valor51.grid(row=32, column=2, padx=100)

        valor52 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor52.insert(0, ren[29])
        valor52.grid(row=33, column=2, padx=100)

        valor53 = tk.Entry(self.second_frame, width=20,bg="#3fffff", fg="#000000") 
        valor53.insert(0, ren[30])
        valor53.grid(row=34, column=2, padx=100)

        valor71 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor71.insert(0, ren[31])
        valor71.grid(row=36, column=2, padx=100)

        valor72 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor72.insert(0, ren[32])
        valor72.grid(row=37, column=2, padx=100)

        valor73 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor73.insert(0, ren[33])
        valor73.grid(row=38, column=2, padx=100)

        valor74 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor74.insert(0, ren[34])
        valor74.grid(row=39, column=2, padx=100)

        valor75 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor75.insert(0,  ren[35])
        valor75.grid(row=40, column=2, padx=100)

        valor76 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor76.insert(0, ren[36])
        valor76.grid(row=41, column=2, padx=100)

        valor77 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor77.insert(0, ren[37])
        valor77.grid(row=42, column=2, padx=100)

        valor78 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor78.insert(0, ren[38])
        valor78.grid(row=43, column=2, padx=100)

        valor87 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor87.insert(0, ren[39])
        valor87.grid(row=45, column=2, padx=100)

        valor88 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor88.insert(0, ren[40])
        valor88.grid(row=46, column=2, padx=100)

        valor89 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor89.insert(0, ren[41])
        valor89.grid(row=47, column=2, padx=100)

        valor90 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor90.insert(0,  ren[42])
        valor90.grid(row=48, column=2, padx=100)

        valor91 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor91.insert(0, ren[43])
        valor91.grid(row=49, column=2, padx=100)

        valor92 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor92.insert(0, ren[44])
        valor92.grid(row=50, column=2, padx=100)

        valor92 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor92.insert(0, ren[44])
        valor92.grid(row=50, column=2, padx=100)

        valor92 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor92.insert(0, ren[44])
        valor92.grid(row=50, column=2, padx=100)

        valor92 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor92.insert(0, ren[44])
        valor92.grid(row=50, column=2, padx=100)

        valor92 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor92.insert(0, ren[44])
        valor92.grid(row=50, column=2, padx=100)

        valor92 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor92.insert(0, ren[44])
        valor92.grid(row=50, column=2, padx=100)

        valor92 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor92.insert(0, ren[44])
        valor92.grid(row=50, column=2, padx=100)

        valor92 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor92.insert(0, ren[44])
        valor92.grid(row=50, column=2, padx=100)

        valor92 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor92.insert(0, ren[44])
        valor92.grid(row=50, column=2, padx=100)

        valor92 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor92.insert(0, ren[44])
        valor92.grid(row=50, column=2, padx=100)

        valor92 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor92.insert(0, ren[44])
        valor92.grid(row=50, column=2, padx=100)

        valor92 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor92.insert(0, ren[44])
        valor92.grid(row=50, column=2, padx=100)

        valor92 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor92.insert(0, ren[44])
        valor92.grid(row=50, column=2, padx=100)

        valor92 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor92.insert(0, ren[44])
        valor92.grid(row=50, column=2, padx=100)

        valor92 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor92.insert(0, ren[44])
        valor92.grid(row=50, column=2, padx=100)

        valor92 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor92.insert(0, ren[44])
        valor92.grid(row=50, column=2, padx=100)

        valor92 = tk.Entry(self.second_frame, width=20,bg="#ffffff", fg="#000000") 
        valor92.insert(0, ren[44])
        valor92.grid(row=50, column=2, padx=100)








        

        



        




    


        
        
        root.mainloop()
