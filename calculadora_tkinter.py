from tkinter import *
from tkinter import ttk

root=Tk()

#ENTRY DOS NUMEROS
nmr_entry=Entry(bg="white", fg="black", font=("Ebrima", 9, "bold"))
nmr_entry.place(relx=0.28, rely=0.17, relwidth=0.4)

#FUNÇÃO PARA CLICAR NO BOTÃO
def clicar_botao(numero):
    bt=nmr_entry.get()
    nmr_entry.delete(0,END)
    nmr_entry.insert(END, str(bt)+str(numero))

#FUNÇÃO DO BOTÃO PONTO
def ponto():
    nmr_entry.insert(END, ".")

#FUNÇÃO DO BOTÃO DA SOMA
def soma():
    primeiro_numero=nmr_entry.get()
    global p_numero
    global matematica
    matematica="soma"
    p_numero=float(primeiro_numero)
    nmr_entry.delete(0,END)

#FUNÇÃO DO BOTÃO DE SUBTRAÇÃO
def subtracao():
    primeiro_numero=nmr_entry.get()
    global p_numero
    global matematica
    matematica="subtracao"
    p_numero=float(primeiro_numero)
    nmr_entry.delete(0,END)

#FUNÇÃO DO BOTÃO DE MULTIPLICAÇÃO
def multiplicacao():
    primeiro_numero=nmr_entry.get()
    global p_numero
    global matematica
    matematica="multiplicacao"
    p_numero=float(primeiro_numero)
    nmr_entry.delete(0, END)

#FUNÇÃO DO BOTÃO DE DIVISÃO
def divisao():
    primeiro_numero=nmr_entry.get()
    global p_numero
    global matematica
    matematica="divisao"
    p_numero=float(primeiro_numero)
    nmr_entry.delete(0,END)

#FUNÇÃO DO BOTÃO IGUAL
def igual():
    s_numero=nmr_entry.get()
    nmr_entry.delete(0,END)
    if (matematica=="soma"):
        nmr_entry.insert(0, p_numero+float(s_numero))
    if (matematica=="subtracao"):
        nmr_entry.insert(0, p_numero-float(s_numero))
    if (matematica=="multiplicacao"):
        nmr_entry.insert(0, p_numero*float(s_numero))
    if (matematica=="divisao"):
        nmr_entry.insert(0, p_numero/float(s_numero))

#FUNÇÃO DO BOTÃO CE
def apagar():
    nmr_entry.delete(0,END)

class DesignerCalculadora():
    def __init__(self):
        self.root=root
        self.tela()
        self.label()
        self.botao()
        root.mainloop()

    #FUNÇÃO DA TELA
    def tela(self):
        self.root.title("Calculadora by Jvictor")
        self.root.configure(background="#DCDCDC")
        self.root.geometry("280x380")
        self.root.resizable(False, False)

    #FUNÇÃO DAS LABELS
    def label(self):
        #LABEL TITULO
        self.lb_title=Label(text="CALCULADORA", bg="#DCDCDC", fg="black", font=("Ebrima",20,"bold"))
        self.lb_title.place(relx=0.12, rely=0.01)

    #FUNÇÃO PARA OS BOTÕES
    def botao(self):
        #FILEIRA1
        #BOTÃO7
        self.bt_07=Button(text="7", bd=4, bg="black", fg="white", activebackground='#DCDCDC', activeforeground='black',
                                font=("Ebrima",12,"bold"), command=lambda: clicar_botao(7))
        self.bt_07.place(relx=0.05, rely=0.3, relwidth=0.149, relheight=0.133)

        #BOTÃO4
        self.bt_04=Button(text="4", bd=4, bg="black", fg="white", activebackground='#DCDCDC', activeforeground='black',
                                font=("Ebrima",12,"bold"), command=lambda: clicar_botao(4))
        self.bt_04.place(relx=0.05, rely=0.439, relwidth=0.149, relheight=0.133)

        #BOTÃO1
        self.bt_01=Button(text="1", bd=4, bg="black", fg="white", activebackground='#DCDCDC', activeforeground='black',
                                font=("Ebrima",12,"bold"), command=lambda: clicar_botao(1))
        self.bt_01.place(relx=0.05, rely=0.576, relwidth=0.149, relheight=0.133)

        #BOTÃO0
        self.bt_00=Button(text="0", bd=4, bg="black", fg="white", activebackground='#DCDCDC', activeforeground='black',
                                font=("Ebrima",12,"bold"), command=lambda: clicar_botao(0))
        self.bt_00.place(relx=0.05, rely=0.712, relwidth=0.149, relheight=0.133)

        #FILEIRA2
        #BOTÃO8
        self.bt_08=Button(text="8", bd=4, bg="black", fg="white", activebackground='#DCDCDC', activeforeground='black',
                                font=("Ebrima",12,"bold"), command=lambda: clicar_botao(8))
        self.bt_08.place(relx=0.209, rely=0.3, relwidth=0.149, relheight=0.133)

        #BOTÃO5
        self.bt_05=Button(text="5", bd=4, bg="black", fg="white", activebackground='#DCDCDC', activeforeground='black',
                                font=("Ebrima",12,"bold"), command=lambda: clicar_botao(5))
        self.bt_05.place(relx=0.209, rely=0.439, relwidth=0.149, relheight=0.133)

        #BOTÃO2
        self.bt_02=Button(text="2", bd=4, bg="black", fg="white", activebackground='#DCDCDC', activeforeground='black',
                                font=("Ebrima",12,"bold"), command=lambda: clicar_botao(2))
        self.bt_02.place(relx=0.209, rely=0.576, relwidth=0.149, relheight=0.133)

        #BOTÃOPONTO
        self.bt_pt=Button(text=".", bd=4, bg="black", fg="white", activebackground='#DCDCDC', activeforeground='black',
                                font=("Ebrima",12,"bold"), command=ponto)
        self.bt_pt.place(relx=0.209, rely=0.712, relwidth=0.309, relheight=0.133)

        #FILEIRA3
        #BOTÃO9
        self.bt_09=Button(text="9", bd=4, bg="black", fg="white", activebackground='#DCDCDC', activeforeground='black',
                                font=("Ebrima",12,"bold"), command=lambda: clicar_botao(9))
        self.bt_09.place(relx=0.368, rely=0.3, relwidth=0.149, relheight=0.133)

        #BOTÃO6
        self.bt_06=Button(text="6", bd=4, bg="black", fg="white", activebackground='#DCDCDC', activeforeground='black',
                                font=("Ebrima",12,"bold"), command=lambda: clicar_botao(6))
        self.bt_06.place(relx=0.368, rely=0.439, relwidth=0.149, relheight=0.133)

        #BOTÃO3
        self.bt_03=Button(text="3", bd=4, bg="black", fg="white", activebackground='#DCDCDC', activeforeground='black',
                                font=("Ebrima",12,"bold"), command=lambda: clicar_botao(3))
        self.bt_03.place(relx=0.368, rely=0.576, relwidth=0.149, relheight=0.133)

        #FILEIRA4
        #BOTÃOMAIS
        self.bt_mais=Button(text="+", bd=4, bg="#696969", fg="white", activebackground='#DCDCDC', activeforeground='black',
                                font=("Ebrima",12,"bold"), command=soma)
        self.bt_mais.place(relx=0.532, rely=0.3, relwidth=0.149, relheight=0.133)

        #BOTÃOMENOS
        self.bt_menos=Button(text="-", bd=4, bg="#696969", fg="white", activebackground='#DCDCDC', activeforeground='black',
                                font=("Ebrima",12,"bold"), command=subtracao)
        self.bt_menos.place(relx=0.532, rely=0.439, relwidth=0.149, relheight=0.133)

        #BOTÃOMULTI
        self.bt_multi=Button(text="x", bd=4, bg="#696969", fg="white", activebackground='#DCDCDC', activeforeground='black',
                                font=("Ebrima",12,"bold"), command=multiplicacao)
        self.bt_multi.place(relx=0.532, rely=0.576, relwidth=0.149, relheight=0.133)

        #BOTÃODIVI
        self.bt_divi=Button(text="/", bd=4, bg="#696969", fg="white", activebackground='#DCDCDC', activeforeground='black',
                                font=("Ebrima",12,"bold"), command=divisao)
        self.bt_divi.place(relx=0.532, rely=0.712, relwidth=0.149, relheight=0.133)

        #FILEIRA4
        #BOTÃOCE
        self.bt_ce=Button(text="CE", bd=4, bg="#B22222", fg="white", activebackground='#B22222', activeforeground='white',
                                font=("Ebrima",12,"bold"), command=apagar)
        self.bt_ce.place(relx=0.71, rely=0.3, relwidth=0.23, relheight=0.68)

        #FILEIRA5
        #BOTÃOIGUAL
        self.bt_ig=Button(text="=", bd=4, bg="#696969", fg="white", activebackground='#DCDCDC', activeforeground='black',
                                font=("Ebrima",12,"bold"), command=igual)
        self.bt_ig.place(relx=0.05, rely=0.86, relwidth=0.631, relheight=0.12)

DesignerCalculadora()
