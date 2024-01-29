#variabel lokal dan global
nama = "Mohammad Nauval Abdul Azis"
golongan = "Golangan D"
def sebut():
    # ini variabel lokal
    nama = "Moch Faisal Nurmadani"
    golongan = "Golongan E"
    # mengakses variabel lokal
    print ("Nama: %s" % nama)
    print ("Versi: %s" % golongan)

# mengakses variabelglobal
print("Nama: %s" % nama)
print("Versi: %s" % golongan)

# memanggil fungsi sebut()
sebut()
