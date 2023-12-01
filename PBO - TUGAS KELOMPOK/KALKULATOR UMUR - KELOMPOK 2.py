import flet as ft

def main(page: ft.Page):
    page.title = "Calculator Usia"

    def btn_click(e):
        tahun_sekarang.value = int(tahun_sekarang.value)
        tahun_kelahiran.value = int(tahun_kelahiran.value)
        if not tahun_sekarang.value:
            tahun_sekarang.error_text = "Mohon masukkan nilai!"
            page.update()
        else:
            rumus = tahun_sekarang.value - tahun_kelahiran.value
            if tahun_kelahiran.value > 0 and tahun_kelahiran.value <= 2023:
                dlg = ft.AlertDialog(
                    title=ft.Text(f"Hello,Usia mu sekarang {rumus} TH !"), on_dismiss=lambda e: print("Dialog dismissed!"))
                page.dialog = dlg
                dlg.open = True
                page.update()
            else:
                tahun_kelahiran.error_text = "Masukkan Tahun Kelahiran dari 1800-2023 !"
                page.update()

    tahun_sekarang = ft.TextField(label="Tahun sekarang")
    tahun_kelahiran = ft.TextField(label="Tahun Kelahiran")

    page.add(tahun_sekarang, tahun_kelahiran, ft.ElevatedButton("Hitung!", on_click=btn_click))

ft.app(main)