class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_data, new_data):
        current = self.head
        while current:
            if current.data == prev_data:
                new_node = Node(new_data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print("Node dengan nilai", prev_data, "tidak ditemukan dalam linked list.")
    
    def insert_before(self, next_data, new_data):
        if self.head is None:
            print("Linked list kosong.")
            return
        
        if self.head.data == next_data:
            self.add_at_beginning(new_data)
            return
        
        prev = None
        current = self.head
        while current and current.data != next_data:
            prev = current
            current = current.next
        
        if current is None:
            print("Node dengan nilai", next_data, "tidak ditemukan dalam linked list.")
            return
        
        new_node = Node(new_data)
        prev.next = new_node
        new_node.next = current
    
    def update_node(self, old_data, new_data):
        current = self.head
        while current:
            if current.data == old_data:
                current.data = new_data
                print("Node dengan nilai", old_data, "telah diperbarui menjadi", new_data)
                return
            current = current.next
        print("Node dengan nilai", old_data, "tidak ditemukan dalam linked list.")

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def delete_node(self, key):
        temp = self.head
        # Kasus khusus jika node yang akan dihapus adalah node pertama
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        # Mencari node dengan nilai key dan node sebelumnya
        prev = None
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        # Jika node dengan nilai key tidak ditemukan
        if temp is None:
            print("Node dengan nilai", key, "tidak ditemukan dalam linked list.")
            return
        # Menghapus node
        prev.next = temp.next
        temp = None

    def search_node(self, key):
        current = self.head
        while current:
            if current.data == key:
                print("Node dengan nilai", key, "ditemukan dalam linked list.")
                return
            current = current.next
        print("Node dengan nilai", key, "tidak ditemukan dalam linked list.")

#Buat Objek baru
MyLinkedList = LinkedList()
#Membuat mode baru dengan nilai 10,14,55,17,200 11
MyLinkedList.add_at_beginning(11)
MyLinkedList.add_at_beginning(100)
MyLinkedList.add_at_beginning(17)
MyLinkedList.add_at_beginning(55)
MyLinkedList.add_at_beginning(14)
MyLinkedList.add_at_beginning(10)
# Menampilkan semua node
print("node yang ditambahkan = ")
MyLinkedList.traverse()
# menyisipkan nilai 8 setelah 17
MyLinkedList.insert_after(17,8)
MyLinkedList.insert_before(17,1)
#merubah nilai 100 menjadi 150
MyLinkedList.update_node(100,150)
#meghapus node 55
MyLinkedList.delete_node(55)
#Menampilkam semua node
print("node setelah di tambahkan = ")
MyLinkedList.traverse()

# mencari node 2 dan 10
MyLinkedList.search_node(2)
MyLinkedList.search_node(10)
