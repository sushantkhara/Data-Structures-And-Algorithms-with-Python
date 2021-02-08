"""
How to Implement Dynamic Array?
1.	Create a Static array with an initial capacity
2.	Add elements to the underlying static array, keeping track of the no. elements.
3.	If adding another element will exceed the capacity, then create a new static array with twice the capacity and copy the original elements into it.

"""
class dynamic_array():
    def __init__(self, capacity) -> int:
        self.capacity = capacity




    