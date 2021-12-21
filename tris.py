import tkinter as tk
import tkinter.font as tkFont


class Menu:
  def __init__ (self):
    self.root = tk.Tk()
    self.root.geometry("300x300")

    self.frame = tk.Frame(self.root)
    self.frame.pack()

    self.fontSryle = tkFont.Font(family="Helvetica", size=20)

    self.testo_mod = tk.Label(self.frame, text="Scegli la modalità di gioco:", borderwidth=4, relief="groove", font="Helvetica", bg="white")
    self.testo_mod.grid(row=1, column=4, sticky="N")

    self.button_modA = tk.Button(self.frame,
                              text = "Inizia partita",
                              textvariable=self.testo_mod,
                              state="normal",
                              command=self.touch_mod_a,
                              font= self.fontSryle,
                              bg="white",
                              fg="black")

    self.button_modA.place(width=50,
                        height=50,
                        y=100,
                        x=100)
    self.button_modA.grid(row=2, column=4, sticky="N")

    self.game = Test(self.root)

    self.root.mainloop()
  
  def touch_mod_a(self):
    self.frame.pack_forget()
    self.game.mostra_tris()
    




class Test:
  
    def __init__(self, root):
        self.root = tk.Frame(root)
        self.i=0

        self.text0 = tk.StringVar()
        self.text1 = tk.StringVar()
        self.text2 = tk.StringVar()
        self.text3 = tk.StringVar()
        self.text4 = tk.StringVar()
        self.text5 = tk.StringVar()
        self.text6 = tk.StringVar()
        self.text7 = tk.StringVar()
        self.text8 = tk.StringVar()
        self.text9 = tk.StringVar()

        self.text0.set("RESTART")
        self.text1.set("  ")
        self.text2.set("  ")
        self.text3.set("  ")
        self.text4.set("  ")
        self.text5.set("  ")
        self.text6.set("  ")
        self.text7.set("  ")
        self.text8.set("  ")
        self.text9.set("  ")

        self.bottoneA_x = False
        self.bottoneA_o = False
        self.bottoneB_x = False
        self.bottoneB_o = False
        self.bottoneC_x = False
        self.bottoneC_o = False
        self.bottoneD_x = False
        self.bottoneD_o = False
        self.bottoneE_x = False
        self.bottoneE_o = False
        self.bottoneF_x = False
        self.bottoneF_o = False
        self.bottoneG_x = False
        self.bottoneG_o = False
        self.bottoneH_x = False
        self.bottoneH_o = False
        self.bottoneI_x = False
        self.bottoneI_o = False
        

        self.titolo = tk.Label(self.root, text="TRIS", borderwidth=4, relief="groove", font="Helvetica", bg="white")
        self.titolo.grid(row=1, column=4, sticky="N")

        self.testo = tk.Label(self.root, text="Giocatore 1 è O e giocatore 2 è X", borderwidth=4, relief="groove", font="Helvetica", bg="white")
        self.testo.grid(row=2, column=2, columnspan=5, sticky="N", padx=10, pady=5)

        self.fontSryle = tkFont.Font(family="Helvetica", size=20)
        self.fontSryle2 = tkFont.Font(family="Helvetica", size=10)

        self.canvas = tk.Canvas(self.root)
        self.buttonA = tk.Button(self.canvas,
                                textvariable=self.text1,
                                state="normal",
                                command=self.changeText1,
                                font= self.fontSryle,
                                bg="white",
                                fg="black")

        self.buttonA.place(width=50,
                            height=50,
                            y=100,
                            x=20)


        self.buttonB = tk.Button(self.canvas,
                                textvariable=self.text2,
                                state="normal",
                                command=self.changeText2,
                                font= self.fontSryle,
                                bg="white",
                                fg="black")

        self.buttonB.place(width=50,
                            height=50,
                            y=100,
                            x=90)


        self.buttonC = tk.Button(self.canvas,
                                textvariable=self.text3,
                                state="normal",
                                command=self.changeText3,
                                font= self.fontSryle,
                                bg="white",
                                fg="black")

        self.buttonC.place(width=50,
                            height=50,
                            y=100,
                            x=160)


        self.buttonD = tk.Button(self.canvas,
                                textvariable=self.text4,
                                state="normal",
                                command=self.changeText4,
                                font= self.fontSryle,
                                bg="white",
                                fg="black")

        self.buttonD.place(width=50,
                            height=50,
                            y=170,
                            x=20)


        self.buttonE = tk.Button(self.canvas,
                                textvariable=self.text5,
                                state="normal",
                                command=self.changeText5,
                                font= self.fontSryle,
                                bg="white",
                                fg="black")

        self.buttonE.place(width=50,
                            height=50,
                            y=170,
                            x=90)


        self.buttonF = tk.Button(self.canvas,
                                textvariable=self.text6,
                                state="normal",
                                command=self.changeText6,
                                font= self.fontSryle,
                                bg="white",
                                fg="black")

        self.buttonF.place(width=50,
                            height=50,
                            y=170,
                            x=160)


        self.buttonG = tk.Button(self.canvas,
                                textvariable=self.text7,
                                state="normal",
                                command=self.changeText7,
                                font= self.fontSryle,
                                bg="white",
                                fg="black")

        self.buttonG.place(width=50,
                            height=50,
                            y=240,
                            x=20)


        self.buttonH = tk.Button(self.canvas,
                                textvariable=self.text8,
                                state="normal",
                                command=self.changeText8,
                                font= self.fontSryle,
                                bg="white",
                                fg="black")

        self.buttonH.place(width=50,
                            height=50,
                            y=240,
                            x=90)


        self.buttonI = tk.Button(self.canvas,
                                textvariable=self.text9,
                                state="normal",
                                command=self.changeText9,
                                font= self.fontSryle,
                                bg="white",
                                fg="black")

        self.buttonI.grid(column=2, row=5)
        self.buttonI.place(width=50,
                            height=50,
                            y=240,
                            x=160)

        self.button_restart = tk.Button(self.canvas,
                                textvariable=self.text0,
                                state="normal",
                                #command= self.restart_program(),
                                font= self.fontSryle2,
                                bg="white",
                                fg="black")

        self.canvas.grid(row=3, column=4, sticky="N")
        self.button_restart.place(width=50, height=50, y=100, x=230)

    def mostra_tris(self):
      self.root.pack()
        
       
#    def restart_program(self):
#     python = sys.executable
#      os.execl(python, python, * sys.argv)



    def changeText1(self):
        self.i += 1 
        if self.i % 2 == 0:
            self.buttonA.config(state="disabled")
            self.text1.set("X")
            self.bottoneA_x = True
            self.cont_x()

        elif self.i % 2 != 0:
            self.buttonA.config(state="disabled")
            self.text1.set("O")
            self.bottoneA_o = True
            self.cont_o()

    def changeText2(self):
        self.i += 1
        if self.i % 2 == 0:
            self.buttonB.config(state="disabled")
            self.text2.set("X")
            self.bottoneB_x = True
            self.cont_x()

        elif self.i % 2 != 0:
            self.buttonB.config(state="disabled")
            self.text2.set("O")
            self.bottoneB_o = True
            self.cont_o()

    def changeText3(self):
        self.i += 1
        if self.i % 2 == 0:
            self.buttonC.config(state="disabled")
            self.text3.set("X")
            self.bottoneC_x = True
            self.cont_x()

        elif self.i % 2 != 0:
            self.buttonC.config(state="disabled")
            self.text3.set("O")
            self.bottoneC_o = True
            self.cont_o()

    def changeText4(self):
        self.i += 1
        if self.i % 2 == 0:
            self.buttonD.config(state="disabled")
            self.text4.set("X")
            self.bottoneD_x = True
            self.cont_x()


        elif self.i % 2 != 0:
            self.buttonD.config(state="disabled")
            self.text4.set("O")
            self.bottoneD_o = True
            self.cont_o()

    def changeText5(self):
        self.i += 1
        if self.i % 2 == 0:
            self.buttonE.config(state="disabled")
            self.text5.set("X")
            self.bottoneE_x = True
            self.cont_x()


        elif self.i % 2 != 0:
            self.buttonE.config(state="disabled")
            self.text5.set("O")
            self.bottoneE_o = True
            self.cont_o()

    def changeText6(self):
        self.i += 1
        if self.i % 2 == 0:
            self.buttonF.config(state="disabled")
            self.text6.set("X")
            self.bottoneF_x = True
            self.cont_x()


        elif self.i % 2 != 0:
            self.buttonF.config(state="disabled")
            self.text6.set("O")
            self.bottoneF_o = True
            self.cont_o()

    def changeText7(self):
        self.i += 1
        if self.i % 2 == 0:
            self.buttonG.config(state="disabled")
            self.text7.set("X")
            self.bottoneG_x = True
            self.cont_x()


        elif self.i % 2 != 0:
            self.buttonG.config(state="disabled")
            self.text7.set("O")
            self.bottoneG_o = True
            self.cont_o()

    def changeText8(self):
        self.i += 1
        if self.i % 2 == 0:
            self.buttonH.config(state="disabled")
            self.text8.set("X")
            self.bottoneH_x = True
            self.cont_x()


        elif self.i % 2 != 0:
            self.buttonH.config(state="disabled")
            self.text8.set("O")
            self.bottoneH_o = True
            self.cont_o()

    def changeText9(self):
        self.i += 1
        if self.i % 2 == 0:
            self.buttonI.config(state="disabled")
            self.text9.set("X")
            self.bottoneI_x = True
            self.cont_x()


        elif self.i % 2 != 0:
            self.buttonI.config(state="disabled")
            self.text9.set("O")
            self.bottoneI_o = True
            self.cont_o()


    def cont_x(self):       
        if self.bottoneA_x == True and self.bottoneB_x == True and self.bottoneC_x == True:
          self.buttonA.config(bg = "red")
          self.buttonB.config(bg = "red")
          self.buttonC.config(bg = "red")
          self.configurazione_bottoni()
          self.fine_gioco_x()

        elif self.bottoneD_x == True and self.bottoneE_x == True and self.bottoneF_x == True:
          self.buttonD.config(bg = "red")
          self.buttonE.config(bg = "red")
          self.buttonF.config(bg = "red")
          self.configurazione_bottoni()
          self.fine_gioco_x()

        elif self.bottoneG_x == True and self.bottoneH_x == True and self.bottoneI_x == True:
          self.buttonG.config(bg = "red")
          self.buttonH.config(bg = "red")
          self.buttonI.config(bg = "red")
          self.configurazione_bottoni()
          self.fine_gioco_x()


        elif self.bottoneA_x == True and self.bottoneD_x == True and self.bottoneG_x == True:
          self.buttonA.config(bg = "red")
          self.buttonD.config(bg = "red")
          self.buttonG.config(bg = "red")
          self.configurazione_bottoni()
          self.fine_gioco_x()


        elif self.bottoneB_x == True and self.bottoneE_x == True and self.bottoneH_x == True:
          self.buttonB.config(bg = "red")
          self.buttonE.config(bg = "red")
          self.buttonH.config(bg = "red")
          self.configurazione_bottoni()
          self.fine_gioco_x()


        elif self.bottoneC_x == True and self.bottoneF_x == True and self.bottoneI_x == True:
          self.buttonC.config(bg = "red")
          self.buttonF.config(bg = "red")
          self.buttonI.config(bg = "red")
          self.configurazione_bottoni()
          self.fine_gioco_x()


        elif self.bottoneA_x == True and self.bottoneE_x == True and self.bottoneI_x == True:
          self.buttonA.config(bg = "red")
          self.buttonE.config(bg = "red")
          self.buttonI.config(bg = "red")
          self.configurazione_bottoni()
          self.fine_gioco_x()


        elif self.bottoneC_x == True and self.bottoneE_x == True and self.bottoneG_x == True:
          self.buttonC.config(bg = "red")
          self.buttonE.config(bg = "red")
          self.buttonG.config(bg = "red")
          self.configurazione_bottoni()
          self.fine_gioco_x()


    def cont_o(self):
        if self.bottoneA_o == True and self.bottoneB_o == True and self.bottoneC_o == True:
          self.buttonA.config(bg = "red")
          self.buttonB.config(bg = "red")
          self.buttonC.config(bg = "red")
          self.configurazione_bottoni()
          self.fine_gioco_o()

        elif self.bottoneG_o == True and self.bottoneH_o == True and self.bottoneI_o == True:
          self.buttonD.config(bg = "red")
          self.buttonE.config(bg = "red")
          self.buttonF.config(bg = "red")
          self.configurazione_bottoni()
          self.fine_gioco_o()

        elif self.bottoneG_o == True and self.bottoneH_o == True and self.bottoneI_o == True:
          self.buttonG.config(bg = "red")
          self.buttonH.config(bg = "red")
          self.buttonI.config(bg = "red")
          self.configurazione_bottoni()
          self.fine_gioco_o()

        elif self.bottoneA_o == True and self.bottoneD_o == True and self.bottoneG_o == True:
          self.buttonA.config(bg = "red")
          self.buttonD.config(bg = "red")
          self.buttonG.config(bg = "red")
          self.configurazione_bottoni()
          self.fine_gioco_o()
        elif self.bottoneB_o == True and self.bottoneE_o == True and self.bottoneH_o == True:
          self.buttonB.config(bg = "red")
          self.buttonE.config(bg = "red")
          self.buttonH.config(bg = "red")
          self.configurazione_bottoni()
          self.fine_gioco_o()

        elif self.bottoneC_o == True and self.bottoneF_o == True and self.bottoneI_o == True:
          self.buttonC.config(bg = "red")
          self.buttonF.config(bg = "red")
          self.buttonI.config(bg = "red")
          self.configurazione_bottoni()
          self.fine_gioco_o()

        elif self.bottoneA_o == True and self.bottoneE_o == True and self.bottoneI_o == True:
          self.buttonA.config(bg = "red")
          self.buttonE.config(bg = "red")
          self.buttonI.config(bg = "red")
          self.configurazione_bottoni()
          self.fine_gioco_o()  
          
        elif self.bottoneC_o == True and self.bottoneE_o == True and self.bottoneG_o == True:
          self.buttonC.config(bg = "red")
          self.buttonE.config(bg = "red")
          self.buttonG.config(bg = "red")
          self.configurazione_bottoni()
          self.fine_gioco_o()

        elif self.i == 9:
          self.configurazione_bottoni()
          self.testo_pareggio = tk.StringVar()

          self.testo_pareggio = tk.Label(text="Avete pareggiato!!!", borderwidth=4, relief="groove", font="Helvetica", bg= "white")
          self.testo_pareggio.grid(column=4, row=3)

    
    def configurazione_bottoni(self):
        self.buttonA.config(state="disabled")
        self.buttonB.config(state="disabled")
        self.buttonC.config(state="disabled")
        self.buttonD.config(state="disabled")
        self.buttonE.config(state="disabled")
        self.buttonF.config(state="disabled")
        self.buttonG.config(state="disabled")
        self.buttonH.config(state="disabled")
        self.buttonI.config(state="disabled")

  
    def fine_gioco_o(self):
        self.testo_vitt_o = tk.StringVar()

        self.testo_vitt_o = tk.Label(text="Ha vinto il giocatore 1!!!", borderwidth=4, relief="groove", font="Helvetica", bg= "white")
        self.testo_vitt_o.grid(column=4, row=3)

    def fine_gioco_x(self):
        self.testo_vitt_x = tk.StringVar()

        self.testo_vitt_x = tk.Label(text="Ha vinto il giocatore 2!!!", borderwidth=4, relief="groove", font="Helvetica", bg= "white")
        self.testo_vitt_x.grid(column=4, row=3)

app = Menu()