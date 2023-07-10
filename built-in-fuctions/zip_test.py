"""
The `zip` function in Python is a built-in function that allows you to 
combine multiple iterables into a single iterator of tuples. It takes 
iterables as input, such as lists, tuples, or strings, and returns an 
iterator that produces tuples containing elements from each input iterable. 

The syntax for the `zip` function is as follows:

```python
zip(*iterables)
```

The `zip` function takes any number of iterables as arguments, which are 
passed as separate arguments or packed into a single iterable using the 
asterisk (*) operator. It returns an iterator that generates tuples where the 
i-th tuple contains the i-th element from each of the input iterables. 

Here are some key characteristics of the `zip` function: 

1. Length: The length of the resulting iterator is determined by the shortest 
input iterable. If the input iterables have different lengths, the resulting 
iterator will only contain tuples up to the length of the shortest iterable. 

2. Laziness: The `zip` function generates the tuples on-the-fly as they are 
requested, making it memory-efficient for large iterables. 

3. Iterator: The `zip` function returns an iterator rather than a list. If 
you need a list, you can wrap the `zip` function call with the `list` 
constructor to convert the iterator into a list. 

4. Uneven iterables: When the input iterables have different lengths, the 
resulting iterator will only contain tuples up to the length of the shortest 
iterable. Elements from longer iterables that do not have corresponding 
elements in shorter iterables are simply ignored. 

5. Immutable: The tuples generated by the `zip` function are immutable, 
meaning you cannot modify the elements within them. 

It's worth noting that the `zip` function can accept any number of input 
iterables, as long as they are of compatible lengths. This makes it a 
versatile tool for combining and iterating over multiple sequences in 
parallel. 

Remember that the `zip` function returns an iterator, so if you need to 
access the resulting tuples multiple times, you should convert it to a list 
or store it in a variable. 



"""

def test_zip1():
    """ Basic Usage """
    numbers = [1, 2, 3]
    letters = ['a', 'b', 'c']

    result = zip(numbers, letters)

    assert list(result) == [(1, 'a'), (2, 'b'), (3, 'c')]


def test_zip2():
    """ Unequal-Length Iterablese """
    numbers = [1, 2, 3, 4]
    letters = ['a', 'b', 'c']

    result = zip(numbers, letters)

    assert list(result) == [(1, 'a'), (2, 'b'), (3, 'c')]


def test_zip3():
    """ Using zip with More Than Two Iterables """
    numbers = [1, 2, 3]
    letters = ['a', 'b', 'c']
    fruits = ['apple', 'banana', 'cherry']

    result = zip(numbers, letters, fruits)

    assert list(result) == [
        (1, 'a', 'apple'),
        (2, 'b', 'banana'),
        (3, 'c', 'cherry')
    ]


def test_zip4():
    """ Unzipping """
    combined = [(1, 'a'), (2, 'b'), (3, 'c')]

    numbers, letters = zip(*combined)

    assert numbers == (1, 2, 3)
    assert letters == ('a', 'b', 'c')
