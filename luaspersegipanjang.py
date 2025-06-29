# langkah 1 : meminta input dari pengguna
panjang = float(input("masukkan panjang persegi panjang:"))
lebar = float(input("masukkan lebar persegi panjang:"))

# langkah 2: meghitung luas dan keliling (menggunakan operand dan operator)
luas = panjang * lebar                  # operator perkalian
keliling = 2 * (panjang + lebar)        # operator penjumlahan dan perkalian

# langkah 3: menampilkan hasil perhitungan
print("luas persegi panjang adalah:", luas)
print("keliling persegi panjang adalah:", keliling)

# langkah 4: mengecek apakah luas lebih besar dari keliling (menggunakan operator relasional)
if luas > keliling:
    print("luas lebih besar dari keliling.")
else:
    print("keliling lebih besar atau sama dengan lain.")