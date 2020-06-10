class node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return 'Node [' + str(self.value) + ']'

class Tree:
    def __init__(self):
        self.root = None

    #функция для добавления узла в дерево
    def newNode(self, data):
        temp = node(0, None, None)
        temp.data = data
        return temp

    #функция для вычисления высоты дерева
    def height(self, node):
        if node == None:
            return 0
        else:
            lheight = self.height(node.left)
            rheight = self.height(node.right)

            if lheight > rheight:
                return (lheight + 1)
            else:
                return (rheight + 1)

    #функция для распечатки элементов на определенном уровне дерева
    def printGivenLevel(self, root, level, ltr):
        if root == None:
            return
        if level == 1:
            print("%d " % root.data)
        elif level > 1:
            if ltr:
                self.printGivenLevel(root.left, level - 1, ltr);
                self.printGivenLevel(root.right, level - 1, ltr);
            else:
                self.printGivenLevel(root.right, level - 1, ltr);
                self.printGivenLevel(root.left, level - 1, ltr);

    #функция для распечатки дерева
    def printLevelOrder(self, root):
        h = self.height(self.root)
        i = 1
        ltr = 1
        while (i <= h):
            self.printGivenLevel(self.root, i, ltr)
            i += 1

    #функция для вычисления ширины дерева
    def getMaxWidth(self, root):
        maxWdth = 0
        i = 1
        width = 0;
        h = self.height(root)
        while (i < h):
            width = self.getWidth(root, i)
            if (width > maxWdth):
                maxWdth = width;
            i += 1

        return maxWdth;

    def getWidth(self, root, level):
        if root == None:
            return 0
        if level == 1:
            return 1
        elif level > 1:
            return self.getWidth(root.left, level - 1) + self.getWidth(root.right, level - 1)
        self.getWidth(root.right, level - 1)


t = Tree()
t.root = t.newNode(8)

t.root.left = t.newNode(4)
t.root.right = t.newNode(12)
t.root.left.left = t.newNode(2)
t.root.left.right = t.newNode(6)
t.root.right.left = t.newNode(10)
t.root.right.right = t.newNode(14)
t.root.left.left.left = t.newNode(1)
t.root.right.right.right = t.newNode(25)
t.root.left.left.left.left = t.newNode(0)
t.root.left.left.right = t.newNode(3)
t.root.right.right.right.right = t.newNode(100)
t.root.right.right.right.left = t.newNode(20)

t.printLevelOrder(t.root)
print("\nвысота: %d\n" % t.height(t.root))
print("\nширина %d\n" % t.getMaxWidth(t.root))