from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W

class FrmPrisma:
    def __init__(self, parent, title):
        self.parent = parent       
        #self.parent.geometry("400x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # pasang Label
        Label(mainFrame, text='Alas:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Tinggi:").grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Tinggi Prisma:").grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Sisi1:").grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Sisi2:").grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Sisi3:").grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas Alas:").grid(row=7, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas Sisi:").grid(row=8, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Volume:").grid(row=9, column=0,
            sticky=W, padx=5, pady=5)

        # pasang textbox
        self.txtAlas = Entry(mainFrame) 
        self.txtAlas.grid(row=0, column=1, padx=5, pady=5)  
        self.txtTinggi = Entry(mainFrame) 
        self.txtTinggi.grid(row=1, column=1, padx=5, pady=5) 
        self.txtTinggiPrisma = Entry(mainFrame) 
        self.txtTinggiPrisma.grid(row=2, column=1, padx=5, pady=5) 
        self.txtSisi1 = Entry(mainFrame) 
        self.txtSisi1.grid(row=3, column=1, padx=5, pady=5)
        self.txtSisi2 = Entry(mainFrame) 
        self.txtSisi2.grid(row=4, column=1, padx=5, pady=5)
        self.txtSisi3 = Entry(mainFrame) 
        self.txtSisi3.grid(row=5, column=1, padx=5, pady=5)
        self.txtLuasAlas = Entry(mainFrame) 
        self.txtLuasAlas.grid(row=7, column=1, padx=5, pady=5)
        self.txtLuasSisi = Entry(mainFrame) 
        self.txtLuasSisi.grid(row=8, column=1, padx=5, pady=5)
        self.txtVolume = Entry(mainFrame) 
        self.txtVolume.grid(row=9, column=1, padx=5, pady=5)
        
        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung)
        self.btnHitung.grid(row=6, column=1, padx=5, pady=5)
        
           
    # fungsi "onHitung" berfungsi untuk menghitung luas persegi panjang  
    def onHitung(self, event=None):
        alas = int(self.txtAlas.get())
        tinggi = int(self.txtTinggi.get())
        tinggiprisma = int(self.txtTinggiPrisma.get())
        sisi1 = int(self.txtSisi1.get())
        sisi2 = int(self.txtSisi2.get())
        sisi3 = int(self.txtSisi3.get())
        LuasAlas = (sisi1 + sisi2 + sisi3) * tinggiprisma
        LuasSisi = (sisi1 + sisi2 + sisi3) * tinggiprisma + alas * tinggi
        volume = (alas * tinggi) / 2 * tinggiprisma
        self.txtLuasAlas.delete(0,END)
        self.txtLuasAlas.insert(END,str(LuasAlas))
        self.txtLuasSisi.delete(0,END)
        self.txtLuasSisi.insert(END,str(LuasSisi))
        self.txtVolume.delete(0,END)
        self.txtVolume.insert(END,str(volume))

               
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmPrisma(root, "Program Luas Alas, Luas Sisi dan Volume ")
    root.mainloop() 