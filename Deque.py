# Basic Deque implementation using lists
#TODO implement using doubly-linked lists

class Deque:

    def __init__(self) -> None:
        self.elements = []
    
    def add_first(self, item):
        # first element should be at the end of the list
        self.elements.append(item)
    
    def add_last(self, item):
        # last element should be at the front of the list
        self.elements.insert(0, item)

    def remove_first(self):
        if self.is_empty(): # Empty
            return None
        
        # first element is at the end of the list
        return self.elements.pop()
    
    def remove_last(self):
        if self.is_empty():
            return None
        # last element at the front of the list
        return self.elements.pop(0)
    
    def peek_first(self):
        if self.is_empty():
            return None
        return self.elements[-1]
    
    def peek_last(self):
        if self.is_empty():
            return None
        return self.elements[0]
    
    def is_empty(self):
        return (True if len(self.elements) == 0 else False)
    
    def size(self):
        return len(self.elements)