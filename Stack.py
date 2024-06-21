class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Stack:

    def __init__(self) -> None:
        self.top = None
        self._size = 0
        
    def push(self, data):
        # Create new Node
        new_node = Node(data)

        # Set Node Next ptr
        new_node.next = self.top
    
        # Set top to new node
        self.top = new_node

        # Increment size counter
        self._size += 1

    def pop(self):
        # Return False if stack is empty
        if self._size == 0:
            return False

        # Store value of top
        top_entry = self.top

        # Set top to the next element
        self.top = self.top.next
    
        # Decrement size
        self._size -= 1

        # Return data in old top
        return top_entry.data
    
    def peek(self):
        if self._size == 0:
            return None
        return self.top.data
    
    def print_stack(self):
        current = self.top
        while current is not None:
            print(current.data)
            current = current.next

    def size(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0

    def clear(self):
        self.top = None
        self._size = 0

s = Stack()
s.push(5)
s.push(6)
s.push(5)
s.push(6)
s.push(5)
s.push(90)
s.pop()
s.print_stack()

