class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self): 
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    def display(self):
        return self.items

    def count(self, item):
        #Menghitung jumlah kemunculan item dalam stack
        return self.items.count(item)

    def change(self, index, new_item):
        #Mengubah nilai item pada indeks tertentu dalam stack
        if 0 <= index < len(self.items):
            self.items[index] = new_item
        else:
            print("Indeks di luar jangakauan!")

# Contoh penggunaan
MyStack = Stack()
MyStack.push(1)
MyStack.push(5)
MyStack.push(4)
MyStack.push(4)
MyStack.push(4)
MyStack.push(7)
MyStack.push(4)
MyStack.push(4)

print("Menampilkan semua elemen=", MyStack.display())
print("Menampilkan element teratas = ", MyStack.peek())
print("Menampilkan element yang sama = ", MyStack.count(4))
MyStack.change(5, 7)
print("Menampilkan semua element = ", MyStack.display())
print("Jumlah element =", MyStack.size())
MyStack.isEmpty()
print("pop=", MyStack.pop())

print("Menampilkan semua element=", MyStack.display())
