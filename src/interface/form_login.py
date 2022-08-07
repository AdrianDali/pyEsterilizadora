import tkinter as tk 
from tkinter import ttk, messagebox
from tkinter.font import BOLD 
import utils.generic as utl 
from interface.form_master import MasterPanel

class App: 
    def verificar(self): 
        usu = self.usuario.get()
        pas = self.password.get()
        if(usu == "admin" and pas == "admin"):
            self.ventana.destroy()
            MasterPanel()
            
        else:
            messagebox.showerror(message = "La contrasena es incorrecta", title = "messsage")

    def __init__(self): 
        self.ventana = tk.Tk() 
        self.ventana.title("Inicio de sesion")
        self.ventana.geometry("800x500")
        self.ventana.config(bg= "#ffffff")
        self.ventana.resizable(width = 0, height= 0)
        utl.centrar_ventana(self.ventana, 800, 500)
        

        logo = utl.leer_imagen("images/descarga.jpg", (200,200))  

        #frame para el logo
        frame_logo = tk.Frame(self.ventana, bd = 0 , width = 300 , relief= tk.SOLID , padx=10, pady=10, bg = "#ffffff")
        frame_logo.pack (side = "left", expand = tk.NO, fill = tk.BOTH)
        label = tk.Label(frame_logo, image=logo, bg= "#ffffff")
        label.place(x=0, y=0, relwidth=1, relheight=1)

        #panel que estara a la derecha 
        frame_form = tk.Frame(self.ventana, bd = 0 , relief=tk.SOLID, bg = "#ffffff")
        frame_form.pack (side = "right", expand = tk.YES, fill = tk.BOTH)

        frame_form_top = tk.Frame(frame_form,height=50, bd = 0, relief=tk.SOLID, bg = "black")
        #que se expanda en x
        frame_form_top.pack (side = "top", fill= tk.X)
        #titulo 
        title = tk.Label(frame_form_top , text = "Inicio de sesion", font = ('Times', 30 ), bg = "#ffffff", fg = "#000000", pady = 50)
        #que se expanda 
        title.pack(expand= tk.YES, fill = tk.BOTH)

        #frame de relleno para el formulareio 
        frame_from_fill = tk.Frame(frame_form,height  = 50 , bd = 0 , relief = tk.SOLID , bg = "#ffffff")
        frame_from_fill.pack(side= "bottom", expand = tk.YES, fill = tk.BOTH)
       
        etiqueta_usuario = tk.Label(frame_from_fill, text = "Usuario", font = ('Times', 14 ), bg = "#ffffff", fg = "#000000", anchor = "w" )
        etiqueta_usuario.pack(fill= tk.X ,padx =20 , pady = 5)
        self.usuario = ttk.Entry(frame_from_fill, font=('Times', 14 ))
        self.usuario.pack(fill= tk.X ,padx =20 , pady = 10)

        etiqueta_password = tk.Label(frame_from_fill, text = "Contrasena", font = ('Times', 14 ), bg = "#ffffff", fg = "#000000", anchor = "w" )
        etiqueta_password.pack(fill= tk.X ,padx =20 , pady = 5)
        self.password = ttk.Entry(frame_from_fill, font=('Times', 14 ))
        self.password.pack(fill= tk.X ,padx =20 , pady = 10)
        #todo lo que escribimos se muestra con asterisco
        self.password.config(show="*")

        inicio = tk.Button(frame_from_fill, text = "Iniciar", font = ('Times', 15, BOLD ), bg = "#3a7ff6", bd = 0, fg = "#fff" , command = self.verificar)
        inicio.pack(fill= tk.X ,padx =20 , pady = 20)
        #inicio.bind("<Return>", self.verificar)
        self.ventana.mainloop()