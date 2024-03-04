# filename : FrmPelanggan.py
import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Pelanggan import Pelanggan
class FormPelanggan:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("1200x550")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        
        self.old_NAMA_USER = None  # Menambahkan variabel instance untuk menyimpan NAMA_USER sebelum pengeditan
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # Background
        background = "#448c9d"
        # Set background color
        mainFrame.configure(background=background)

         # varchar 
        Label(mainFrame, text='NAMA_USER:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        # Textbox NAMA_USER
        self.txtNAMA_USER = Entry(mainFrame) 
        self.txtNAMA_USER.grid(row=0, column=1, padx=5, pady=5) 
        self.txtNAMA_USER.bind("<Return>",self.onCari) # menambahkan event Enter key
                
         # enum 
        Label(mainFrame, text='JENIS_KELAMIN:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        # Combo Box
        self.txtJENIS_KELAMIN = StringVar()
        CboJENIS_KELAMIN = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtJENIS_KELAMIN) 
        CboJENIS_KELAMIN.grid(row=1, column=1, padx=5, pady=5)
        # Adding combobox drop down list
        CboJENIS_KELAMIN['values'] = ('PEREMPUAN','LAKI-LAKI')
        CboJENIS_KELAMIN.current()
        
         # varchar 
        Label(mainFrame, text='EMAIL:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        # Textbox EMAIL
        self.txtEMAIL = Entry(mainFrame) 
        self.txtEMAIL.grid(row=2, column=1, padx=5, pady=5)
                
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        
        # define columns
        columns = ('ID','NAMA_USER','JENIS_KELAMIN','EMAIL')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('ID', text='ID')
        self.tree.column('ID', width="30")
        self.tree.heading('NAMA_USER', text='NAMA_USER')
        self.tree.column('NAMA_USER', width="200")
        self.tree.heading('JENIS_KELAMIN', text='JENIS_KELAMIN')
        self.tree.column('JENIS_KELAMIN', width="200")
        self.tree.heading('EMAIL', text='EMAIL')
        self.tree.column('EMAIL', width="200")
        # set tree position
        self.tree.place(x=0, y=150)
        self.onReload()
    
    def onClear(self, event=None):
        self.txtNAMA_USER.delete(0,END)
        self.txtNAMA_USER.insert(END,"")
                                
        self.txtJENIS_KELAMIN.set("")
            
        self.txtEMAIL.delete(0,END)
        self.txtEMAIL.insert(END,"")
                                
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data pelanggan
        obj = Pelanggan()
        result = obj.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        mylist=[]
        for row_data in result:
            mylist.append(row_data)
        for row in mylist:
            self.tree.insert('',END, values=row)
        
        # Menampilkan NAMA_USER baru setelah pengupdatean
        if self.ditemukan:
            NAMA_USER = self.txtNAMA_USER.get()
            for item in self.tree.get_children():
                if self.tree.item(item)['values'][1] == NAMA_USER:
                    self.tree.selection_set(item)
                    break
            
    def onCari(self, event=None):
        NAMA_USER = self.txtNAMA_USER.get()
        obj = Pelanggan()
        res = obj.getByNAMA_USER(NAMA_USER)
        rec = obj.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.old_NAMA_USER = NAMA_USER  # Menyimpan NAMA_USER sebelum pengeditan
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            # self.txtNama.focus()
        return res
    def TampilkanData(self, event=None):
        NAMA_USER = self.txtNAMA_USER.get()
        obj = Pelanggan()
        res = obj.getByNAMA_USER(NAMA_USER)
            
        self.txtJENIS_KELAMIN.set(obj.JENIS_KELAMIN)
            
        self.txtEMAIL.delete(0,END)
        self.txtEMAIL.insert(END,obj.EMAIL)
                                
        self.btnSimpan.config(text="Update")

    def onSimpan(self, event=None):
        NAMA_USER = self.txtNAMA_USER.get()
        JENIS_KELAMIN = self.txtJENIS_KELAMIN.get()
        EMAIL = self.txtEMAIL.get()       
        obj = Pelanggan()
        obj.NAMA_USER = NAMA_USER
        obj.JENIS_KELAMIN = JENIS_KELAMIN
        obj.EMAIL = EMAIL

        # Memeriksa apakah NAMA_USER berubah
        if self.ditemukan:
            if NAMA_USER != self.old_NAMA_USER:
                # Jika NAMA_USER berubah, lakukan pengupdatean untuk NAMA_USER lama dan baru
                res = obj.updateByNAMA_USER(self.old_NAMA_USER)
                res2 = obj.simpan()
            else:
                # Jika NAMA_USER tidak berubah, lakukan pengupdatean seperti biasa
                res = obj.updateByNAMA_USER(NAMA_USER)
            ket = 'Diperbarui'
        else:
            res = obj.simpan()
            ket = 'Disimpan'
            
        rec = obj.affected
        if(rec > 0):
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec
 
    def onDelete(self, event=None):
        NAMA_USER = self.txtNAMA_USER.get()
        obj = Pelanggan()
        obj.NAMA_USER = NAMA_USER
        if(self.ditemukan==True):
            res = obj.deleteByNAMA_USER(NAMA_USER)
            rec = obj.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()
 
 
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = FormPelanggan(root, "Aplikasi Data Pelanggan")
    root.mainloop() 