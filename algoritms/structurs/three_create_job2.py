# дать им реализовать функцию по заполнению дерева из отсортированного списка
# Дать им доработать удаление из дерева. Удаления корня если есть 2 детей



class Node:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None
        self.parrent = None

class BinaryTree:
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
    
    def insert_sorted_list(self, sorted_list):
        for i in sorted_list:
            self.add(i)
        
    def find_node(self, cn, value):
        v = cn
        while v is not None:
            if v.value == value:
                return v
            elif value < v.value:
                v = v.left
            else:  # x > v.key:
                v = v.right
        return None

    def find_min_node(self, cn):
        min_node = cn
        while cn is not None:
            if cn.value < min_node.value:
                min_node = cn
            if cn.left is not None:
                cn = cn.left
                temp = cn
            else:
                temp = cn
                cn = cn.left
        return temp    
        '''   
        if cn is None:
            return cn
        node = self.find_min_node(cn.left)
        return node
        ''' 

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
            #вариант удаления корневой ноды с двумя детьми с переносом на место корня минимального правого значения лепестка
            min_node_of_right = self.find_min_node(node.right)
            if min_node_of_right.value != node.left.value:
                min_node_of_right.left = node.left
                min_node_of_right.left.parrent = min_node_of_right
            if min_node_of_right.value != node.right.value:
                min_node_of_right.right = node.right
                min_node_of_right.right.parrent = min_node_of_right
            
            min_node_of_right.parrent = node.parrent
            if node.parrent is not None:
                if node.parrent.left == node:
                    node.parrent.left = min_node_of_right
                else:
                    node.parrent.right = min_node_of_right
            else:
                self.root = min_node_of_right
            return
            
            '''
            #удалим корень вместе с лепестками, если у корня есть два лепестка
            #за корень примем ноду с двумя детьми. удалим ноду и её детей
            if node.parrent.left == node:
                node.parrent.left = None
                return
            else:
                node.parrent.right = None
                return
            '''
        raise Exception("Не могу удалить ноду")
  




sorted_list = [5, 3, 1, 2, 8, 7, 6, 19, 15, 22]
tree = BinaryTree()
tree.insert_sorted_list(sorted_list)

print(tree.find_node(tree.root, 19))

tree.delete(5)
a = 0