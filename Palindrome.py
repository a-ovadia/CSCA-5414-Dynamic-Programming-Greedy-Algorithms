from Deque import Deque

# Implement palindrome checker using Deque structure
def is_palindrome(word):
    if word.strip() == "":
        return False
    
    deque = Deque()
    # Add each char to the first position of the Deque
    for char in word:
        deque.add_first(char)
    
    while deque.size() > 1:
        first = deque.remove_last()
        last = deque.remove_first()
        if first != last:
            return False
    
    return True