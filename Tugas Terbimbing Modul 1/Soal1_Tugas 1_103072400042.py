tahun = int(input("Masukkan Tahun : "))

def isKabisat(tahun):
    return (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0)

if isKabisat(tahun):
    print(tahun, "adalah tahun kabisat")
else:
    print(tahun, "bukan tahun kabisat")