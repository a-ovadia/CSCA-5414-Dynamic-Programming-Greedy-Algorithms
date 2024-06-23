def QuickSort(data, left, right):
    # assert left == -1, "left index starts at -1 "
    # assert right == len(data) - 1, "Right index should be last element"
     
    if left >= right:
        return data
    
   
    p = partition(data, left, right)
    QuickSort(data, left, p - 1)
    QuickSort(data, p + 1, right)
    return data



def partition(data, left, right):
    pivot = data[right]
    i = left - 1
    j = left
    while j < right:
        if data[j] < pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
        j += 1
    data[i + 1], data[right] = data[right], data[i + 1]
    return i + 1