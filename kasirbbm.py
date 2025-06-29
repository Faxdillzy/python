def kasir_bbm():

    # daftar harga per liter untuk setiap jenis BBM
    harga_pertalite = 10000
    harga_pertamax = 12000
    harga_solar = 6800
    harga_pertamax_turbo = 15000

    # menampilkan pilihan jeni BBM
    print("|------------------------------------|")
    print("|             Pilihan Jenis BBM      |")
    print("|------------------------------------|")
    print("|1. Pertalite (Rp 10.000/liter)      |")
    print("|2. Pertamax (Rp 12.000/liter)       |")
    print("|3. Solar (Rp6.800/liter)            |")
    print("|4. Petamax Tubo (Rp 15.000/liter)   |")
    print("|------------------------------------|\n")

    # meminta input nama pembeli
    nama_pembeli = input("Masukkan nama pembeli: ")

    # meminta input pilihan jenis BBM
    pilihan_bbm = input("Masukkan pilihan jenis BBM (1/2/3/4): ")

    # meminta input jumlah liter
    jumlah_liter = float(input("Masukkan jumlah liter: "))

    # menghitung total harga berdasarkan pilihan jenis BBM
    if pilihan_bbm == "1":
        jenis_bbm = "Pertalite"
        harga_per_liter = harga_pertalite
    elif pilihan_bbm == "2":
        jenis_bbm = "Pertamax"
        harga_per_liter = harga_pertamax
    elif pilihan_bbm == "3":
        jenis_bbm = "Solar"
        harga_per_liter = harga_solar
    elif pilihan_bbm == "4":
        jenis_bbm = "Pertamax Tubo"
        harga_per_liter = harga_pertamax_turbo
    else:
        print("Pilihan tidak valid.")
        return
    
    total_harga = harga_per_liter * jumlah_liter
    print("\n--- Struk Pembelian BBM ---")
    print(f"Nama Pembeli: {nama_pembeli}")
    print(f"Jenis BBM: {jenis_bbm}")
    print(f"Harga per Liter: Rp {harga_per_liter:,.0f}")
    print(f"Jumlah Liter: {jumlah_liter:.2f} liter")
    print(f"Total Harga: Rp {total_harga:,.0f}")
    print("-----------------------------")

# memanggil fungsi kasir_bbm
kasir_bbm()