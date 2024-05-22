stok = []

def add():
    input_nama = input("Masukkan nama barang : ").lower()
    input_stok = int(input("Masukkan stok barang : "))
    item = {'nama' : input_nama, 'stok' : input_stok}
    stok.append(item)
    print("--- Data berhasil ditambahkan ---")

def edit():
    index = int(input("Ubah data ke : "))
    index -= 1
    input_nama = input("Masukkan nama barang : ").lower()
    input_stok = int(input("Masukkan stok barang : "))
    data_change = {'nama' : input_nama, 'stok' : input_stok}
    stok[index] = data_change
    print("--- Data berhasil diperbarui ---")

def delete():
    index = int(input("Hapus data ke : "))
    index -= 1
    del stok[index]
    print("--- Data berhasil dihapus ---")

def search():
    data_input = input("Cari nama barang : ").lower()
    number = 1
    items = []
    for i in stok:
        if data_input in i['nama']:
            stock.append(i)
    if items:
        for i in items:
            print(f"{number}. {i['nama']} , Stok : {i['stok']}")
            number += 1
    else:
        print("--- Data barang tidak ditemukan ---")

def list():
    number = 1
    if stok:
        print("--- Data barang ---")
        for i in stok:
            print(f"{number}. {i['nama']} , Stok : {i['stok']}")
            number += 1
    else:
        print("--- Data barang kosong ---")

def total():
    print(f"Jumlah data tersimpan : {len(stok)}")
