print("Mencari Luas dan Volume Prisma Segitiga")

#variabel
Alas_segitiga = 4
Tinggi_segitiga = 4
tinggi_prisma = 4

#rumus prisma segitiga
Luas_segitiga = (1/2) * Alas_segitiga * Tinggi_segitiga
Luas_prisma = (2 * Alas_segitiga * Tinggi_segitiga) + (3 * Alas_segitiga * tinggi_prisma)
volume_prisma = Luas_segitiga * tinggi_prisma

#output
print("Luas prisma :", Luas_prisma)
print("volume prisma:", volume_prisma)