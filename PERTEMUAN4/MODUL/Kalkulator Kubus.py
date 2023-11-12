import tkinter as tk 
from tkinter import Frame, Label, Entry, Button, END, W
from fungsi_ruang import Luaskubus,Volumekubus

def hitung_luas():
    sisi = float(txtsisi.get())

    L = Luaskubus(sisi)

    txtLuas.delete(0, END)
    txtLuas.insert(END,L)

def hitung_volume():
    sisi = float(txtsisi.get())

    v = Volumekubus(sisi)

    txtvolume.delete(0,END)
    txtvolume.insert(END,v)

def hitung():
    hitung_luas()
    hitung_volume()

# Create tkinter object app = tk.Tk()
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulator Luas dan Volume Kubus")

# Windows
frame = Frame(app) 
frame.pack(padx=20, pady=20)

# Label Panjang
sisi = Label(frame, text="Rusuk:") 
sisi.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Textbox Rusuk
txtsisi = Entry(frame)
txtsisi.grid(row=0, column=1)


# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=2, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
Luas = Label(frame, text="Luas: ")
Luas.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Output label Keliling
volume = Label (frame, text="volume: ")
volume.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas
txtLuas = Entry(frame)
txtLuas.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Keliling
txtvolume = Entry (frame)
txtvolume.grid(row=4, column=1, sticky=W, padx=5, pady=5)

app.mainloop()