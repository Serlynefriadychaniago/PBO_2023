print("Mencari Luas dan Volume Kerucut")

#output
import math
jari_jari = 8
tinggi = 16

# Fungsi untuk menghitung luas permukaan kerucut
garis_miring = math.sqrt(jari_jari**2 + tinggi**2)
luas_permukaan = math.pi * jari_jari * (jari_jari + garis_miring)

# Fungsi untuk menghitung volume kerucut
volume = (1/3) * math.pi * jari_jari**2 * tinggi

#output
print('hasil dari mencari luas kerucut dengan\njari_jari : ',jari_jari,'\ntinggi : ',tinggi,'\nadalah = ', luas_permukaan )
print('\nhasil dari mencari volume kerucut dengan\njari_jari : ',jari_jari,'\ntinggi : ',tinggi,'\nadalah = ', volume )