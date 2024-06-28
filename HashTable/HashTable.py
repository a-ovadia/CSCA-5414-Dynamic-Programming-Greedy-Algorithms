from LinkedList import LinkedList
#TODO implement load factor to rehash

class HashTable:

    def __init__(self, size) -> None:
        self.size = size
        self.table = []
        
        for num in range(self.size):
            self.table.append(LinkedList())
    
    def hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self.hash(key)
        self.table[index].insert(key, value)
    
    def get(self, key):
        index = self.hash(key)
        return self.table[index].get(key)
    
    def remove(self, key):
        index = self.hash(key)
        return self.table[index].remove(key)
    
    def print_all(self):
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}:")
            current = bucket.head
            while current:
                print(f"  {current.key}: {current.value}")
                current = current.next
            if not bucket.head:
                print("  <empty>")
            print()