#PLACAR DE FUTEBOL By Jvictor
from tkinter import *
from tkinter import ttk

root=Tk()

class Placar():
    def __init__(self):
        self.root=root
        self.tela()
        self.iniciar()
        self.frames_da_tela()
        self.labels()
        self.menu()
        root.mainloop()

    #FUNÇÃO PARA A TELA
    def tela(self):
        self.root.title("Placar de Futebol By Jvictor")
        self.root.configure(background="white")
        self.root.geometry("500x100")
        self.root.resizable(False, False)

        #CRONOMETRO
        global tempo, limitador, rodar, contador

        limitador=59
        tempo="00:00"
        rodar=False
        contador=0

    #FUNÇÃO PARA INICIAR
    def iniciar(self):
        global tempo, contador, limitador

        if rodar:
            if contador<=0:
                self.bt_tempo["font"] = "Ebrima 14 bold"

            else:
                self.bt_tempo["font"] = "Ebrima 14 bold"

                self.temporaria=str(tempo)
                self.min, self.seg=map(int, self.temporaria.split(":"))
                self.min=int(self.min)
                self.seg=int(contador)

                if (self.seg>=limitador):
                    contador=0
                    self.min+=1

                self.seg=str(0)+str(self.seg)
                self.min=str(0)+str(self.min)

                self.temporaria=str(self.min[-2:])+":"+str(self.seg[-2:])
                self.bt_tempo["text"]=self.temporaria

                tempo=self.temporaria

            self.bt_tempo.after(1000, self.iniciar)
            contador+=1

    #FUNÇÃO PARA INICIO
    def start(self):
        global rodar

        rodar=True
        self.iniciar()

    #FRAMES PARA SEPARAR JANELAS
    def frames_da_tela(self):
        self.frame1=Frame(self.root, bd=4, bg="#8B0000", highlightbackground="#FF0000", highlightthickness=2)
        self.frame1.place(relx=0.26 , rely=0.015, relwidth=0.46, relheight=0.48)

        self.frame2=Frame(self.root, bd=4, bg="#8B0000",highlightbackground="#FF0000", highlightthickness=2)
        self.frame2.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.46)

    #FUNÇÃO PARA AS LABELS
    def labels(self):
        #LABEL TITLE
        self.lb_titulo=Label(self.frame1, text="FINAL WORLD CUP 2022", bg="#8B0000", fg="white", font=('Ebrima',13,'bold'))
        self.lb_titulo.place(relx=0.04, rely=0.1)

        #LABEL PLACAR TIME 1
        self.lb_resultado1=Label(self.frame2,text="0", bg="white", fg="#8B0000", font=('Ebrima',18,'bold'))
        self.lb_resultado1.place(relx=0, rely=0, relwidth=0.1, relheight=1)

        #LABEL PLACAR TIME 2
        self.lb_resultado2=Label(self.frame2, text="0", bg="white", fg="#8B0000", font=('Ebrima',18,'bold'))
        self.lb_resultado2.place(relx=0.9, rely=0, relwidth=0.1, relheight=1)

        #LABEL CRONOMETRO
        self.bt_tempo=Button(self.frame2, text=tempo, bd=0, bg="white", fg="#8B0000", font=('Ebrima',14,'bold'), command=self.start)
        self.bt_tempo.place(relx=0.398, rely=0, relwidth=0.2, relheight=1)

        #LABEL TIME 1
        self.lb_time1=Label(self.frame2, text="BRASIL", bg="#8B0000", fg="white", font=('Ebrima',13,'bold'))
        self.lb_time1.place(relx=0.14, rely=0, relwidth=0.2, relheight=1)

        #LABEL TIME 2
        self.lb_time2=Label(self.frame2, text="FRANÇA", bg="#8B0000", fg="white", font=('Ebrima',13,'bold'))
        self.lb_time2.place(relx=0.66, rely=0, relwidth=0.2, relheight=1)

    #MENU
    def menu(self):
        menubar=Menu(self.root)
        self.root.config(menu=menubar)
        filemenu=Menu(menubar)

        def Quit(): self.root.destroy()
        menubar.add_cascade(label="Opções", menu=filemenu)
        filemenu.add_cascade(label="Sair", command=Quit)

Placar()
