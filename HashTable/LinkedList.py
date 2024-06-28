from Node import Node

class LinkedList:

    def __init__(self) -> None:
        self.head = None

    def insert(self, key, value):
        """" Inserts new element to the end of the list"""
        
        # Initialze new Node
        newNode = Node(key, value)

        # Check if Head is empty
        if not self.head:
            self.head = newNode

        # Else iterate through linked list to find last element to append new Node    
        else:
            current = self.head
            while current.next:
                if current.key == key:
                    current.value = value
                    return True
                current = current.next
            
            # If key exists already, modify the value to the new value
            if current.key == key:
                current.value = value
            
            else:
                current.next = newNode

        return True
    
    def get(self, key):
        """ Returns value of a Node of specified key """
        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None
    
    def remove(self, key):
        """Remove a key from the linked list"""

        # Check if linked list is empty
        if not self.head:
            return None
        
        value_to_delete = None

        # Check if the key is at the head
        if self.head.key == key:
            value_to_delete = self.head.value
            self.head = self.head.next
            return value_to_delete
        
        current = self.head

        # Iterate through linked list to find key
        while current.next:
            if current.next.key == key:
                value_to_delete = current.next.value
                current.next = current.next.next
                return value_to_delete
            current = current.next
        return None