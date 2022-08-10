import tkinter as tk 
from tkinter import *
from tkinter.font import BOLD 
import utils.generic as utl 
import components.components as cmp
import time

class RecetasMenu:

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
        #----------------------------------------------------------------------------------------------------------------------

        #FRAME PARA LISTA Y BOTONES DE RECETAS
        frame_left = tk.Frame(root, bd = 0 , relief= tk.SOLID, width= 40,padx=10, pady=10, bg = "#3a7ff6")
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
        main_frame = Frame(root,bg="red")
        main_frame.pack( fill=BOTH, expand=True, padx=10, pady=10)
        #canvas
        canvas = Canvas(main_frame,bg = "yellow")
        canvas.pack(side = LEFT ,fill=BOTH, expand=True, padx=10, pady=10)
       

        #scroll bar to canvas 
        scroll_bar = Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview, bg="green")
        scroll_bar.pack(side=RIGHT, fill=Y)
        #configure the canvas 
        canvas.configure(yscrollcommand=scroll_bar.set)

        canvas.bind('<Configure>', lambda e:canvas.configure( scrollregion = canvas.bbox('all')))
        #create another frame inside the canvas 
        second_frame = Frame(canvas, bg="blue")
        second_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # add thet new frame to a window in the canvas
        canvas.create_window((0,0), window=second_frame, anchor='nw')

        #for thing in range(100):
        #    Button(second_frame, text=thing, width=10).grid(row=thing, column=0)

        #labe = Label(second_frame, text="Pre Calentamiento", font=('Times', 30 ), bg = "#ffffff", fg = "#000000")
        #labe.grid(row=3, column=2)
        #labe2 = Label(second_frame, text="Pre Calentamiento", font=('Times', 30 ), bg = "#ffffff", fg = "#000000")
        #labe2.grid(row=3, column=3)
        second_frame.columnconfigure(0, weight=1)
        second_frame.rowconfigure(200, weight=15)
        text11 = tk.Label(second_frame, text = "VACUUM", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000")
        text11.grid(row = 0, column = 1, sticky = tk.W)
        text1 = tk.Label(second_frame, text = "Evacuation Pressure: ", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000")
        text1.grid(row = 1, column = 0, sticky = tk.W, pady = 5 ,padx=10)
        text2 = tk.Label(second_frame, text = "Anti-cavitation Pressure: ", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000")
        text2.grid(row = 2, column = 0, sticky = tk.W, pady = 5 ,padx=10)
        text3 = tk.Label(second_frame, text = "Gas Interlock Pressure: ", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000")
        text3.grid(row = 3, column = 0, sticky = tk.W, pady = 5 ,padx=10)
        text4 = tk.Label(second_frame, text = "Pressure Increment: ", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000")
        text4.grid(row = 4, column = 0, sticky = tk.W, pady = 5 ,padx=10)
        text5 = tk.Label(second_frame, text = "Time Increment: ", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000")
        text5.grid(row = 5, column = 0, sticky = tk.W, pady = 5 ,padx=10)
        text6 = tk.Label(second_frame, text = "Fast Increment Tolerance: ", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000")
        text6.grid(row = 6 , column = 0, sticky = tk.W, pady = 5 ,padx=10)
        text7 = tk.Label(second_frame, text = "Slow Increment Termination Pressure: ", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000")
        text7.grid(row = 7, column = 0, sticky = tk.W, pady = 5 ,padx=10)
        text8 = tk.Label(second_frame, text = "Print Interval: ", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000")
        text8.grid(row = 8, column = 0, sticky = tk.W, pady = 5 ,padx=10)
        text9 = tk.Label(second_frame, text = "LEAK TEST ", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000")
        text9.grid(row = 9, column = 1, sticky = tk.W, pady = 5 ,padx=10)
        text10 = tk.Label(second_frame, text = "Leak Test Time", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000")
        text10.grid(row = 10, column = 0, sticky = tk.W, pady = 5 ,padx=10)
        text111 = tk.Label(second_frame, text = "Leak Test Tolerance", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000")
        text111.grid(row = 11, column = 0, sticky = tk.W, pady = 5 ,padx=10)
        text12 = tk.Label(second_frame, text = "Print Interva", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000")
        text12.grid(row = 12, column = 0, sticky = tk.W, pady = 5 ,padx=10)
        text13 = tk.Label(second_frame, text = "Inert Dilution", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000") 
        text13.grid(row = 13, column = 0, pady = 5 ,padx=10)
        text14 = tk.Label(second_frame, text = "# Of Dilution Cycles", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000")
        text14.grid(row = 14, column = 0, sticky = tk.W, pady = 5 ,padx=10)
        text15 = tk.Label(second_frame, text = "Inert Gas Pressure", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000")
        text15.grid(row = 15, column = 0, sticky = tk.W, pady = 5 ,padx=10)
        text16 = tk.Label(second_frame, text = "Inert Pressure Increment", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000")
        text16.grid(row = 16, column = 0, sticky = tk.W, pady = 5 ,padx=10)
        text17 = tk.Label(second_frame, text = "Inert Time Increment", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000")
        text17.grid(row = 17, column = 0, sticky = tk.W, pady = 5 ,padx=10)
        text18 = tk.Label(second_frame, text = "Inert Fast Increment Tolerance", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000")
        text18.grid(row = 18, column = 0, sticky = tk.W, pady = 5 ,padx=10)
        text19 = tk.Label(second_frame, text = "Evacuation Pressure", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000")
        text19.grid(row = 19, column = 0, sticky = tk.W, pady = 5 ,padx=10)
        text20 = tk.Label(second_frame, text = "Vacuum Pressure Increment", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000")
        text20.grid(row = 20, column = 0, sticky = tk.W, pady = 5 ,padx=10)
        text21 = tk.Label(second_frame, text = "Vacuum Time Increment", font = ('Times', 15, BOLD ), bg = "#ffffff", fg = "#000000")
        text21.grid(row = 21, column = 0, sticky = tk.W, pady = 5 ,padx=10)

        root.mainloop()
       



