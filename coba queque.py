class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def peek(self):
        if not self.is_empty():
            return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    
    def traverse(self):
        return self.items
    
#coba penggunaan
# Membuat instance dari Queue
q = Queue()

# Menambahkan elemen ke antrian
q.enqueue("apel")
q.enqueue("pisang")
q.enqueue("ceri")

# Melihat elemen pertama tanpa menghapusnya
print("Elemen pertama:", q.peek())  # Output: apel

# Menghapus elemen pertama dari antrian
print("Menghapus:", q.dequeue())    # Output: apel

# Menampilkan semua elemen dalam antrian
print("Isi antrian:", q.traverse()) # Output: ['pisang', 'ceri']

# Menampilkan ukuran antrian
print("Ukuran antrian:", q.size())  # Output: 2

# Mengecek apakah antrian kosong
print("Apakah antrian kosong?", q.is_empty())  # Output: False
