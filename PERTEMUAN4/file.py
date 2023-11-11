# open a file

teks = "SAYA MAHASISWA UNIVERSITAS MUHAMMADIYAH CIREBON"

# write the file


# add teks the file
with open ("test.txt", "a") as file1:
    file1.write(teks)

# close the file
file1.close()

with open("test.txt", "r") as file2:
    read_content = file2.read()
    print(read_content)

# close the file
file2.close()