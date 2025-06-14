def sequentialsearch(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

# contoh penggunaan
data = [10, 22, 5, 31, 17]
print(data)
target = int(input("masukkan data yang dicari = "))
index = sequentialsearch(data, target)
if index != -1:
    print("target ditemukan pada indeks:", index)
else:
    print("target tidak ditemukan dalam daftar")