class MyList:
    def __init__(self, *args):
        self.items = list(args)
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, key):
        return self.items[key]
    
    def __setitem__(self, key, value):
        self.items[key] = value
    
    def __delitem__(self, key):
        del self.items[key]
    
    def __iter__(self):
        self.current = 0
        return self
    
    def __next__(self):
        if self.current >= len(self.items):
            raise StopIteration
        item = self.items[self.current]
        self.current += 1
        return item
    
    def __contains__(self, item):
        return item in self.items


def test_container_iteration_example():
    my_list = MyList(1, 2, 3, 4, 5)
    
    # Length
    assert len(my_list) == 5
    
    # Item retrieval using indexing
    assert my_list[0] == 1
    assert my_list[3] == 4
    
    # Item assignment using indexing
    my_list[2] = 10
    assert my_list[2] == 10
    
    # Item deletion using indexing
    del my_list[1]
    assert len(my_list) == 4
    assert my_list[1] == 10
    
    # Iteration
    iteration_result = []
    for item in my_list:
        iteration_result.append(item)
    assert iteration_result == [1, 10, 4, 5]
    
    # Membership check
    assert 4 in my_list
    assert 7 not in my_list


"""
The container and iteration methods are implemented as follows:

- `__len__(self)`: This method returns the length of the container. In this 
case, it returns the length of `self.items`, which represents the number of 
elements in the list. 

- `__getitem__(self, key)`: This method allows item retrieval using indexing 
or slicing. It delegates the indexing operation to the underlying `
self.items` list and returns the corresponding item. 

- `__setitem__(self, key, value)`: This method allows item assignment using 
indexing or slicing. It delegates the assignment operation to the underlying `
self.items` list. 

- `__delitem__(self, key)`: This method allows item deletion using indexing 
or slicing. It delegates the deletion operation to the underlying `
self.items` list. 

- `__iter__(self)`: This method creates an iterator object by returning `self`
. It initializes `self.current` to 0, representing the current index of the 
iteration. 

- `__next__(self)`: This method retrieves the next item from the iterator. It 
checks if `self.current` is within the bounds of the `self.items` list. If it 
is, it retrieves the item at the current index, increments `self.current`, 
and returns the item. If `self.current` exceeds the length of `self.items`, 
it raises the `StopIteration` exception to signal the end of iteration. 

- `__contains__(self, item)`: This method performs a membership check by 
determining if `item` is present in `self.items`. It returns `True` if `item` 
is found and `False` otherwise. 

The `test_container_iteration_example()` function tests the container and 
iteration methods of the `MyList` class. It creates an instance of `MyList` 
with some initial elements. The function then performs operations such as 
length retrieval, item retrieval, item assignment, item deletion, iteration, 
and membership check. It asserts the expected results for each operation. 

This example demonstrates how the container and iteration methods can be 
implemented to make a custom class behave like a container object, such as a 
list, allowing for indexing, slicing, iteration, and membership checks.
"""