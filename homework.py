import modul as data

print("Selamat datang di program manajemen stock barang!")
print("Pilihan :")
print("1. Tambah data barang")
print("2. Edit data")
print("3. Hapus data barang")
print("4. Cari data")
print("5. Tampilkan data barang")
print("6. Tampilkan jumlah data")
print("7. Keluar")
print('\n')

while True:
    pilihan = int(input("Masukkan pilihan : "))
    print("=====================================")
    if pilihan == 1:
        print(data.add())
        print("")
    elif pilihan == 2:
        print(data.edit())
        print("")
    elif pilihan == 3:
        print(data.delete())
        print("")
    elif pilihan == 4:
        print(data.search())
    elif pilihan == 5:
        print(data.list())
    elif pilihan == 6:
        print(data.total())
        print("")
    elif pilihan == 7:
        exit()