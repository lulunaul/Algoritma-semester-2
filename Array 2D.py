# Contoh membuat array 2 dimensi
array_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Mengakses elemen di baris ke-2, kolom ke-3
value = array_2d[1][2]  # Baris indeks 1, kolom indeks 2
print("Nilai Array =", value)

# Menghitung jumlah baris dan kolom dalam array 2D
num_rows = len(array_2d)
num_cols = len(array_2d[0]) if array_2d else 0

print("Jumlah baris:", num_rows)
print("Jumlah kolom:", num_cols)

# Menghitung total penjumlahan semua elemen dalam array 2D
total = sum(sum(row) for row in array_2d)
print("Total penjumlahan semua elemen:", total)

# Menemukan nilai maksimum dalam array 2D
max_value = max(max(row) for row in array_2d)
print("Nilai maksimum:", max_value)