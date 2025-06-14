class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def print_tree(node, level=0):
    indent = ' ' * 4 * level + ('└── ' if level > 0 else '')
    print(indent + str(node.data))
    for child in node.children:
        print_tree(child, level + 1)

# Contoh Inputan
A = TreeNode("A")
B = TreeNode("B")
C = TreeNode("C")
D = TreeNode("D")
E = TreeNode("E")
F = TreeNode("F")
G = TreeNode("G")
H = TreeNode("H")
I = TreeNode("I")
K = TreeNode("K")
L = TreeNode("L")
A.add_child(D)
D.add_child(K)
A.add_child(E)
E.add_child(G)
A.add_child(F)
F.add_child(H)
F.add_child(L)
A.add_child(B)
A.add_child(C)
C.add_child(I)
print_tree(A)