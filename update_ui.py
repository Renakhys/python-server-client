import tkinter as tk


class App:
    def __init__(self, root=None):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        tk.Label(self.frame, text='Menu principale').pack()
        tk.Button(self.frame, text='Inizia Partita', command=self.start_tris).pack()
        self.tris = TicTacToe(master=self.root, app=self)

    def goto_menu(self):
        # mostra il menu principale (frame)
        self.frame.pack()

    def start_tris(self):
        # nasconde il menu principale
        self.frame.pack_forget()
        # mostra la partita
        self.tris.mostra_tris()


class TicTacToe:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master)
        tk.Label(self.frame, text='Tic Tac Toe').pack()

        # stato della partita
        # 0 = cella vuota
        # 1 = X
        # - 1 = O
        self.state = []
        # griglia di pulsanti del tris
        self.game = tk.Frame(self.frame)
        self.cells = []
        for x in range(0,3):
            for y in range(0,3):
                print(x,y)
                cell=tk.Button(self.game, command= lambda c=x*3+y : self.cella_click(c))
                cell.grid(row=x,column=y)
                self.cells.append(cell)    
                self.state.append(0)
        self.game.pack()

        # giocatore corrente (X)
        self.current_turn = 1

        # comandi vari
        tk.Button(self.frame, text='menu', command=self.goto_menu).pack()
        tk.Button(self.frame, text='ricomincia', command=self.reset_partita).pack()
        self.reset_partita()

    def reset_partita(self):
        # reset dello stato della partita
        for c in range(0,9):
            self.state[c] = 0
        # aggiorna la grafica con lo stato della partita
        self.update_ui()

    def update_ui(self):
        # passa tutte le celle e imposta il testo corretto in base allo stato della partita
        for c in range(0,9):
            if(self.state[c] == 0):
                self.cells[c]["text"] = " "
            if(self.state[c] == 1):
                self.cells[c]["text"] = "X"
            if(self.state[c] == -1):
                self.cells[c]["text"] = "O"

    def cella_click(self, c):
        # controllo se la cella cliccata è vuota
        if(self.state[c] == 0):
            # imposto lo stato della cella al giocatore corrente
            self.state[c] = self.current_turn
            # cambio giocatore
            self.current_turn = self.current_turn * -1
            # mostro lo stato aggiornato della partita
            self.update_ui()
            # qui andrebbe controllato se la partita è finita
        else:
            print("mossa non valida")

    def mostra_tris(self):
        # mostra nella finestra la partita
        self.frame.pack()

    def goto_menu(self):
        # nasconde la partita
        self.frame.pack_forget()
        # mostra il menu principale
        self.app.goto_menu()


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
