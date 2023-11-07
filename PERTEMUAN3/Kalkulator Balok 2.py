import tkinter as tk 
from tkinter import Frame, Label, Entry, Button, END, W

def hitung_luas():
    Jari_jari = float(txtJari_jari.get())
   
    
    L = 4 * math.pi * Jari_jari

    txtLuas.delete(0, END)
    txtLuas.insert(END,L)

def hitung_Volume():
    Jari_jari  = float(txtJari_jari.get())
   
    V = 4/3 * math.pi * Jari_jari

    txtKeliling.delete(0,END)
    txtKeliling.insert(END,K)

def hitung():
    hitung_luas()
    hitung_keliling()

# Create tkinter object app = tk.Tk()
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulator Luas dan Volume Bola")

# Windows
frame = Frame(app) 
frame.pack(padx=20, pady=20)

# Label jari_jari
Jari_jari = Label(frame, text="Jari-jari:") 
Panjang.grid(row=0, column=0, sticky=W, padx=5, pady=5)


# Textbox Panjang
txtJari_jari = Entry(frame)
txtJari_jari.grid(row=0, column=1)


# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Output Label Luas
Luas = Label(frame, text="Luas: ")
Luas.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output label Volume
Volume = Label (frame, text="Volume: ")
Volume.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas
txtLuas = Entry(frame)
txtLuas.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtvolume = Entry (frame)
txtvolume.grid(row=5, column=1, sticky=W, padx=5, pady=5)

app.mainloop()