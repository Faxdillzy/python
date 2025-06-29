# variabel global untuk menyimpan data buku
buku = []

# fungsi untuk menampilkan semua data
def lihat_data():
    if len(buku) <= 0:
        print("belum ada data")
    else:
        for indeks, judul in enumerate(buku):
            print(f"{indeks}. {judul}")

# fungsi untuk menambah data
def insert_data():
    buku_baru = input("judul buku:")
    buku. append(buku_baru)
    print("data berhasil ditambahkan")

# fungsi untuk edit data
def edit_data():
    lihat_data()
    try:
        indeks = int(input("inputkan ID buku:"))
        if indeks < 0 or indeks >= len(buku):
            print("ID salah")
        else:
            judul_buku = input("judul buku baru:")
            buku[indeks] = judul_buku
            print("data berhasil diubah!")
    except ValueError:
        print("input tidak valid")

# fungsi untuk menghapus data
def delete_data():
    lihat_data()
    try:
        indeks = int(input("inputkan ID buku:"))
        if indeks < 0 or indeks >= len(buku):
            print("ID salah")
        else:
            buku.pop(indeks)
            print("data berhasil dihapus!")
    except ValueError:
        print("input tidak valid!")

# fungsi untuk menampilkan menu
def show_menu():
    print("\n---------- MENU ----------")
    print("[1] Show data")
    print("[2] Insert data")
    print("[3] Edit data")
    print("[4] Delete data")
    print("[5] Exit")

    try:
        menu = int(input("pilih menu>"))
        print()

        if menu == 1:
            lihat_data()
        elif menu == 2:
            insert_data()
        elif menu == 3:
            edit_data()
        elif menu == 4:
            delete_data()
        elif menu == 5:
            print("keluar dari program...")
            exit()
        else:
            print("menu tidak valid!")
    except ValueError:
        print("input tidak valid!")

if __name__ == "__main__":
    while True:
        show_menu()