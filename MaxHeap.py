class MaxHeap:

    def __init__(self, data = None) -> None:
        self.heap = data if data is not None else []

    def __repr__(self) -> str:
        return f"Max-Heap of size {self.getSize()}, Max = {self.getMax()}, Elements = {self.heap}"

    def getSize(self):
        # Return size starting from 1
        return len(self.heap)
    
    def insert(self, element):
        self.heap.append(element)
        self.bubbleUp(self.getSize() - 1)

    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        

    def bubbleUp(self, index):
        if index <= 0:
            return
        
        # Find parent index
        parent = (index - 1) // 2

        # Compare element to its parent
        if self.heap[index] > self.heap[parent]:
            # Swap with parent
            self.swap(index, parent)

            self.bubbleUp(parent)
        else:
            return
        
    def bubbleDown(self, index):
        # Determine children position
        left_child = (2 * index) + 1
        right_child = (2 * index) + 2

        # Check if index is leaf
        if left_child >= self.getSize():
            return # Nothing needs to be done
        
        # Check for existance of 1 left child
        if right_child >= self.getSize():
            if self.heap[index] < self.heap[left_child]:
                # Swap
                self.swap(index, left_child)

        # else index has 2 children
        else:
            # Check which child has a greater value
            if self.heap[left_child] > self.heap[right_child]:
               if self.heap[index] < self.heap[left_child]:
                    # Swap
                    self.swap(index, left_child)
                    self.bubbleDown(left_child)
            else:
                if self.heap[index] < self.heap[right_child]:
                    # Swap
                    self.swap(index, right_child)
                    self.bubbleDown(right_child)

    def getMax(self):
        return self.heap[0]
    
    def remove(self, index):
        # Bounds check
        if self.getSize() <= index or index < 0 or self.getSize() == 0:
            return None
        
        # Check edge case that index is the last element
        if self.getSize() -1 == index:
            return self.heap.pop()
        
        # swap index with last element
        else:
            self.swap(index, self.getSize() - 1 ) #Index start at 0
            # Store deleted element
            remove_element = self.heap.pop()
            # Now that we removed an element, check to make sure we have a parent to check
            if self.getSize() <= 1:
                # If we are left with 1 element after the pop() then we are good
                return remove_element
            else:
                self.bubbleDown(index)
        
        return remove_element
    
    def removeMax(self):
        return self.remove(0)
    
    def heapify(self, data):
        self.heap = data
        index = self.getSize() // 2
        while index >= 0:
            self.bubbleDown(index)
            index -= 1