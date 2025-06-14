# Belajar list
My_List = [10,20,30,40,50]
print("Semua Element = ",My_List)

# Memanggil Element 30
panggil = My_List[0]
print("Panggil nilai awal =",panggil)
akhir = My_List[-1]
print("Panggil nilai akhir =",akhir)

# Memodifikasi
My_List[4]=25
print("element setelah diubah =",My_List)

# Menyisipkan
My_List.insert(0,5)
print("Semua Element = ",My_List)

# Sisispkan nilai 7 setelah 30
My_List.insert(4,7)
print("Semua Element = ",My_List)

# Sisipkan nilai 15 sebelum 10
My_List.insert(1,15)
print("Semua Element = ",My_List)

# Sisispkan nilai 25 sebelum 25
My_List.insert(7,25)
print("Semua Element = ",My_List)
My_List.insert
My_List.append(100)
print("semua element =",My_List)

# Menghapus
My_List.remove(10)
print("Semua Element=",My_List)

# Mengurutkan
My_List.sort()
print("semua element =",My_List)

# Menjumlahkan
total = sum(My_List)
print("total nilai =",total)

# Nilai tertinggi
tertinggi = max(My_List)
print("element tertinggi =",tertinggi)

# Nilai terendah
terendah = min(My_List)
print("element terendah =",terendah)