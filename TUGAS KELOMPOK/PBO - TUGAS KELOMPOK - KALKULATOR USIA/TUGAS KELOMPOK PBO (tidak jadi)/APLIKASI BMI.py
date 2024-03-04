import flet as ft

def main(page: ft.Page):
    page.title = "Kalkulator BMI"

    def button(e):
        try:
            berat = float(berat_badan.value)
            tinggi = float(tinggi_badan.value) / 100  # Mengubah tinggi ke meter
            bmi = berat / (tinggi ** 2)

            if berat <= 0:
                berat_badan.error_text = "Berat dan tinggi harus lebih dari 0."                
                page.update()
            elif tinggi * 100 <= 0:
                tinggi_badan.error_text = "Berat dan tinggi harus lebih dari 0."
                page.update()
            else:
                if bmi < 18.5:
                    hasil = "Kurus"
                elif 18.5 <= bmi < 24.9:
                    hasil = "Normal"
                elif 24.9 <= bmi < 29.9:
                    hasil = "Gemuk"
                else:
                    hasil = "Obesitas"
                
                # berat_badan.error_text = ""
                # hasil_label.value = f"BMI Anda: {bmi:.2f}\nKategori: {hasil}"
                
                page.add(ft.Text(f"BMI Anda: {bmi:.2f}\nKategori: {hasil}"))
                
        except ValueError:
            berat_badan.error_text = "Masukkan berat dan tinggi yang valid."

    berat_badan = ft.TextField(label="Berat badan (kg)")
    tinggi_badan = ft.TextField(label="Tinggi badan (cm)")
    hasil_label = ft.Text()

    page.add(berat_badan, tinggi_badan, ft.ElevatedButton("Hitung", on_click=button), hasil_label)

if __name__ == "__main__":
    ft.app(target=main)
