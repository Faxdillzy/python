import calendar

def tampilkan_kalender(tahun, bulan):
    # Membuat objek TextCalendar
    kal = calendar.TextCalendar()
    
    # Menampilkan kalender untuk bulan dan tahun yang diberikan
    kalender_bulan = kal.formatmonth(tahun, bulan)
    print(kalender_bulan)

# Input tahun dan bulan dari pengguna
tahun = int(input("Masukkan tahun (misal: 2023): "))
bulan = int(input("Masukkan bulan (1-12): "))

# Menampilkan kalender
tampilkan_kalender(tahun, bulan)
