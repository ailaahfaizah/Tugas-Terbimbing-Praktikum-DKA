import numpy as np

data = []

n = int(input("Masukkan jumlah barang: "))

for i in range(n):
    print(f"\nData barang ke-{i+1}")
    nama = input("Nama Barang   : ")
    kode = input("Kode Barang   : ")
    jumlah = int(input("Jumlah  : "))
    harga = float(input("Harga per Unit : "))
    
    data.append([nama, kode, jumlah, harga])


arr = np.array(data, dtype=object)#melakukan konversi ke numpy array


print("\n---Data Inventaris---")#menampilkan data dan total nilai
for row in arr:
    total = int(row[2]) * float(row[3])
    print(row, "Total   :", total)

#berfungsi untuk pencarian
cari = input("\nMasukkan Nama/Kode Barang yang dicari   : ")

print("\n---Hasil Pencarian---")
ditemukan = False
for row in arr:
    if row[0] == cari or row[1] == cari:
        total = int(row[2]) * float(row[3])
        print(row, "Total   :", total)
        ditemukan = True

if not ditemukan:
    print("Barang tidak ditemukan")
