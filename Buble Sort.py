def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

# Contoh penggunaan
data = [64, 34, 25, 12, 22, 11, 90]
print("Array sebelum diurutkan:")
print(data)

bubble_sort(data)

print("Array setelah diurutkan menggunakan Bubble Sort:")
print(data)
