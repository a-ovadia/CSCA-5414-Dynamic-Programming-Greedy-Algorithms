from Node import Node

class LinkedList:

    def __init__(self) -> None:
        self.head = None

    def insert(self, key, value):
        newNode = Node(key, value)
        if not self.head:
            self.head = newNode
        else:
            current = self.head
            while current.next:
                if current.key == key:
                    current.value = value
                    return True
                current = current.next

            if current.key == key:
                current.value = value
            else:
                current.next = newNode
        return True
    
    def get(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None
    
    def remove(self, key):
        if not self.head:
            return None
        
        value_to_delete = None

        if self.head.key == key:
            value_to_delete = self.head.value
            self.head = self.head.next
            return value_to_delete
        
        current = self.head

        while current.next:
            if current.next.key == key:
                value_to_delete = current.next.value
                current.next = current.next.next
                return value_to_delete
            current = current.next
        return None