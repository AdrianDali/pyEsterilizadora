from tkinter import*
from tkinter import messagebox
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfilename, askopenfilenames
from tkinter.simpledialog import askfloat, askinteger, askstring

class Ventana(Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.geometry("400x400")
        self.resizable(0,0)
        self.widgest()
        self.lista=[1,2,3,4]
    def salir(self):
        valor=messagebox.askquestion(title="SALIR",message="¿Esta seguro que desea salir?")
        if valor=="yes":
            self.destroy()
    def advertencia(self):
        print(self.lista)
        messagebox.showwarning(title="ADVERTENCIA",message=f"Se eliminara el numero {self.lista[2]}")
        del self.lista[2]
        print(self.lista)
    def informacion(self):
        while True:
            try:
                num=int(input("Ingrese un numero: "))
                if num<0:
                    messagebox.showinfo(title="INFORMACION",message="Ingrese un numero mayor a cero")
                else:
                    break
            except:
                messagebox.showinfo(title="INFORMACION",message="Ingrese digitos")
        print(num+5)
    def color(self):
        valor=askcolor()
        print(valor)
    def archivos(self):
        #valor=askopenfilename()
        valor=askopenfilenames()
        print(valor)
    def okcancel(self):
        valor=messagebox.askokcancel(title="OPCIONES",message="¿DESEA CONTINUAR?")
        if valor==True:
            print(sum(self.lista))
        else:
            print(self.lista)
    def numeros(self):
        #valor=askfloat(title="VALOR",prompt="Ingrese un numero")
        valor= askstring(title="VALOR",prompt="Ingrese un numero")
        #if valor==None:
        #    print(self.lista)
        #else:
        #    self.lista=[i*valor for i in self.lista]
        #    print(self.lista)
        print(valor)
    
    def widgest(self):
        btnquitar=Button(self,text="SALIR",command=self.salir)
        btnquitar.pack()
        btnadvertencia=Button(self,text="ADVERTENCIA",command=self.advertencia)
        btnadvertencia.pack()
        btninforamcion=Button(self,text="INFORAMCION",command=self.informacion)
        btninforamcion.pack()
        btncolores=Button(self,text="COLORES",command=self.color)
        btncolores.pack()
        btnarchivos=Button(self,text="ARCHIVOS",command=self.archivos)
        btnarchivos.pack()
        btnokcancel=Button(self,text="OKCANCEL",command=self.okcancel)
        btnokcancel.pack()
        btnnumeros=Button(self,text="NUMEROS",command=self.numeros)
        btnnumeros.pack()
app=Ventana()
app.mainloop()