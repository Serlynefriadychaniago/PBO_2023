from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W

class FrmLimasEmpat:
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
        Label(mainFrame, text='Sisi:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Tinggi Limas:").grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Tinggi Segitiga:").grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas:").grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Volume:").grid(row=5, column=0,
            sticky=W, padx=5, pady=5)

        # pasang textbox
        self.txtSisi = Entry(mainFrame) 
        self.txtSisi.grid(row=0, column=1, padx=5, pady=5)  
        self.txtTinggiLimas = Entry(mainFrame) 
        self.txtTinggiLimas.grid(row=1, column=1, padx=5, pady=5) 
        self.txtTinggiSegitiga = Entry(mainFrame) 
        self.txtTinggiSegitiga.grid(row=2, column=1, padx=5, pady=5) 
        self.txtLuas = Entry(mainFrame) 
        self.txtLuas.grid(row=4, column=1, padx=5, pady=5) 
        self.txtVolume = Entry(mainFrame) 
        self.txtVolume.grid(row=5, column=1, padx=5, pady=5) 
        
        
        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung)
        self.btnHitung.grid(row=3, column=1, padx=5, pady=5)
        
           
    # fungsi "onHitung" berfungsi untuk menghitung luas persegi panjang  
    def onHitung(self, event=None):
        sisi = int(self.txtSisi.get())
        tinggilimas = int(self.txtTinggiLimas.get())
        tinggisegitiga = int(self.txtTinggiSegitiga.get())                  
        luas = (sisi*sisi)+(4*sisi*tinggisegitiga/2)
        volume = 1/3*(sisi*sisi)*tinggilimas
        self.txtLuas.delete(0,END)
        self.txtLuas.insert(END,str(luas))
        self.txtVolume.delete(0,END)
        self.txtVolume.insert(END,str(volume))
               
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmLimasEmpat(root, "Program Luas dan Volume Limas Segiempat")
    root.mainloop() 