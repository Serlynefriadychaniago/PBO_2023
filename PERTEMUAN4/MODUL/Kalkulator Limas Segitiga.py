import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W
from fungsi_ruang import l_limass,v_limass

def hitung_luas():
    luas_segitiga = float(txtluas_segitiga.get())
    luas_alas = float(txtluas_alas.get())

    luas= l_limass(luas_segitiga,luas_alas)

    txtluas.delete(0,END)
    txtluas.insert(END,luas)

def hitung_volume():
    tinggi_segitiga = float(txttinggi_segitiga.get())
    Tinggi_limas = float(txtTinggi_limas.get())
    luas_alas = float(txtluas_alas.get())

    volume= v_limass(tinggi_segitiga,Tinggi_limas,luas_alas)

    txtvolume.delete(0,END)
    txtvolume.insert(END,volume)

def hitung():
    hitung_luas()
    hitung_volume()

app = tk . Tk()
app.title("aplikasi mencari luas dan volume limas segitiga")

frame = Frame(app)
frame.pack(padx=20,pady=20)

#luas segitiga
luas_segitiga = Label(frame, text="luas segitiga:")
luas_segitiga.grid(row=0, column=0, sticky=W, padx=5, pady=5)

luas_alas = Label(frame, text="luas alas:")
luas_alas.grid(row=1, column=0, sticky=W, padx=5, pady=5)

tinggi_segitiga = Label(frame, text="tinggi segitiga:")
tinggi_segitiga.grid(row=2, column=0, sticky=W, padx=5, pady=5)

Tinggi_limas = Label(frame, text="Tinggi limas:")
Tinggi_limas.grid(row=3, column=0, sticky=W, padx=5, pady=5)

#textbox

txtluas_segitiga = Entry(frame)
txtluas_segitiga.grid(row=0, column=1, sticky=W, padx=5, pady=5)

txtluas_alas = Entry(frame)
txtluas_alas.grid(row=1, column=1, sticky=W, padx=5, pady=5)

txttinggi_segitiga = Entry(frame)
txttinggi_segitiga.grid(row=2, column=1, sticky=W, padx=5, pady=5)

txtTinggi_limas = Entry(frame)
txtTinggi_limas.grid(row=3, column=1, sticky=W, padx=5, pady=5)

#button
hitung_button = Button(frame, text="hitung:", command=hitung )
hitung_button.grid(row=4, column=0, sticky=W, padx=5, pady=5)

#label output
luas = Label(frame, text="luas:")
luas.grid(row=5, column=0, sticky=W, padx=5, pady=5)

volume = Label(frame, text="volume:")
volume.grid(row=6, column=0, sticky=W, padx=5, pady=5)

#textbox output

txtluas = Entry(frame)
txtluas.grid(row=5, column=1, sticky=W, padx=5, pady=5)

txtvolume = Entry(frame)
txtvolume.grid(row=6, column=1, sticky=W, padx=5, pady=5)

app.mainloop()










