class MinHeap:

    def __init__(self, data = None) -> None:
        self.heap = data if data is not None else []

    def __repr__(self) -> str:
        return f"Min-Heap of size {self.getSize()}, min = {self.getMin()}"

    def getSize(self):
        # Return size starting from 1
        return len(self.heap)
    
    def insert(self, element):
        self.heap.append(element)
        self.bubbleUp(self.getSize() - 1) # Using start index 0
        

    def bubbleUp(self, index):
        if index <= 0:
            return None
        
        # Find parent index
        parent_index = (index - 1) // 2

        # Compare element at index to its parent
        if self.heap[index] < self.heap[parent_index]:
            # Swap index with its parent
            self.swap(index, parent_index)
            # Recursively call bubbleUp to check if it is in the right place
            self.bubbleUp(parent_index)
        
        # Otherwise Index is in the right spot, return
        else:
            return
        
    def bubbleDown(self, index):
        # Determine children positions
        left_child = (2 * index) + 1
        right_child = (2 * index) + 2

        # Check if index is the leaf
        if left_child >= self.getSize():
            return # Nothing needs to be done
        
        # check if index has 1 child
        # If 1 child exists, it must be a left child
        if right_child >= self.getSize():
            #compare values to see if swap needed
            if self.heap[index] > self.heap[left_child]:
                # Swap
                self.swap(index, left_child)
                # Recursive call
                self.bubbleDown(left_child)
        # index has 2 children
        else: 
            # Check with child has a lower value
            #if self.heap[left_child] > self.heap[right_child]:
            if self.heap[left_child] < self.heap[right_child]:
                if self.heap[index] > self.heap[left_child]:
                    self.swap(index, left_child)
                    self.bubbleDown(left_child)
            else:
                if self.heap[index] > self.heap[right_child]:
                    self.swap(index, right_child)
                    self.bubbleDown(right_child)
   
    def getMin(self):
        return self.heap[0]

    # Simple function to swap 2 elements in a list
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
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
    
    # Basic wrapper function to call remove() at index = 0
    def remove_min(self):
        return self.remove(0)
    
    # Create min-heap from list input adn save in self.heap
    def heapify(self, data):
        self.heap = data
        index = self.getSize() // 2
        while index >= 0:
            self.bubbleDown(index)
            index -= 1
    
    def isEmpty(self):
        return len(self.heap) == 0
    
    def size(self):
        return len(self.heap)
    
    def peek(self):
        if not self.isEmpty():
            return self.getMin()

# Testing the MinHeap
def test_min_heap():
    # Test heapify
    heap_data = [5, 7, 10, 15, 12, 20, 25, 42, 35, 30]
    heap_obj = MinHeap(heap_data)
    assert heap_obj.heap == [5, 7, 10, 15, 12, 20, 25, 42, 35, 30], f"Expected [5, 7, 10, 15, 12, 20, 25, 42, 35, 30], but got {heap_obj.heap}"

    # Test insert
    heap_obj.insert(3)
    assert heap_obj.heap[0] == 3, f"Expected min element 3, but got {heap_obj.heap[0]}"
    assert 3 in heap_obj.heap, "Inserted element 3 not found in the heap"

    # Test getMin
    min_element = heap_obj.getMin()
    assert min_element == 3, f"Expected min element 3, but got {min_element}"

    # Test remove_min
    removed_min = heap_obj.remove_min()
    assert removed_min == 3, f"Expected removed min element 3, but got {removed_min}"
    assert 3 not in heap_obj.heap, "Removed element 3 still found in the heap"

    # Test remove specific index
    size_before_removal = heap_obj.getSize()
    removed_element = heap_obj.remove(2)  # Remove element at index 2
    assert size_before_removal - 1 == heap_obj.getSize(), "Heap size did not decrease after removal"
    assert removed_element == 10, f"Expected removed element 10, but got {removed_element}"
    assert 10 not in heap_obj.heap, "Removed element 10 still found in the heap"

    # Test remove with invalid index
    invalid_remove = heap_obj.remove(-1)
    assert invalid_remove == None, "Expected None for invalid index removal"
    invalid_remove = heap_obj.remove(heap_obj.getSize() + 1)
    assert invalid_remove == None, "Expected None for out-of-bounds index removal"

    # Additional inserts and removals
    heap_obj.insert(1)
    assert heap_obj.heap[0] == 1, f"Expected min element 1, but got {heap_obj.heap[0]}"
    
    heap_obj.insert(8)
    assert 8 in heap_obj.heap, "Inserted element 8 not found in the heap"
    
    min_element = heap_obj.getMin()
    assert min_element == 1, f"Expected min element 1, but got {min_element}"

    removed_min = heap_obj.remove_min()
    assert removed_min == 1, f"Expected removed min element 1, but got {removed_min}"
    assert 1 not in heap_obj.heap, "Removed element 1 still found in the heap"

    print("All test cases passed!")

# Run the tests
test_min_heap()