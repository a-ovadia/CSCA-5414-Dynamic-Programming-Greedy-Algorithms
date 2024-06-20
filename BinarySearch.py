class BinarySearch:

    @staticmethod
    def binary_search(data, search_element):
        return BinarySearch.binary_search_helper(data, search_element, 0, len(data) - 1)

    @staticmethod
    def binary_search_helper(data, search_element, left, right):
        if left > right:
            # Return False if search element is not in data list
            return False
        else:
            mid = (left + right) // 2
        
            if data[mid] == search_element:
                # If element is found, return tuple containing True and the index of the element in the data list
                return (True, mid)
            elif data[mid] < search_element:
                return BinarySearch.binary_search_helper(data, search_element, mid + 1, right)
            else: # data[mid] > element
                return BinarySearch.binary_search_helper(data, search_element, left, mid - 1)