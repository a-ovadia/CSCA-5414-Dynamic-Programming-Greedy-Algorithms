class MergeSort:

    def __init__(self) -> None:
        pass

    @staticmethod
    def merge_sort(data, left, right):
        if left < right:
            # Find mid point
            mid = (left + right) // 2

            # Sort left half
            MergeSort.merge_sort(data, left, mid)

            # Sort right half
            MergeSort.merge_sort(data, mid + 1, right)

            # Merge the 2 sorted halves
            MergeSort.merge(data, left, mid, right)

        # Return sorted array    
        return data

    @staticmethod
    def merge(data, left, mid, right):
        # Calculate sizes of subarrays
        left_size = mid - left + 1
        right_size = right - mid

        # Temp vars to hold elements of data
        left_data = [0] * left_size
        right_data = [0] * right_size

        # Copy data to temp arrays
       
        for left_i in range(len(left_data)):
            left_data[left_i] = data[left + left_i ]
        
        for right_j in range(len(right_data)):
            right_data[right_j] = data[mid + right_j + 1]

        left_i, right_j, start = 0, 0, left

        # merge sorted array back into original array
        while left_i < left_size and right_j < right_size:
            if left_data[left_i] <= right_data[right_j]:
                data[start] = left_data[left_i]
                left_i += 1
            else:
                data[start] = right_data[right_j]
                right_j += 1
            start += 1
        
        # Copy remaining elements back into original array
        while left_i < left_size:
            data[start] = left_data[left_i]
            start += 1
            left_i += 1
        
        while right_j < right_size:
            data[start] = right_data[right_j]
            start += 1
            right_j += 1
        
        return data
