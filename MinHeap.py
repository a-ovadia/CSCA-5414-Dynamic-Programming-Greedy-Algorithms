class Heap:

    def __init__(self) -> None:
        self.heap = []
        self.size = 0

    def insert(self, value):
        self.heap.append(value)
        self.bubbleUp(self.size)
        self.size += 1

    def bubbleUp(self, index):
        if index <= 0:
            return
        parent_index = (index - 1) // 2
        if self.heap[index] < self.heap[parent_index]:
            # Swap
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.bubbleUp(parent_index)

    def bubbleDown(self, index):
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < self.size and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < self.size and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break

    def heapify(self, new_data, size):
        self.size = size
        self.heap = new_data
        index = (self.size // 2) - 1
        while index >= 0:
            self.bubbleDown(index)
            index -= 1
        
    def deleteIndex(self, index):
        # Swap index and last element
        self.heap[index], self.heap[self.size - 1] = self.heap[self.size - 1], self.heap[index]
        # Remove the last element
        self.heap.pop()
        self.size -= 1

        if index < self.size:
            if index > 0 and self.heap[index] < self.heap[(index - 1) // 2]:
                self.bubbleUp(index)
            else:
                self.bubbleDown(index)
