# Реализовать второй способ устранения коллизий в хэш таблицах
# Мы на занятии рассмотрели - связный список
# Второй способ - найти другую подходящую ячейку




class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = [None] * self.size
    
    def hash_function(self, key):
        return key % self.size
    
    def insert(self, key, value):
        hash_value = self.hash_function(key)
        
        # Если ячейка свободна, помещаем значение
        if self.hash_table[hash_value] is None:
            self.hash_table[hash_value] = (key, value)
        # Иначе ищем другую ячейку с помощью линейного пробирования
        else:
            i = 1
            while True:
                new_hash_value = (hash_value + i) % self.size
                # Если найдена свободная ячейка, помещаем значение
                if self.hash_table[new_hash_value] is None:
                    self.hash_table[new_hash_value] = (key, value)
                    break
                i += 1
    
    def find(self, key):
        hash_value = self.hash_function(key)
        
        # Если ключ соответствует ячейке, возвращаем значение
        if self.hash_table[hash_value] is not None and self.hash_table[hash_value][0] == key:
            return self.hash_table[hash_value][1]
        
        # Иначе ищем значение через линейное пробирование
        else:
            i = 1
            while True:
                new_hash_value = (hash_value + i) % self.size
                # Если ключ соответствует ячейке, возвращаем значение
                if self.hash_table[new_hash_value] is not None and self.hash_table[new_hash_value][0] == key:
                    return self.hash_table[new_hash_value][1]
                i += 1
                # Если достигнут конец таблицы, возвращаем None
                if i == self.size:
                    return None
                
if __name__ == '__main__':
    # Create a hash table with 
    # a size of 5 
    ht = HashTable(5) 
  
    # Add some key-value pairs 
    # to the hash table 
    ht.insert(10, 3) 
    ht.insert(20, 2) 
    ht.insert(30, 5)
    ht.insert(30, 6)
    ht.insert(30, 7)
    #ht.insert(30, 8)




    # Get the value for a key 
    print(ht.find(20))  # 2 