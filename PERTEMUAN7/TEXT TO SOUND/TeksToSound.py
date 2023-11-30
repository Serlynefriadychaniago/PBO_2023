import tkinter as tk
from gtts import gTTS
from playsound import playsound
from io import BytesIO
import tempfile
from PIL import Image, ImageTk

class TextToSpeechApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Text to Speech")
        self.master.geometry("400x300")
        self.master.configure(bg='#D2B48C')

        self.label = tk.Label(self.master, text="Masukkan Teks:", font=("Helvetica", 14), bg='#D2B48C', fg='white')
        self.label.pack(pady=10)

        self.text_entry = tk.Entry(self.master, width=40, font=("Helvetica", 12))
        self.text_entry.pack(pady=10)

        self.speak_button = tk.Button(self.master, text="Bicara", command=self.speak_text, bg='#8B4513', fg='white', padx=20, pady=10)
        self.speak_button.pack(pady=20)

    def speak_text(self):
        text = self.text_entry.get()
        if text:
            language = 'id'  # Ganti dengan kode bahasa yang sesuai
            tts = gTTS(text=text, lang=language, slow=False)

            # Simpan suara dalam file temporary
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
                tts.write_to_fp(temp_file)
            
            # Mainkan suara dari file temporary
            playsound(temp_file.name)

def main():
    root = tk.Tk()
    app = TextToSpeechApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
