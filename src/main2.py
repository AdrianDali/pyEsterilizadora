from ast import Lambda
from tkinter import *
from tkinter import ttk 

root = Tk() 
root.title("Pre Calentamiento")
root.geometry("1200x800")

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

for thing in range(100):
    Button(second_frame, text=thing, width=10).grid(row=thing, column=0)

labe = Label(second_frame, text="Pre Calentamiento", font=('Times', 30 ), bg = "#ffffff", fg = "#000000")
labe.grid(row=3, column=2)
labe2 = Label(second_frame, text="Pre Calentamiento", font=('Times', 30 ), bg = "#ffffff", fg = "#000000")
labe2.grid(row=3, column=3)
root.mainloop()
#    win = Tk()

#    wrapper1 = LabelFrame(win, bg="red", text="Wrapper 1")
#    wrapper2 = LabelFrame(win, bg="green", text="Wrapper 2")

#    mycanvas = Canvas(wrapper1,  bg="yellow")
#    mycanvas.pack(side=LEFT)

#    yscrollbar = ttk.Scrollbar(wrapper1, orient="vertical", command= mycanvas.yview)
#    yscrollbar.pack(side=RIGHT, fill="y")
#    mycanvas.configure(yscrollcommand=yscrollbar.set)

#    mycanvas.bind('<Configure>', lambda e:mycanvas.configure( scrollregion = mycanvas.bbox('all')))

#    myframe = Frame(mycanvas, bg="blue")
#    myframe.pack(fill=BOTH, expand=True)
#    mycanvas.create_window((0,0), window=myframe, anchor="nw")

#   wrapper1.pack(fill='both', expand=True, padx=10, pady=5)
#    wrapper2.pack(fill='both', expand=True, padx=10, pady=5)

#    for i in range(50):
#        Button(myframe, text = "my button " + str(i), width=10).pack()

    #Label(mycanvas, text="This is a label").pack()

#    win.geometry("500x500")
#    win.resizable(False, False)
#    win.title("My first GUI")

#    win.mainloop()
