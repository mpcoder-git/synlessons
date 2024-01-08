class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None
        self.parrent = None

class BinarySearchTree:
    def __init__(self):
        self.root = Node()

    

    def add_data(self, cn, value):
        if cn.value > value:
            if cn.left is None:
                cn.left = Node()
                cn.left.value = value
                cn.left.parrent  = cn
            else:
                self.add_data(cn.left, value)
        else:
            if cn.right is None:
                cn.right = Node()
                cn.right.value = value
                cn.right.parrent  = cn
            else:
                self.add_data(cn.right, value)


    def add(self, value):
        if self.root.value is None:
            self.root.value = value
            return
        self.add_data(self.root, value)

    def find(self, value):
        if self.root.value is None:
            return False
        if self.root.value == value:
            return True
        
        node = self.find_node(self.root, value)
        if node is None:
            return False
        return True
        
    def find_node(self, cn, value):
         if cn is None or cn.value == value:

        return cn

    if cn.value > value:

        res = self.find_node(cn.left, value)

        if res is not None:

            return res

    else:

        res = self.find_node(cn.right, value)

        if res is not None:

            return res


    def find_min_node(self, cn):
        if cn is None:
            return cn
        
        node = self.find_min_node(cn.left)
        return node


    def delete(self, value):
        if (self.root.left is None and self.root.right is None and
            self.root.value == value):
            self.root.value = None
            return
        if (self.root.left is not None and self.root.right is None and
            self.root.value == value):
            self.root = self.root.left
            self.root.parrent = None
            return
        if (self.root.left is  None and self.root.right is not None and
            self.root.value == value):
            self.root = self.root.right
            self.root.parrent = None
            return
        
        node = self.find_node(self.root, value)
        if node is None:
            raise Exception("Не могу найти узел для удаления")
        else:
            self.delete_data(node)
        

    def delete_data(self, node):
        #если детей нет
        if (node.left is None and node.right is None):
            if node.parrent.left == node:
                node.parrent.left = None
            else: 
                node.parrent.right = None
            return        
        
        #если дети есть
        if (node.left is not None and node.right is None):
            if node.parrent.left == node:
                node.parrent.left = node.left
            else: 
                node.parrent.right = node.left
            return
        #если дети есть
        if (node.left is  None and node.right is not None):
            if node.parrent.left == node:
                node.parrent.left = node.right
            else: 
                node.parrent.right = node.right
            return
        #если двое детей
        if (node.left is not None and node.right is not None):
            min_node_of_right = self.find_min_node(node.right)
            min_node_of_right.left = node.left
            if node.parrent.left == node:
                node.parrent.left = min_node_of_right
            else:
                node.parrent.right = min_node_of_right
            return
        raise Exception("Не могу удалить ноду")








bst = BinarySearchTree()
'''
bst.add(10)
bst.add(8)
bst.add(9)
bst.add(7)
bst.add(20)

print(bst.find(7))

bst.delete(7)
print(bst.find(20))
'''
bst.add(5)
bst.add(3)
bst.add(1)
bst.add(2)
bst.add(8)
bst.add(7)
bst.add(6)
bst.add(19)
bst.add(15)
bst.add(22)
'''
bst.delete(2)
bst.delete(15)
bst.delete(22)
'''
#bst.delete(1)
#bst.delete(3)

bst.delete(19)

#удаление 5 доработать, проверка что мы корень, ищем минимум 6 и ставим вместо 5
a  = 1