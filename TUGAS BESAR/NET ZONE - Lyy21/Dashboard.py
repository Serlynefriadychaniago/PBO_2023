import tkinter as tk
from tkinter import Frame, Label, Button, Menu, messagebox
from PIL import Image, ImageTk

from FrmUsers import FormLogin
from FrmPelanggan import FormPelanggan
from FrmNota import FormNota

class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Dashboard")
        self.root.geometry("1400x1000")
        self.logged_in = False
        self.login_success_message = "Welcome!"  # Menyimpan pesan login berhasil

        # Creating a menu bar
        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)
        
        # Login menu
        self.login_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.login_menu.add_command(label="Login", command=self.open_login_form)
        self.menu_bar.add_cascade(label="Login", menu=self.login_menu)

        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Pelanggan", command=self.pelanggan)
        self.file_menu.add_command(label="Nota", command=self.nota)
        self.file_menu.add_command(label="Exit", command=root.quit)
        self.menu_bar.add_cascade(label="Menu", menu=self.file_menu)

        # Image Label
        self.image_label = Label(root)
        self.image_label.pack(fill="both", expand=True)
        self.image_label.bind("<Configure>", self.update_image)  # Panggil fungsi saat jendela diubah ukurannya


    def pelanggan(self):
        if self.logged_in:
            top_level = tk.Toplevel(self.root)
            pelanggan = FormPelanggan(top_level, "Pelanggan")  # Pass the title
        else:
            messagebox.showerror("Access Denied", "Please log in first.")

    def nota(self):
        if self.logged_in:
            top_level = tk.Toplevel(self.root)
            nota = FormNota(top_level, "Nota")  # Pass the title
        else:
            messagebox.showerror("Access Denied", "Please log in first.")

    def open_login_form(self):
        top_level = tk.Toplevel(self.root)
        login_form = FormLogin(top_level, "Login Form", self.login_callback)

    def login_callback(self, result):
        if result[1]:  # If login successful
            self.logged_in = True
            # Menampilkan pesan login berhasil hanya di form login
            messagebox.showinfo("Login Successful", self.login_success_message)
        else:
            messagebox.showerror("Login Failed", "Invalid credentials. Please try again.")

    def update_image(self, event):
        # Fungsi untuk memperbarui tampilan gambar
        lebar_jendela = event.width
        tinggi_jendela = event.height
        gambar = Image.open('NET ZONE - LYY.png')  # Ganti dengan path gambar Anda
        resized = gambar.resize((lebar_jendela, tinggi_jendela), Image.BILINEAR)  # Menggunakan BILINEAR sebagai interpolasi
        photo = ImageTk.PhotoImage(resized)
        self.image_label.configure(image=photo)
        self.image_label.image = photo

if __name__ == "__main__":
    root = tk.Tk()
    dashboard = Dashboard(root)
    root.mainloop()
