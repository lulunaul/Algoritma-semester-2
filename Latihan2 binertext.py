

biner_text = "01010000 01101001 01101110 01101010 01100001 01101101 00100000 0010001 00110000 00110000"
teks = ''.join(chr(int(b, 2)) for b in biner_text.split())
print(teks)