import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W
import math

def hitung_luas():
    sisi_sisi = float(txtsisi_sisi.get())
    sisi_sisi  = float(txtsisi_sisi.get())

    luas = 3 * sisi_sisi 

    txtLuas.delete(0, END)
    txtLuas.insert(END, luas)

def hitung_volume():
    sisi_sisi = float(txtsisi_sisi.get())

    Volume =  sisi_sisi * sisi_sisi * sisi_sisi

    txtVolume.delete(0,END)
    txtVolume.insert(END, Volume)

def hitung():
    hitung_luas()
    hitung_volume()

app = tk . Tk()
app.title ("Kalkulator Mencari Luas dan Volume kubus")

frame = Frame (app)
frame.pack(padx=20, pady=20)

#panjang
sisi_sisi = Label (frame, text="Sisi:")
sisi_sisi.grid(row=0, column=0, sticky=W, padx=5, pady=5)

#textbox panjang
txtsisi_sisi = Entry(frame)
txtsisi_sisi.grid(row=0, column=1,  sticky=W, padx=5, pady=5)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Output Label Luas
luas= Label(frame, text="Luas: ")
luas.grid(row=3, column=0, sticky=W, padx=5, pady=5)


volume = Label (frame, text="Volume: ")
volume.grid(row=4, column=0, stick=W, padx=5, pady=5)

# Output Textbox Luas
txtLuas = Entry(frame)
txtLuas.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Textbox volume
txtVolume = Entry (frame)
txtVolume.grid(row=4, column=1, sticky=W, padx=5, pady=5)

app.mainloop()