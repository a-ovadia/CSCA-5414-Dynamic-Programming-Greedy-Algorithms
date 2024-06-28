from MinHeap import MinHeap

class PriorityQueue:

    def __init__(self) -> None:
        self.heap = MinHeap()

    def enqueue(self, item, priority):
        self.heap.insert((priority, item))
    
    def dequeue(self):
        if self.heap.isEmpty():
            return None
        
        (priority, item) = self.heap.remove_min()
        return item
    
    def peek(self):
        return self.heap.peek()[1]
    
    def size(self):
        return self.heap.size()
    
    def isEmpty(self):
        return self.heap.isEmpty()