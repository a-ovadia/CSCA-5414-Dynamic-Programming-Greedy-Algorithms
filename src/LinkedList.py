from Node import Node

class LinkedList:

    def __init__(self) -> None:
        self.head = None

    # Insert new Node at end of LinkedList
    def insertAtEnd(self, data):
        # Create new Node structure
        new_node = Node(data)

        # Check if head is None -> No elements in list
        if self.head is None:
            self.head = new_node # Set head to new Node
        
        else:
            current = self.head
            # Loop through linked list to find last position
            while current.next is not None:
                current = current.next
            
            # current holds last element, set the next ptr to new node
            current.next = new_node
        return True
    
    # Insert new Node at the beginning of LinkedList
    def insertAtBeginning(self, data):
        # Creare new Node structure
        new_node = Node(data)
        # set new node as head
        new_node.next = self.head
        self.head = new_node
        return True
    
    # Deletes a Node from LinkedList
    def deleteNode(self, value):
        if self.head is None: # list is empty
            return False
        
        if self.head.data == value: # value is at the head
            self.head = self.head.next
            return True
        
        current = self.head

        # Iterate through the list to find the position of the value to delete
        while current.next is not None and current.next.data != value:
            current = current.next
        
        if current.next is not None:
            current.next = current.next.next
            return True
        
        return False

    # Traverses LinkedList and prints out the value at each Node
    def traverse(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
