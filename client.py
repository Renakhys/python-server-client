import socket
import tkinter as tk

HOST = '127.0.0.1'  
PORT = 1300         

# crea una socket da usare come client
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# crea una connessione all'ip e la porta specificati
# HOST e PORT devono essere uguali per client e server
s.connect((HOST, PORT))

def button_click():
  # invia sulla socket connessa al server il testo contenuto nella casella di testo 
  # e.get() ritona il testo come stringa
  # bisogna chiamare .encode() per trasformarlo in byte grezzi altrimenti non si può inviare
  s.sendall(e.get().encode())

# crea la finestra con un pulsante e una casella di testo
root = tk.Tk()
root.geometry("200x200")
# casella di testo
e = tk.Entry()
e.pack()
# pulsante. quando viene premuto si chiama la funzione button_click
b = tk.Button(text ="Invia dati", command = button_click)
b.pack()
# apre la finestra
root.mainloop()
# dopo che la finestra viene chiusa termina la connessione con il server
s.close()
