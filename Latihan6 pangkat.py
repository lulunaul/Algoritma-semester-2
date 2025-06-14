def pangkat(base, exponent):
    return base ** exponent

# contoh penggunaan
base = int(input("masukkan angka = "))
exponent = int(input("masukkan pangkat = "))

hasil = pangkat(base, exponent)
print(base, "pangkat", exponent ,"adalah = ", hasil)