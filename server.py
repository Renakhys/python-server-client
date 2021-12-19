import socket
import tkinter as tk
from threading import Thread

HOST = '127.0.0.1'
PORT = 1300

# funzione di gestione del server
def run_server(s, label):
  # collega la socket ad un indirizzo ip e una porta
  # 127.0.0.1 -> significa questo computer
  s.bind((HOST, PORT))

  # si mette in ascolto per vedere se c'è qualche client che si connette
  s.listen()

  while 1:
    # finchè il server è in esecuzione continua ad accettare connessioni
    try:
      # attende la connessione di un client
      # conn è la connessione
      # ip è l'indirizzo del client 
      # port è la porta del client
      conn, addr = s.accept()
      label["text"] = "Connesso, attesa dati"
      print('client connesso', addr)

      # continua a ricevere i dati fino a quando il client non si disconnette
      while 1:
          # attese di 1024 byte di dati. il programma rimane bloccato in questo punto fino a quando non si
          # ricevono dati oppure la connessione viene chiusa
          # visto che il server gira su un thread a parte non è un problema, nel caso girasse sullo stesso thread
          # dell'interfaccia grafica la finestra smette di rispondere fino a quando non si ricevono dati
          data = conn.recv(1024)

          # se il client si è disconnesso si esce dal while
          if not data: break

          # aggiorna la label nell'interfaccia grafica con i dati ricevuti
          label["text"] = data
      conn.close()
      label["text"] = "Disconnesso, attesa di una nuova connessione"
      print('client disconnesso')
    except:
      # c'è stato un errore, ad esempio è stato chiamato close sulla socket del server mentre era in attesa di nuove connessioni
      print('server terminato')
      # esce dal while dove continua ad accettare connessioni
      break



# creazione della finestra con un testo
root = tk.Tk()
root.geometry("300x200")
label = tk.Label(text="attesa connessione")
label.pack()

# crea una socket su cui mettere in ascolto il server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# crea un thread su cui eseguire il server
t = Thread(target=run_server, args=(server, label, ))
t.start() 

# fa partire l'interfaccia grafica. esce da questa funzione quando la finestra viene chiusa
root.mainloop()

# dopo che la finestra viene chiusa chiude la socket del server
server.close()

# aspetta che il thread si chiuda
t.join()