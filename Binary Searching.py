def binary_search(data, target):
    low = 0
    high = len(data) -1
    while low <= high:
        mid = (low + high) //2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
        return -1

 # contoh penggunaan
data = [1, 5, 8, 12, 16, 20, 24, 28]

#ulangi pencarian
while True:
    print("isi dari array = ", data)
    target = int(input("Masukkan Nilai yang Dicari = "))
    index = binary_search(data, target)
    if index != -1:
        print("Target ditemukan pada indeks:", index)
    else:
        print("target tidak ditemukan dalam daftar")
        
#Kondisi Ya atau Tidak
    ulang = input("Ingin mencari lagi? (Y/T): ").strip().upper()
    if ulang != 'Y':
        print("Terima kasih! program selesai.")
        break