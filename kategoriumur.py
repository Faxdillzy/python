# meminta input umur dari pengguna
umur = int(input("masukkan umur anda: "))

# menentukan kategori umur
if umur < 0:
    kategori = "umur tidak valid"
elif umur <= 12:
    kategori = "Anak-anak"
elif umur <= 17:
    kategori = "Remaja"
elif umur <= 64:
    kategori = "Dewasa"
else:
    kategori = "Lansia"

# Menampilkan kategori umur
print(f"Kategori umur Anda adalah: {kategori}")