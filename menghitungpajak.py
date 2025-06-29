# program untuk menhitung total harga setelah pajak

# meminta input dari pengguna
harga_barang = float(input("masukkan harga barang:"))
persentase_pajak = float(input("masukkan persentase pajak (dalam %):"))

# menghitung total harga setelah pajak
pajak = (persentase_pajak / 100) * harga_barang
total_harga = harga_barang + pajak

# menampilkan hasil
print(f"total harga setelah pajak adalah: {total_harga:.2f}")