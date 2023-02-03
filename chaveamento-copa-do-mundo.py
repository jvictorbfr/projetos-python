#CHAVEAMENTO DA COPA by Jvictor
from tkinter import *
from tkinter import ttk

root=Tk()

class Application():
    def __init__(self):
        self.root=root
        self.tela()
        self.frame()
        self.botao()
        self.label()
        self.menu()
        root.mainloop()
    #FUNÇÃO PARA A TELA
    def tela(self):
        self.root.title("CHAVEAMENTO DA COPA DO MUNDO 2022")
        self.root.configure(background="#8B0000")
        self.root.geometry("800x500")
        self.root.resizable(False, False)

    #FUNÇÃO PARA O FRAME
    def frame(self):
        self.frame=Frame(self.root, bd=5, bg='white',highlightbackground='#FF7F50', highlightthickness=4 )
        self.frame.place(relx=0.02 , rely=0.02, relwidth=0.96, relheight=0.96)

    #FUNÇÃO PARA O BOTÃO CAMPEÃO
    def botao(self):
        self.bt_campeao=Button(self.frame, text="CAMPEÃO!", bd=2, bg='gold', fg='black',
                              font=('verdana',8,'bold'))
        self.bt_campeao.place(relx=0.46, rely=0.04, relwidth=0.10, relheight=0.07)

    #FUNÇÃO PARA AS LABELS
    def label(self):
        #LABEL TITULO
        self.titulo_lb=Label(self.frame, text="WORLD CUP CATAR 2022", bg='white', fg='#8B0000',
                             font=('Ebrima',11,'bold'))
        self.titulo_lb.place(relx=0.39, rely=0.9, relwidth=0.25)
        #LABEL OITAVAS
        self.lb_oitavas1=Label(self.frame, text="OITAVAS", bg='#8B0000', fg='white', font=('Ebrima',9,'bold'))
        self.lb_oitavas1.place(relx=0.045, rely=0.04, relwidth=0.10)

        self.lb_oitavas2=Label(self.frame, text="OITAVAS", bg='#8B0000', fg='white', font=('Ebrima',9,'bold'))
        self.lb_oitavas2.place(relx=0.865, rely=0.04, relwidth=0.10)

        #LABEL QUARTAS
        self.lb_quartas1=Label(self.frame, text="QUARTAS", bg='#8B0000', fg='white', font=('Ebrima',9,'bold'))
        self.lb_quartas1.place(relx=0.20, rely=0.1, relwidth=0.10)

        self.lb_quartas2=Label(self.frame, text="QUARTAS", bg='#8B0000', fg='white', font=('Ebrima',9,'bold'))
        self.lb_quartas2.place(relx=0.715, rely=0.1, relwidth=0.10)

        #LABEL SEMIS
        self.lb_semis1=Label(self.frame, text="SEMIS", bg='#8B0000', fg='white', font=('Ebrima',9,'bold'))
        self.lb_semis1.place(relx=0.32, rely=0.27, relwidth=0.10)

        self.lb_semis2=Label(self.frame, text="SEMIS", bg='#8B0000', fg='white', font=('Ebrima',9,'bold'))
        self.lb_semis2.place(relx=0.6, rely=0.27, relwidth=0.10)

        #LABEL FINAL
        self.lb_final=Label(self.frame, text="FINAL", bg='#8B0000', fg='white', font=('Ebrima',9,'bold'))
        self.lb_final.place(relx=0.46, rely=0.4, relwidth=0.10)

        #LABEL CAMPEÃO
        self.lb_camp=Label(self.frame, text="ARGENTINA", bg='lightblue', fg='white',)
        self.lb_camp.place(relx=0.46, rely=0.12, relwidth=0.1, relheight=0.06)

        #CONFRONTO 1 OITAVAS
        self.lb_hol=Label(self.frame, text="HOL", bg='orange', fg='blue')
        self.lb_hol.place(relx=0.05, rely=0.1, relwidth=0.05)
        self.hol_lb=Label(self.frame, text="3", bg='#8B0000', fg='white', font=('Ebrima',9,'bold'))
        self.hol_lb.place(relx=0.11, rely=0.1, relwidth=0.028, relheight=0.047)

        self.lb_eua=Label(self.frame, text="EUA", bg='red', fg='cyan')
        self.lb_eua.place(relx=0.05, rely=0.16, relwidth=0.05)
        self.eua_lb=Label(self.frame, text="1", bg='#8B0000', fg='white', font=('Ebrima',9,'bold'))
        self.eua_lb.place(relx=0.11, rely=0.16, relwidth=0.028, relheight=0.047)

        #CONFRONTO 2 OITAVAS
        self.lb_arg=Label(self.frame, text="ARG", bg='lightblue', fg='white')
        self.lb_arg.place(relx=0.05, rely=0.26, relwidth=0.05)
        self.arg_lb=Label(self.frame, text="2", bg='#8B0000', fg='white', font=('Ebrima',9,'bold'))
        self.arg_lb.place(relx=0.11, rely=0.26, relwidth=0.028, relheight=0.047)

        self.lb_aus=Label(self.frame, text="AUS", bg='yellow', fg='blue')
        self.lb_aus.place(relx=0.05, rely=0.32, relwidth=0.05)
        self.aus_lb=Label(self.frame, text="1", bg='#8B0000', fg='white', font=('Ebrima',9,'bold'))
        self.aus_lb.place(relx=0.11, rely=0.32, relwidth=0.028, relheight=0.047)

        #CONFRONTO 3 OITAVAS
        self.lb_jap=Label(self.frame, text="JAP", bg='#FFFAF0', fg='red')
        self.lb_jap.place(relx=0.05, rely=0.62, relwidth=0.05)
        self.jap_lb=Label(self.frame, text="1(1)", bg='#8B0000', fg='white', font=('Ebrima',8,'bold'))
        self.jap_lb.place(relx=0.11, rely=0.62, relwidth=0.028, relheight=0.047)

        self.lb_cro=Label(self.frame, text="CRO", bg='red', fg='blue')
        self.lb_cro.place(relx=0.05, rely=0.68, relwidth=0.05)
        self.cro_lb=Label(self.frame, text="1(3)", bg='#8B0000', fg='white', font=('Ebrima',8,'bold'))
        self.cro_lb.place(relx=0.11, rely=0.68, relwidth=0.028, relheight=0.047)

        #CONFRONTO 4 OITAVAS
        self.lb_bra=Label(self.frame, text="BRA", bg='green', fg='yellow')
        self.lb_bra.place(relx=0.05, rely=0.78, relwidth=0.05)
        self.bra_lb=Label(self.frame, text="4", bg='#8B0000', fg='white', font=('Ebrima',9,'bold'))
        self.bra_lb.place(relx=0.11, rely=0.78, relwidth=0.028, relheight=0.047)

        self.lb_cor=Label(self.frame, text="COR", bg='blue', fg='white')
        self.lb_cor.place(relx=0.05, rely=0.84, relwidth=0.05)
        self.cor_lb=Label(self.frame, text="1", bg='#8B0000', fg='white', font=('Ebrima',9,'bold'))
        self.cor_lb.place(relx=0.11, rely=0.84, relwidth=0.028, relheight=0.047)

        #CONFRONTO 5 OITAVAS
        self.lb_ing=Label(self.frame, text="ING", bg='#FFFAF0', fg='red')
        self.lb_ing.place(relx=0.91, rely=0.1, relwidth=0.05)
        self.ing_lb=Label(self.frame, text="3", bg='#8B0000', fg='white', font=('Ebrima',9,'bold'))
        self.ing_lb.place(relx=0.87, rely=0.1, relwidth=0.028, relheight=0.047)

        self.lb_sen=Label(self.frame, text="SEN", bg='lightgreen', fg='red')
        self.lb_sen.place(relx=0.91, rely=0.16, relwidth=0.05)
        self.sen_lb=Label(self.frame, text="0", bg='#8B0000', fg='white', font=('Ebrima',9,'bold'))
        self.sen_lb.place(relx=0.87, rely=0.16, relwidth=0.028, relheight=0.047)

        #CONFRONTO 6 OITAVAS
        self.lb_fra=Label(self.frame, text="FRA", bg='blue', fg='#B22222')
        self.lb_fra.place(relx=0.91, rely=0.26, relwidth=0.05)
        self.fra_lb=Label(self.frame, text="3", bg='#8B0000', fg='white', font=('Ebrima',9,'bold'))
        self.fra_lb.place(relx=0.87, rely=0.26, relwidth=0.028, relheight=0.047)

        self.lb_pol=Label(self.frame, text="POL", bg='red', fg='white')
        self.lb_pol.place(relx=0.91, rely=0.32, relwidth=0.05)
        self.pol_lb=Label(self.frame, text="1", bg='#8B0000', fg='white', font=('Ebrima',9,'bold'))
        self.pol_lb.place(relx=0.87, rely=0.32, relwidth=0.028, relheight=0.047)

        #CONFRONTO 7 OITAVAS
        self.lb_mar=Label(self.frame, text="MAR", bg='red', fg='lightgreen')
        self.lb_mar.place(relx=0.91, rely=0.62, relwidth=0.05)
        self.mar_lb=Label(self.frame, text="(3)0", bg='#8B0000', fg='white', font=('Ebrima',8,'bold'))
        self.mar_lb.place(relx=0.87, rely=0.62, relwidth=0.028, relheight=0.047)

        self.lb_esp=Label(self.frame, text="ESP", bg='red', fg='yellow')
        self.lb_esp.place(relx=0.91, rely=0.68, relwidth=0.05)
        self.esp_lb=Label(self.frame, text="(0)0", bg='#8B0000', fg='white', font=('Ebrima',8,'bold'))
        self.esp_lb.place(relx=0.87, rely=0.68, relwidth=0.028, relheight=0.047)

        #CONFRONTO 8 OITAVAS
        self.lb_por=Label(self.frame, text="POR", bg='red', fg='green')
        self.lb_por.place(relx=0.91, rely=0.78, relwidth=0.05)
        self.por_lb=Label(self.frame, text="6", bg='#8B0000', fg='white', font=('Ebrima',9,'bold'))
        self.por_lb.place(relx=0.87, rely=0.78, relwidth=0.028, relheight=0.047)

        self.lb_sui=Label(self.frame, text="SUI", bg='red', fg='white')
        self.lb_sui.place(relx=0.91, rely=0.84, relwidth=0.05)
        self.sui_lb=Label(self.frame, text="1", bg='#8B0000', fg='white', font=('Ebrima',9,'bold'))
        self.sui_lb.place(relx=0.87, rely=0.84, relwidth=0.028, relheight=0.047)

        #CONFRONTO 1 QUARTAS
        self.lb_hol2=Label(self.frame, text="HOL", bg='orange', fg='blue')
        self.lb_hol2.place(relx=0.21, rely=0.16, relwidth=0.05)
        self.hol2_lb=Label(self.frame, text="2(3)", bg='#8B0000', fg='white', font=('Ebrima',8,'bold'))
        self.hol2_lb.place(relx=0.268, rely=0.16, relwidth=0.028, relheight=0.048)

        self.lb_arg2=Label(self.frame, text="ARG", bg='lightblue', fg='white')
        self.lb_arg2.place(relx=0.21, rely=0.26, relwidth=0.05)
        self.arg2_lb=Label(self.frame, text="2(4)", bg='#8B0000', fg='white', font=('Ebrima',8,'bold'))
        self.arg2_lb.place(relx=0.268, rely=0.26, relwidth=0.028, relheight=0.048)

        #CONFRONTO 2 QUARTAS
        self.lb_cro2=Label(self.frame, text="CRO", bg='red', fg='blue')
        self.lb_cro2.place(relx=0.21, rely=0.68, relwidth=0.05)
        self.cro2_lb=Label(self.frame, text="1(4)", bg='#8B0000', fg='white', font=('Ebrima',9,'bold'))
        self.cro2_lb.place(relx=0.268, rely=0.68, relwidth=0.028, relheight=0.048)

        self.lb_bra2=Label(self.frame, text="BRA", bg='green', fg='yellow')
        self.lb_bra2.place(relx=0.21, rely=0.78, relwidth=0.05)
        self.bra2_lb=Label(self.frame, text="1(2)", bg='#8B0000', fg='white', font=('Ebrima',9,'bold'))
        self.bra2_lb.place(relx=0.268, rely=0.78, relwidth=0.028, relheight=0.048)

        #CONFRONTO 3 QUARTAS
        self.lb_ing2=Label(self.frame, text="ING", bg='#FFFAF0', fg='red')
        self.lb_ing2.place(relx=0.76, rely=0.16, relwidth=0.05)
        self.ing2_lb=Label(self.frame, text="1", bg='#8B0000', fg='white', font=('Ebrima',9,'bold'))
        self.ing2_lb.place(relx=0.725, rely=0.16, relwidth=0.028, relheight=0.048)

        self.lb_fra2=Label(self.frame, text="FRA", bg='blue', fg='#B22222')
        self.lb_fra2.place(relx=0.76, rely=0.26, relwidth=0.05)
        self.fra2_lb=Label(self.frame, text="2", bg='#8B0000', fg='white', font=('Ebrima',9,'bold'))
        self.fra2_lb.place(relx=0.725, rely=0.26, relwidth=0.028, relheight=0.048)

        #CONFRONTO 4 QUARTAS
        self.lb_mar2=Label(self.frame, text="MAR", bg='red', fg='lightgreen')
        self.lb_mar2.place(relx=0.76, rely=0.68, relwidth=0.05)
        self.mar2_lb=Label(self.frame, text="1", bg='#8B0000', fg='white', font=('Ebrima',9,'bold'))
        self.mar2_lb.place(relx=0.725, rely=0.68, relwidth=0.028, relheight=0.048)

        self.lb_por2=Label(self.frame, text="POR", bg='red', fg='green')
        self.lb_por2.place(relx=0.76, rely=0.78, relwidth=0.05)
        self.por2_lb=Label(self.frame, text="0", bg='#8B0000', fg='white', font=('Ebrima',9,'bold'))
        self.por2_lb.place(relx=0.725, rely=0.78, relwidth=0.028, relheight=0.048)

        #CONFRONTO 1 SEMIS
        self.lb_arg3=Label(self.frame, text="ARG", bg='lightblue', fg='white')
        self.lb_arg3.place(relx=0.325, rely=0.35, relwidth=0.05)
        self.arg3_lb=Label(self.frame, text="3", bg='#8B0000', fg='white', font=('Ebrima',9,'bold'))
        self.arg3_lb.place(relx=0.385, rely=0.35, relwidth=0.028, relheight=0.048)

        self.lb_cro3=Label(self.frame, text="CRO", bg='red', fg='blue')
        self.lb_cro3.place(relx=0.325, rely=0.6, relwidth=0.05)
        self.cro3_lb=Label(self.frame, text="0", bg='#8B0000', fg='white', font=('Ebrima',9,'bold'))
        self.cro3_lb.place(relx=0.385, rely=0.6, relwidth=0.028, relheight=0.048)

        #CONFRONTO 2 SEMIS
        self.lb_fra3=Label(self.frame, text="FRA", bg='blue', fg='#B22222')
        self.lb_fra3.place(relx=0.64, rely=0.35, relwidth=0.05)
        self.fra3_lb=Label(self.frame, text="2", bg='#8B0000', fg='white', font=('Ebrima',9,'bold'))
        self.fra3_lb.place(relx=0.603, rely=0.35, relwidth=0.028, relheight=0.048)

        self.lb_mar3=Label(self.frame, text="MAR", bg='red', fg='lightgreen')
        self.lb_mar3.place(relx=0.64, rely=0.6, relwidth=0.05)
        self.mar3_lb=Label(self.frame, text="0", bg='#8B0000', fg='white', font=('Ebrima',9,'bold'))
        self.mar3_lb.place(relx=0.603, rely=0.6, relwidth=0.028, relheight=0.048)

        #CONFRONTO FINAL
        self.lb_arg4=Label(self.frame, text="ARG", bg='lightblue', fg='white')
        self.lb_arg4.place(relx=0.465, rely=0.456, relwidth=0.05)
        self.arg4_lb=Label(self.frame, text="3(4)", bg='#8B0000', fg='white', font=('Ebrima',8,'bold'))
        self.arg4_lb.place(relx=0.525, rely=0.46, relwidth=0.028, relheight=0.048)

        self.lb_fra4=Label(self.frame, text="FRA", bg='blue', fg='#B22222')
        self.lb_fra4.place(relx=0.465, rely=0.52, relwidth=0.05)
        self.fra4_lb=Label(self.frame, text="3(2)", bg='#8B0000', fg='white', font=('Ebrima',8,'bold'))
        self.fra4_lb.place(relx=0.525, rely=0.52, relwidth=0.028, relheight=0.048)

    #MENU
    def menu(self):
        menubar=Menu(self.root)
        self.root.config(menu=menubar)
        filemenu=Menu(menubar)

        def Quit(): self.root.destroy()
        menubar.add_cascade(label="Opções", menu=filemenu)
        filemenu.add_cascade(label="Sair", command=Quit)

Application()