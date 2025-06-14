def hitung_faktorial(n):
    if n == 0 or n == 1:
        return 1
    return n * hitung_faktorial(n - 1)
n = int(input("masukkan nilai n: "))
faktorial = hitung_faktorial(n)
print("faktorial", n, "! =", faktorial)