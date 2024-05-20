stok = []

def add():
    input_nama = input("Masukkan nama barang : ").title()
    input_stok = int(input("Masukkan stok barang : "))
    item = {'nama' : input_nama, 'stok' : input_stok}
    stok.append(item)
    print("--- Data berhasil ditambahkan ---")
    return '\n'

def edit():
    index = int(input("Ubah data ke : "))
    index -= 1
    input_nama = input("Masukkan nama barang : ").title()
    input_stok = int(input("Masukkan stok barang : "))
    data_change = {'nama' : input_nama, 'stok' : input_stok}
    stok[index] = data_change
    print("--- Data berhasil diperbarui ---")
    return '\n'

def delete():
    index = int(input("Hapus data ke : "))
    index -= 1
    del stok[index]
    print("--- Data berhasil dihapus ---")
    return '\n'

def search():
    data_input = input("Cari nama barang : ").title()
    number = 1
    stock = []
    for i in stok:
        if data_input in i['nama']:
            stock.append(i)
    if stock:
        for i in stock:
            print(f"{number}. {i['nama']} , Stok : {i['stok']}")
            number += 1
    else:
        print("--- Data tidak ditemukan ---")
    return '\n'

def list():
    number = 1
    if stok:
        print("--- Data barang ---")
        for i in stok:
            print(f"{number}. {i['nama']} , Stok : {i['stok']}")
            number += 1
    else:
        print("--- Data barang kosong ---")
    return '\n'

def total():
    print(f"Jumlah data tersimpan : {len(stok)}")
    return '\n'
