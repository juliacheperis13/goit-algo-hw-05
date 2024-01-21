class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        print(hash(key) % self.size)
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for index in range(len(self.table[key_hash])):
                if self.table[key_hash][index][0] == key:
                    self.table[key_hash].pop(index)
                    return True
        return False


if __name__ == '__main__':
    H = HashTable(10)
    H.insert("Invoice #1", 10)
    H.insert("Invoice #2", 20)
    H.insert("Invoice #3", 30)
    H.insert("Invoice #4", 110)
    H.insert("Invoice #5", 30)

    print(H.table)
    print(H.delete("Invoice #1"))   
    print(H.delete("Invoice #3")) 
    print(H.table)
