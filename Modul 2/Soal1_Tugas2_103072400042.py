import numpy as np

data = [] #menyimpan data

n = int(input("Masukkan jumlah mahasisswa : "))

for i in range(n):
    print(f"\nData Mahasiswa ke-{i+1}")
    nama = input("Nama  : ")
    nim = input("NIM    : ")
    nilai = float(input("Nilai  : "))
    tahun = int(input("Tahun Masuk  : "))

    data.append([nama, nim, nilai, tahun])

arr = np.array(data, dtype=object) #melakukan konversi ke numpy array

print("\n---Data Mahasiswa---") #berfungsi menampilkan data
for row in arr:
    print(row)
    
nilaiList = arr[:, 2].astype(float) #untuk mengambil kolom nilai

print("\nNilai Tertinggi    :", np.max(nilaiList))
print("Nilai Terendah       :", np.min(nilaiList))
print("Nilai Rata-rata      :", np.mean(nilaiList))


cari = input("\nMasukkan Nama/NIM yang dicari   : ") #berfungsi untuk pencarian
print("\n---Hasil Pencarian---")
ditemukan = False
for row in arr:
    if row[0] == cari or row[1] == cari:
        print(row)
        ditemukan = True

if not ditemukan:
    print("Data tidak ditemukan")