from tkinter import *
from tkinter import ttk
import time

root = Tk()
root.configure(background="white")
root.title("Barra de progresso")
root.geometry("500x400")
root.resizable(False, False)

def step():
    #MODO 1:
    #progresso1["value"]=10
    #MODO 2:
    #progresso1.start(40)
    #MODO 3:
    for x in range(10):
        barra_progresso['value']+=10
        root.update_idletasks()
        time.sleep(1)

def stop():
    barra_progresso.stop()

barra_progresso = ttk.Progressbar(root, orient = HORIZONTAL, length = 300, mode = "determinate") #ou indeterminate
barra_progresso.place(relx=0.2, rely=0.2)

bt_start = Button(root, text="START", bd=2, bg="#252525", fg="lightgreen", font=('Verdana',9,"bold"), command=step)
bt_start.place(relx=0.43, rely=0.3)

bt_stop =  Button(root, text="STOP", bd=2, bg="#252525", fg="red", font=('Verdana',9,"bold"), command=stop)
bt_stop.place(relx=0.433, rely=0.4)

root.mainloop()