from tkinter import *

# CORES
blue="#1E90FF"
red="#DC143C"

# MENU
def menu():
    menubar = Menu(root)
    root.config(menu=menubar)
    filemenu = Menu(menubar)

    def Quit(): root.destroy()

    menubar.add_cascade(label="Opções", menu=filemenu)
    filemenu.add_cascade(label="Sair", command=Quit)

# CRIAÇÃO DA JANELA
root = Tk()
root.title("Jogo da Velha")
root.geometry("300x400")
root.resizable(False, False)
root.configure(background="gray85")
menu()

# FRAME 1
frame1 = Frame(root, bg="gray20")
frame1.place(relx="0.03", rely="0.02", relwidth="0.94", relheight="0.3")

# FRAME 2
frame2 = Frame(root, bg="gray85")
frame2.place(relx="0.03", rely="0.33", relwidth="0.94", relheight="0.645")

# WIDGETS FRAME 1--------------------------

# LABEL X
playerX = Label(frame1, text="X", bg="gray20", fg=red, font=("Ivy", 45, "bold"))
playerX.place(relx=0.1, rely=0.08)

playerX_text = Label(frame1, text="JOGADOR 1", bg="gray20", fg="white", font=("Ebrima", 9, "bold"))
playerX_text.place(relx=0.055, rely=0.7)

playerX_points = Label(frame1, text="0", bg="gray20", fg="white", font=("Ivy", 35, "bold"))
playerX_points.place(relx=0.33, rely=0.15)

# VERSUS
versus = Label(frame1, text="x", bg="gray20", fg="white", font=("Ivy", 30, "bold"))
versus.place(relx=0.438, rely=0.18)

# LABEL O
playerO = Label(frame1, text="O", bg="gray20", fg=blue, font=("Ivy", 48, "bold"))
playerO.place(relx=0.7, rely=0.06)

playerO_text = Label(frame1, text="JOGADOR 2", bg="gray20", fg="white", font=("Ebrima", 9, "bold"))
playerO_text.place(relx=0.67, rely=0.7)

playerO_points = Label(frame1, text="0", bg="gray20", fg="white", font=("Ivy", 35, "bold"))
playerO_points.place(relx=0.53, rely=0.15)

# FUNÇÕES----------------------------------

player1 = "X"
player2 = "O"

score1 = 0
score2 = 0

table = [['1','2','3'] , ['4','5','6'] , ['7','8','9']]

playing = 'X'
play = ''
contador = 0
contador_de_rodadas = 0

def start():
    bt_play.destroy()
    def controlar(i):
        global playing
        global contador
        global play

        # COMPARA OS VALORES
        if i == str(1):
            if button01['text'] == '':
                if playing == 'X':
                    color=red
                if playing == 'O':
                    color=blue

                # DEFINE COR E TEXTO
                button01['fg'] = color
                button01['text'] = playing
                table[0][0] = playing

                # VERIFICA QUEM ESTÁ JOGANDO
                if playing == 'X':
                    playing = 'O'
                    play = 'Jogador 1'
                else:
                    playing = 'X'
                    play = 'Jogador 2'

                # PASSA A RODADA
                contador+=1

        # COMPARA OS VALORES
        if i == str(2):
            if button02['text'] == '':
                if playing == 'X':
                    color = red
                if playing == 'O':
                    color = blue

                # DEFINE COR E TEXTO
                button02['fg'] = color
                button02['text'] = playing
                table[0][1] = playing

                # VERIFICA QUEM ESTÁ JOGANDO
                if playing == 'X':
                    playing = 'O'
                    play = 'Jogador 1'
                else:
                    playing = 'X'
                    play = 'Jogador 2'

                # PASSA A RODADA
                contador += 1

        # COMPARA OS VALORES
        if i == str(3):
            if button03['text'] == '':
                if playing == 'X':
                    color = red
                if playing == 'O':
                    color = blue

                # DEFINE COR E TEXTO
                button03['fg'] = color
                button03['text'] = playing
                table[0][2] = playing

                # VERIFICA QUEM ESTÁ JOGANDO
                if playing == 'X':
                    playing = 'O'
                    play = 'Jogador 1'
                else:
                    playing = 'X'
                    play = 'Jogador 2'

                # PASSA A RODADA
                contador += 1

        # COMPARA OS VALORES
        if i == str(4):
            if button04['text'] == '':
                if playing == 'X':
                    color = red
                if playing == 'O':
                    color = blue

                # DEFINE COR E TEXTO
                button04['fg'] = color
                button04['text'] = playing
                table[1][0] = playing

                # VERIFICA QUEM ESTÁ JOGANDO
                if playing == 'X':
                    playing = 'O'
                    play = 'Jogador 1'
                else:
                    playing = 'X'
                    play = 'Jogador 2'

                # PASSA A RODADA
                contador += 1

        # COMPARA OS VALORES
        if i == str(5):
            if button05['text'] == '':
                if playing == 'X':
                    color = red
                if playing == 'O':
                    color = blue

                # DEFINE COR E TEXTO
                button05['fg'] = color
                button05['text'] = playing
                table[1][1] = playing

                # VERIFICA QUEM ESTÁ JOGANDO
                if playing == 'X':
                    playing = 'O'
                    play = 'Jogador 1'
                else:
                    playing = 'X'
                    play = 'Jogador 2'

                # PASSA A RODADA
                contador += 1

        # COMPARA OS VALORES
        if i == str(6):
            if button06['text'] == '':
                if playing == 'X':
                    color = red
                if playing == 'O':
                    color = blue

                # DEFINE COR E TEXTO
                button06['fg'] = color
                button06['text'] = playing
                table[1][2] = playing

                # VERIFICA QUEM ESTÁ JOGANDO
                if playing == 'X':
                    playing = 'O'
                    play = 'Jogador 1'
                else:
                    playing = 'X'
                    play = 'Jogador 2'

                # PASSA A RODADA
                contador += 1

        # COMPARA OS VALORES
        if i == str(7):
            if button07['text'] == '':
                if playing == 'X':
                    color = red
                if playing == 'O':
                    color = blue

                # DEFINE COR E TEXTO
                button07['fg'] = color
                button07['text'] = playing
                table[2][0] = playing

                # VERIFICA QUEM ESTÁ JOGANDO
                if playing == 'X':
                    playing = 'O'
                    play = 'Jogador 1'
                else:
                    playing = 'X'
                    play = 'Jogador 2'

                # PASSA A RODADA
                contador += 1

        # COMPARA OS VALORES
        if i == str(8):
            if button08['text'] == '':
                if playing == 'X':
                    color = red
                if playing == 'O':
                    color = blue

                # DEFINE COR E TEXTO
                button08['fg'] = color
                button08['text'] = playing
                table[2][1] = playing

                # VERIFICA QUEM ESTÁ JOGANDO
                if playing == 'X':
                    playing = 'O'
                    play = 'Jogador 1'
                else:
                    playing = 'X'
                    play = 'Jogador 2'

                # PASSA A RODADA
                contador += 1

        # COMPARA OS VALORES
        if i == str(9):
            if button09['text'] == '':
                if playing == 'X':
                    color = red
                if playing == 'O':
                    color = blue

                # DEFINE COR E TEXTO
                button09['fg'] = color
                button09['text'] = playing
                table[2][2] = playing

                # VERIFICA QUEM ESTÁ JOGANDO
                if playing == 'X':
                    playing = 'O'
                    play = 'Jogador 1'
                else:
                    playing = 'X'
                    play = 'Jogador 2'

                # PASSA A RODADA
                contador += 1

        # VERIFICA SE HÁ VENCEDOR
        if contador >= 5:
            # VENCEDOR PELA LINHA
            if table[0][0] == table[0][1] == table[0][2] != "":
                winner(playing)
            elif table[1][0] == table[1][1] == table[1][2] != "":
                winner(playing)
            elif table[2][0] == table[2][1] == table[2][2] != "":
                winner(playing)

            # VENCEDOR PELA COLUNA
            if table[0][0] == table[1][0] == table[2][0] != "":
                winner(playing)
            elif table[0][1] == table[1][1] == table[2][1] != "":
                winner(playing)
            elif table[0][2] == table[1][2] == table[2][2] != "":
                winner(playing)

            # VENCEDOR PELA DIAGONAL
            if table[0][0] == table[1][1] == table[2][2] != "":
                winner(playing)
            elif table[0][2] == table[1][1] == table[2][0] != "":
                winner(playing)

            # EMPATE
            if contador >= 9:
                winner("Jogo empatado!")

    def winner(i):
        global score1, score2
        global table
        global contador_de_rodadas
        global contador

        # BLOQUEANDO BOTÕES
        button01["state"] = "disable"
        button02["state"] = "disable"
        button03["state"] = "disable"
        button04["state"] = "disable"
        button05["state"] = "disable"
        button06["state"] = "disable"
        button07["state"] = "disable"
        button08["state"] = "disable"
        button09["state"] = "disable"

        winner_lb = Label(frame2, text="", bg="gray20", fg="gold", font=("Ebrima", 9, "bold"))
        winner_lb.place(relx=0.27, rely=0.8)

        if i == "X":
            score2+=1
            winner_lb["text"] = "JOGADOR 2 VENCEU!"
            playerO_points["text"] = score2

        if i == "O":
            score1+=1
            winner_lb["text"] = "JOGADOR 1 VENCEU!"
            playerX_points["text"] = score1

        if i == "Jogo empatado!":
            winner_lb["text"] = "RODADA EMPATADA!"

        def next_round():
            # LIMPA OS BOTÕES APÓS A VITÓRIA
            button01["text"] = ""
            button02["text"] = ""
            button03["text"] = ""
            button04["text"] = ""
            button05["text"] = ""
            button06["text"] = ""
            button07["text"] = ""
            button08["text"] = ""
            button09["text"] = ""

            button01["state"] = "normal"
            button02["state"] = "normal"
            button03["state"] = "normal"
            button04["state"] = "normal"
            button05["state"] = "normal"
            button06["state"] = "normal"
            button07["state"] = "normal"
            button08["state"] = "normal"
            button09["state"] = "normal"

            winner_lb.destroy()
            bt_play.destroy()

        # BOTÃO PRÓXIMA RODADA
        bt_nextRound = Button(frame2, text="PRÓXIMA RODADA", bg="gray20", cursor="hand2", activebackground="gray85",
                         fg="white", font=("Ebrima", 9, "bold"), command=next_round)
        bt_nextRound.place(relx=0.29, rely=0.9, relwidth=0.4)

        def game_over():
            bt_play.destroy()
            winner_lb.destroy()

            end()

        if contador_de_rodadas >= 4:
            game_over()

        else:
            contador_de_rodadas += 1
            # REINICIA A TABELA
            table = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
            contador = 0


    #FIM DO JOGO
    def end():
        global table
        global contador_de_rodadas
        global score1, score2
        global contador

        table = [['1','2','3'] , ['4','5','6'] , ['7','8','9']]
        contador_de_rodadas = 0
        score1 = 0
        score2 = 0
        contador = 0

        # BLOQUEANDO BOTÕES
        button01["state"] = "disable"
        button02["state"] = "disable"
        button03["state"] = "disable"
        button04["state"] = "disable"
        button05["state"] = "disable"
        button06["state"] = "disable"
        button07["state"] = "disable"
        button08["state"] = "disable"
        button09["state"] = "disable"

        end_lb = Label(frame2, text="FIM DO JOGO!", bg="gray20", fg="gold", font=("Ebrima", 9, "bold"))
        end_lb.place(relx=0.34, rely=0.8)

        # NOVO JOGO
        def new_game():
            playerX_points["text"] = "0"
            playerO_points["text"] = "0"
            end_lb.destroy()
            bt_newGame.destroy()

            # INICIANDO O JOGO NOVAMENTE
            start()

        bt_newGame = Button(frame2, text="JOGAR NOVAMENTE", bg="gray20", cursor="hand2", activebackground="gray85",
                        fg="white", font=("Ebrima", 9, "bold"), command=new_game)
        bt_newGame.place(relx=0.27, rely=0.9)

    # WIDGETS FRAME 2--------------------------

    # LABEL VERTICAL
    vertical_lb = Label(frame2, text="", bg="gray20", font=("Ebrima", 5, "bold"))
    vertical_lb.place(relx=0.32, rely=0.05, relheight=0.8)

    vertical_lb2 = Label(frame2, text="", bg="gray20", font=("Ebrima", 5, "bold"))
    vertical_lb2.place(relx=0.65, rely=0.05, relheight=0.8)

    # LABEL HORIZONTAL
    horizontal_lb = Label(frame2, text="", bg="gray20", font=("Ebrima", 5, "bold"))
    horizontal_lb.place(relx=0.09, rely=0.27, relwidth=0.8, relheight=0.02)

    horizontal_lb2 = Label(frame2, text="", bg="gray20", font=("Ebrima", 5, "bold"))
    horizontal_lb2.place(relx=0.09, rely=0.6, relwidth=0.8, relheight=0.02)

    # LINHA 1----------------------------------

    # BOTÃO 1
    button01 = Button(frame2, text="", bg="gray85", font=("Ivy", 30, "bold"),
                      activebackground="gray85", relief="flat", command=lambda:controlar('1'))
    button01.place(relx=0.09, rely=0.05, relwidth=0.23, relheight=0.22)

    # BOTÃO 2
    button02 = Button(frame2, text="", bg="gray85", font=("Ivy", 30, "bold"),
                      activebackground="gray85", relief="flat", command=lambda:controlar('2'))
    button02.place(relx=0.34, rely=0.05, relwidth=0.31, relheight=0.22)

    # BOTÃO 3
    button03 = Button(frame2, text="", bg="gray85", font=("Ivy", 30, "bold"),
                      activebackground="gray85", relief="flat", command=lambda:controlar('3'))
    button03.place(relx=0.67, rely=0.05, relwidth=0.22, relheight=0.22)

    # LINHA 2-----------------------------------

    # BOTÃO 4
    button04 = Button(frame2, text="", bg="gray85", font=("Ivy", 30, "bold"),
                      activebackground="gray85", relief="flat", command=lambda:controlar('4'))
    button04.place(relx=0.09, rely=0.3, relwidth=0.23, relheight=0.28)

    # BOTÃO 5
    button05 = Button(frame2, text="", bg="gray85", font=("Ivy", 30, "bold"),
                      activebackground="gray85", relief="flat", command=lambda:controlar('5'))
    button05.place(relx=0.34, rely=0.3, relwidth=0.31, relheight=0.28)

    # BOTÃO 6
    button06 = Button(frame2, text="", bg="gray85", font=("Ivy", 30, "bold"),
                      activebackground="gray85", relief="flat", command=lambda:controlar('6'))
    button06.place(relx=0.67, rely=0.3, relwidth=0.22, relheight=0.28)

    # LINHA 3-----------------------------------

    # BOTÃO 7
    button07 = Button(frame2, text="", bg="gray85", font=("Ivy", 30, "bold"),
                      activebackground="gray85", relief="flat", command=lambda:controlar('7'))
    button07.place(relx=0.09, rely=0.63, relwidth=0.23, relheight=0.22)

    # BOTÃO 8
    button08 = Button(frame2, text="", bg="gray85", font=("Ivy", 30, "bold"),
                      activebackground="gray85", relief="flat", command=lambda:controlar('8'))
    button08.place(relx=0.34, rely=0.63, relwidth=0.31, relheight=0.22)

    # BOTÃO 9
    button09 = Button(frame2, text="", bg="gray85", font=("Ivy", 30, "bold"),
                      activebackground="gray85", relief="flat", command=lambda:controlar('9'))
    button09.place(relx=0.67, rely=0.63, relwidth=0.22, relheight=0.22)

# BOTÃO PLAY
bt_play = Button(frame2, text="JOGAR", bg="gray20", cursor="hand2", activebackground="gray85",
                 fg="white", font=("Ebrima",9, "bold"), command=start)
bt_play.place(relx=0.29, rely=0.9, relwidth=0.4)

root.mainloop()