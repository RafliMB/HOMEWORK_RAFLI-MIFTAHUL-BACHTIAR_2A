import module as data

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
        data.add()
        print('\n')
    elif pilihan == 2:
        data.edit()
        print('\n')
    elif pilihan == 3:
        data.delete()
        print('\n')
    elif pilihan == 4:
        data.search()
        print('\n')
    elif pilihan == 5:
        data.list()
        print('\n')
    elif pilihan == 6:
        data.total()
        print('\n')
    elif pilihan == 7:
        exit()
