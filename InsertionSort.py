class InsertionSort:

    def __init__(self):
        pass

    @staticmethod
    def sortASC(data):
        for j in range(1, len(data)):
            InsertionSort.insert(data, j)
        return data

    @staticmethod
    def sortDSC(data):
        for j in range(1, len(data)):
            InsertionSort.insertDSC(data, j)
        return data
    
    @staticmethod
    def insertDSC(data, j):
        i = j - 1
        while i >= 0 :
            if data[i] < data[i + 1]:
                InsertionSort.swap(data, i, i+1)
                i -= 1
            else: break       


    @staticmethod
    def insert(data, j):
        i = j - 1
        while i >= 0 :
            if data[i] > data[i + 1]:
                InsertionSort.swap(data, i, i+1)
                i -= 1
            else: break

    @staticmethod
    def swap(data, val1, val2):
        left_pos = data[val1]
        right_pos = data[val2]
        data[val2] = left_pos
        data[val1] = right_pos