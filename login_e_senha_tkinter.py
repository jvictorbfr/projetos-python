#LAYOUT DE LOGIN E SENHA by jvictor
from tkinter import *
from tkinter import ttk

root=Tk()

class Login():
    def __init__(self):
        self.root=root
        self.tela()
        self.frame()
        self.label()
        self.entry()
        self.button()
        self.menu()
        root.mainloop()

    #FUNÇÃO PARA A TELA
    def tela(self):
        self.root.title("LOGIN E SENHA by Jvictor")
        self.root.configure(background="#F5F5F5")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

    #FUNÇÃO PARA O FRAME
    def frame(self):
        self.frame=Frame(self.root, bg="white", highlightbackground='gray', highlightthickness=1)
        self.frame.place(relx=0.17 , rely=0.15, relwidth=0.6, relheight=0.65)

    #FUNÇÃO PARA AS LABELS
    def label(self):
        #LABEL LOGIN
        self.lb_login=Label(text="LOGIN", bg='#4169E1', fg='white', font=('Ebrima',9,'bold'))
        self.lb_login.place(relx=0.201, rely=0.25)

        #LABEL SENHA
        self.lb_senha=Label(text="SENHA", bg='#4169E1', fg='white', font=('Ebrima',9,'bold'))
        self.lb_senha.place(relx=0.2, rely=0.38)

        #LABEL LINHA
        self.lb_linha=Label(text="_____________________________________________________", bg='white', fg='#DCDCDC',
                            font=('Ebrima',9,'bold'))
        self.lb_linha.place(relx=0.2, rely=0.57)

    #FUNÇÃO PARA AS ENTRYS
    def entry(self):
        #ENTRY LOGIN
        self.entry_login=Entry(bg='white', highlightbackground='#DCDCDC',
                               highlightthickness=1, fg='black', font=('Ebrima',8,'bold'))
        self.entry_login.place(relx=0.3, rely=0.25, relwidth=0.4, relheight=0.053)

        #ENTRY SENHA
        self.entry_senha=Entry(bg='white', highlightbackground='#DCDCDC', show='*',
                               highlightthickness=1, fg='black', font=('Ebrima',8,'bold'))
        self.entry_senha.place(relx=0.3, rely=0.38, relwidth=0.4, relheight=0.053)

    #FUNÇÃO PARA O BOTÃO
    def button(self):
        #BOTÃO ESQUECEU SENHA
        self.bt_esqsenha=Button(text="ESQUECEU A SENHA?", bd=0, bg='white', activebackground='white', activeforeground='#4169E1',
                                fg='#4169E1', font=('Ebrima',7))
        self.bt_esqsenha.place(relx=0.2, rely=0.45)

        #BOTÃO ENTRAR
        self.bt_entrar=Button(text="ENTRAR", bd=1, bg='#4169E1', activeforeground='#4169E1',
                              fg='white', font=('Ebrima',8,'bold'))
        self.bt_entrar.place(relx=0.42, rely=0.52)

        #BOTÃO CRIAR CONTA
        self.bt_criar_conta=Button(text="NOVA CONTA", bd=1, bg='#32CD32', activeforeground='#32CD32',
                              fg='white', font=('Ebrima',8,'bold'))
        self.bt_criar_conta.place(relx=0.39, rely=0.66)

    #MENU
    def menu(self):
        menubar=Menu(self.root)
        self.root.config(menu=menubar)
        filemenu=Menu(menubar)

        def Quit(): self.root.destroy()
        menubar.add_cascade(label="Opções", menu=filemenu)
        filemenu.add_cascade(label="Sair", command=Quit)

Login()
