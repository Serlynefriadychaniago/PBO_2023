# filename : FrmNota.py
import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Nota import Nota
# pip install tkcalendar
from tkcalendar import Calendar, DateEntry
class FormNota:   
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("1200x550")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        
        
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
        Label(mainFrame, text='NAMA USER :').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        # Textbox NAMA_USER
        self.txtNAMA_USER = Entry(mainFrame) 
        self.txtNAMA_USER.grid(row=0, column=1, padx=5, pady=5) 
        self.txtNAMA_USER.bind("<Return>",self.onCari) # menambahkan event Enter key
                
         # enum 
        Label(mainFrame, text='ID KOMPUTER :').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        # Combo Box
        self.txtID_KOMPUTER = StringVar()
        CboID_KOMPUTER = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtID_KOMPUTER) 
        CboID_KOMPUTER.grid(row=1, column=1, padx=5, pady=5)
        # Adding combobox drop down list
        CboID_KOMPUTER['values'] = ('PC01','PC02','PC03','PC04','PC05','PC06','PC07','PC08','PC09','PC10','PC11','PC12','PC13','PC14','PC15','PC16','PC17','PC18','PC19','PC20')
        CboID_KOMPUTER.current()
        
         # date 
        Label(mainFrame, text='TANGGAL :').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        # Date Input TANGGAL
        self.txtTANGGAL = DateEntry(mainFrame, width= 16, background= "magenta3", foreground= "white",bd=2, date_pattern='y-mm-dd') 
        self.txtTANGGAL.grid(row=2, column=1, padx=5, pady=5)
                    
         # varchar 
        Label(mainFrame, text='JAM MULAI :').grid(row=3, column=0, sticky=W, padx=5, pady=5)
        # Textbox JAM_MULAI
        self.txtJAM_MULAI = Entry(mainFrame) 
        self.txtJAM_MULAI.grid(row=3, column=1, padx=5, pady=5)
                
         # varchar 
        Label(mainFrame, text='JAM SELESAI :').grid(row=4, column=0, sticky=W, padx=5, pady=5)
        # Textbox JAM_SELESAI
        self.txtJAM_SELESAI = Entry(mainFrame) 
        self.txtJAM_SELESAI.grid(row=4, column=1, padx=5, pady=5)
                
         # varchar 
        Label(mainFrame, text='LAMA WAKTU :').grid(row=5, column=0, sticky=W, padx=5, pady=5)
        # Textbox LAMA_WAKTU
        self.txtLAMA_WAKTU = Entry(mainFrame) 
        self.txtLAMA_WAKTU.grid(row=5, column=1, padx=5, pady=5)
                
         # varchar 
        Label(mainFrame, text='TARIF PERJAM :').grid(row=6, column=0, sticky=W, padx=5, pady=5)
        # Textbox TARIF_PER_JAM
        self.txtTARIF_PER_JAM = Entry(mainFrame) 
        self.txtTARIF_PER_JAM.grid(row=6, column=1, padx=5, pady=5)
                
         # varchar 
        Label(mainFrame, text='TOTAL BAYAR :').grid(row=7, column=0, sticky=W, padx=5, pady=5)
        # Textbox TOTAL_BAYAR
        self.txtTOTAL_BAYAR = Entry(mainFrame) 
        self.txtTOTAL_BAYAR.grid(row=7, column=1, padx=5, pady=5)
                
         # enum 
        Label(mainFrame, text='STATUS BAYAR :').grid(row=8, column=0, sticky=W, padx=5, pady=5)
        # Combo Box
        self.txtSTATUS_BAYAR = StringVar()
        CboSTATUS_BAYAR = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtSTATUS_BAYAR) 
        CboSTATUS_BAYAR.grid(row=8, column=1, padx=5, pady=5)
        # Adding combobox drop down list
        CboSTATUS_BAYAR['values'] = ('TAGIHAN','LUNAS')
        CboSTATUS_BAYAR.current()
        
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        
        # define columns
        columns = ('ID','NAMA_USER','ID_KOMPUTER','TANGGAL','JAM_MULAI','JAM_SELESAI','LAMA_WAKTU','TARIF_PER_JAM','TOTAL_BAYAR','STATUS_BAYAR')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('ID', text='ID')
        self.tree.column('ID', width="30")
        self.tree.heading('NAMA_USER', text='NAMA USER')
        self.tree.column('NAMA_USER', width="100")
        self.tree.heading('ID_KOMPUTER', text='ID KOMPUTER')
        self.tree.column('ID_KOMPUTER', width="100")
        self.tree.heading('TANGGAL', text='TANGGAL')
        self.tree.column('TANGGAL', width="100")
        self.tree.heading('JAM_MULAI', text='JAM MULAI')
        self.tree.column('JAM_MULAI', width="100")
        self.tree.heading('JAM_SELESAI', text='JAM SELESAI')
        self.tree.column('JAM_SELESAI', width="100")
        self.tree.heading('LAMA_WAKTU', text='LAMA WAKTU')
        self.tree.column('LAMA_WAKTU', width="100")
        self.tree.heading('TARIF_PER_JAM', text='TARIF PERJAM')
        self.tree.column('TARIF_PER_JAM', width="100")
        self.tree.heading('TOTAL_BAYAR', text='TOTAL BAYAR')
        self.tree.column('TOTAL_BAYAR', width="100")
        self.tree.heading('STATUS_BAYAR', text='STATUS BAYAR')
        self.tree.column('STATUS_BAYAR', width="100")
        # set tree position
        self.tree.place(x=0, y=300)
        self.onReload()
    
    def onClear(self, event=None):
        self.txtNAMA_USER.delete(0,END)
        self.txtNAMA_USER.insert(END,"")
                                
        self.txtID_KOMPUTER.set("")
            
        self.txtJAM_MULAI.delete(0,END)
        self.txtJAM_MULAI.insert(END,"")
                                
        self.txtJAM_SELESAI.delete(0,END)
        self.txtJAM_SELESAI.insert(END,"")
                                
        self.txtLAMA_WAKTU.delete(0,END)
        self.txtLAMA_WAKTU.insert(END,"")
                                
        self.txtTARIF_PER_JAM.delete(0,END)
        self.txtTARIF_PER_JAM.insert(END,"")
                                
        self.txtTOTAL_BAYAR.delete(0,END)
        self.txtTOTAL_BAYAR.insert(END,"")
                                
        self.txtSTATUS_BAYAR.set("")
            
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data nota
        obj = Nota()
        result = obj.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        mylist=[]
        for row_data in result:
            mylist.append(row_data)
        for row in mylist:
            self.tree.insert('',END, values=row)
            
    def onCari(self, event=None):
        NAMA_USER = self.txtNAMA_USER.get()
        obj = Nota()
        res = obj.getByNAMA_USER(NAMA_USER)
        rec = obj.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            # self.txtNama.focus()
        return res
            
    def TampilkanData(self, event=None):
        NAMA_USER = self.txtNAMA_USER.get()
        obj = Nota()
        res = obj.getByNAMA_USER(NAMA_USER)
            
        self.txtID_KOMPUTER.set(obj.ID_KOMPUTER)
            
        self.txtTANGGAL.delete(0,END)
        self.txtTANGGAL.insert(END,obj.TANGGAL)
                                
        self.txtJAM_MULAI.delete(0,END)
        self.txtJAM_MULAI.insert(END,obj.JAM_MULAI)
                                
        self.txtJAM_SELESAI.delete(0,END)
        self.txtJAM_SELESAI.insert(END,obj.JAM_SELESAI)
                                
        self.txtLAMA_WAKTU.delete(0,END)
        self.txtLAMA_WAKTU.insert(END,obj.LAMA_WAKTU)
                                
        self.txtTARIF_PER_JAM.delete(0,END)
        self.txtTARIF_PER_JAM.insert(END,obj.TARIF_PER_JAM)
                                
        self.txtTOTAL_BAYAR.delete(0,END)
        self.txtTOTAL_BAYAR.insert(END,obj.TOTAL_BAYAR)
                                
        self.txtSTATUS_BAYAR.set(obj.STATUS_BAYAR)
            
        self.btnSimpan.config(text="Update")
    def onSimpan(self, event=None):
        NAMA_USER = self.txtNAMA_USER.get()
        ID_KOMPUTER = self.txtID_KOMPUTER.get()
        TANGGAL = self.txtTANGGAL.get()
        JAM_MULAI = self.txtJAM_MULAI.get()
        JAM_SELESAI = self.txtJAM_SELESAI.get()
        LAMA_WAKTU = self.txtLAMA_WAKTU.get()
        TARIF_PER_JAM = self.txtTARIF_PER_JAM.get()
        TOTAL_BAYAR = self.txtTOTAL_BAYAR.get()
        STATUS_BAYAR = self.txtSTATUS_BAYAR.get()       
        obj = Nota()
        obj.NAMA_USER = NAMA_USER
        obj.ID_KOMPUTER = ID_KOMPUTER
        obj.TANGGAL = TANGGAL
        obj.JAM_MULAI = JAM_MULAI
        obj.JAM_SELESAI = JAM_SELESAI
        obj.LAMA_WAKTU = LAMA_WAKTU
        obj.TARIF_PER_JAM = TARIF_PER_JAM
        obj.TOTAL_BAYAR = TOTAL_BAYAR
        obj.STATUS_BAYAR = STATUS_BAYAR
        if(self.ditemukan==True):
            res = obj.updateByNAMA_USER(NAMA_USER)
            ket = 'Diperbarui'
            
        else:
            res = obj.simpan()
            ket = 'Disimpan'
            
            
        rec = obj.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec
 
    def onDelete(self, event=None):
        NAMA_USER = self.txtNAMA_USER.get()
        obj = Nota()
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
    aplikasi = FormNota(root, "Aplikasi Data Nota")
    root.mainloop() 