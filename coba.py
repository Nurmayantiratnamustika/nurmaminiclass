//contoh
def tampilkan_menu(nama,umur):
    print "================"
    print " SELAMAT DATANG " +nama+ " umur saya " +str(umur)
    print "Aplikasi Hitung Luas"
    print "================="
    print "Pilihan: "
    print "1. Luas Segitiga "
    print "2. Luas Persegi"
    print "3. Keluar"


def pilihLuas(pilihan):
    luas=0
    if pilihan == 1:
        luas= luas_segitiga()
        
    elif pilihan == 2:
        luas= luas_persegi(sisi)

    print "Jadi Luas Persegi " +str(luas)

def luas_segitiga():
    alas = int(input("Masukkan alas: "))
    tinggi = int(input("Masukkan tinggi : "))
    luas = 0.5 * alas * tinggi
    return luas

def luas_persegi(sisi):
    sisi = int(input("Masukkan sisi: "))
    luas=sisi*sisi
    return luas

pilihan = 0
while pilihan != 3:
    tampilkan_menu("Sultan",70)
    pilihan = int(input("Masukkan pilihan: "))
    pilihLuas(pilihan)

        