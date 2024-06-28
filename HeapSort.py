from MinHeap import MinHeap

class HeapSort:

    def __init__(self, data) -> None:
        self.heap = MinHeap(data) if data is not None else []
        

    def heapSort(self):
        sorted_list = []
        while not self.heap.isEmpty():
            sorted_list.append(self.heap.remove_min())
        return sorted_list

