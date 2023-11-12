import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W
from fungsi_ruang import l_prisma, v_prisma

def hitung_luas():
    Alas_segitiga = float(txtAlas_segitiga.get())
    Tinggi_alas = float(txtTinggi_alas.get())
    tinggi_prisma = float(txttinggi_prisma.get())

    luas = l_prisma(Alas_segitiga,Tinggi_alas,tinggi_prisma)
    
    txtluas.delete(0,END)
    txtluas.insert(END,luas)

def hitung_volume():
    Alas_segitiga = float(txtAlas_segitiga.get())
    Tinggi_alas = float(txtTinggi_alas.get())
    tinggi_prisma = float(txttinggi_prisma.get())

    volume = v_prisma(Alas_segitiga,Tinggi_alas,tinggi_prisma)
    txtvolume.delete(0,END)
    txtvolume.insert(END,volume)

def hitung():
    hitung_luas()
    hitung_volume()

app = tk.Tk()
app.title (" kalkulator prisma segitiga")

frame = Frame(app)
frame.pack(padx=20, pady=20)

#label
Alas_segitiga=Label(frame, text="Alas segitiga:")
Alas_segitiga.grid(row=0, column=0,sticky=W, padx=5, pady=5)

Tinggi_alas = Label(frame, text="Tinggi alas:")
Tinggi_alas.grid(row=1, column=0, sticky=W, padx=5, pady=5)

tinggi_prisma = Label(frame, text="tinggi prisma:")
tinggi_prisma.grid(row=2, column=0, sticky=W, padx=5, pady=5)

#outputlabel
txtAlas_segitiga = Entry(frame)
txtAlas_segitiga.grid(row=0, column=1, sticky=W, padx=5, pady=5)

txtTinggi_alas = Entry(frame)
txtTinggi_alas.grid(row=1, column=1, sticky=W, padx=5, pady=5)

txttinggi_prisma = Entry(frame)
txttinggi_prisma.grid(row=2, column=1, sticky=W, padx=5, pady=5)

#button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=3, column=0, sticky=W, padx=5, pady=5)

#label output
luas = Label (frame, text="luas:")
luas.grid(row=4, column=0, sticky=W, padx=5, pady=5)

volume = Label (frame, text="volume:")
volume.grid(row=5, column=0, sticky=W, padx=5, pady=5)

#txt output

txtluas = Entry(frame)
txtluas.grid(row=4, column=1, sticky=W, padx=5, pady=5)

txtvolume = Entry(frame)
txtvolume.grid(row=5, column=1, sticky=W, padx=5, pady=5)

app.mainloop()



    


