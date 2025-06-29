import random # modul ini digunakan untuk menghasilkan angka acak dari daftar
import datetime # modul ini digunakan untul meghasilkan waktu saat ini

def simulasi_cuaca():

    # daftar pilihan untuk setiap parameter cuaca 
    hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    cuaca = ["Cerah", "Berawan", "Hujan Ringan", "Hujan Deras", "Badai Petir"]
    suhu_celcius = random.randint(20, 40)
    # suhu dalam derajat celcius yang menghasilkan angka 20 sampai 40 derajat celcius
    kelembapan = random.randint(50, 90)
    # kelembapan dengan angka acak antara 50 sampai 90 persen

    # konversi suhu celcius ke fahrenheit
    suhu_fahrenheit = (suhu_celcius * 9/5) + 32

    # membuat data cuaca
    '''
    random.choice digunakan untuk memilih secara acak satu elemen dari daftar hari dan cuaca sedangkan datetime.dateime.now()
    digunakan untuk mendapatkan waktu saat ini.
    '''
    data_cuaca = {
        "Hari": random.choice(hari),
        "Cuaca": random.choice(cuaca),
        "Suhu_Celcius": suhu_celcius,
        "Suhu_Fahrenheint": suhu_fahrenheit,
        "Kelembapan": kelembapan,
        "Waktu": datetime.datetime.now()
    }

    return data_cuaca

def tampilkan_cuaca(data_cuaca):
    '''
    fungsi untuk menampilkan informasi cuaca dalam
    format yang sudah dibaca. menerima data cuaca sebagai input.
    '''
    print("=== Simulasi Cuaca ===")
    print(f"Hari\t\t: {data_cuaca['Hari']}")
    print(f"Cuaca\t\t: {data_cuaca['Cuaca']}")
    print(f"Suhu\t\t: {data_cuaca['Suhu_Celcius']} derajat / {data_cuaca['Suhu_Fahrenheint']:.2f} derajat F")
    print(f"Kelembapan\t: {data_cuaca['Kelembapan']}%")
    print(f"Waktu\t\t: {data_cuaca['Waktu'].strftime('%Y-%m-%d %H:%M:%S')}")

    # prediksi cuaca selajutnya
    if data_cuaca['Cuaca'] == "Hujan Lebat":
        print("Pekiraan\t: Hujan akan terus berlanjut selama beberapa jam.")
    elif data_cuaca['Cuaca'] == "Badai Petir":
        print("Perkiraan\t: Badai petir diperkiraan akan mereda sekitar 1 - 2 jam.")
    else:
        print("Perkiraan\t: Cuaca diperkirakan stabil.")

data_cuaca = simulasi_cuaca()
tampilkan_cuaca(data_cuaca)