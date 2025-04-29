'''
access the elements of a collection object sequentially without exposing its underlying representation
'''

# Iterator: Implements __next__() and optionally __iter__() (to make it compatible with for loops).
class AlphabetIterator:
    def __init__(self, start='A', end='Z'):
        self.current = ord(start)
        self.end = ord(end)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        letter = chr(self.current)
        self.current += 1
        return letter

# Iterable: Implements __iter__() and returns an iterator.
class Alphabet:
    def __init__(self):
        self.start = 'A'
        self.end = 'Z'

    def __iter__(self):
        return AlphabetIterator(self.start, self.end)

alphabet = Alphabet()
for letter in alphabet:
    print(letter, end=" ")


class Counter:
    def __init__(self, limit):
        self.current = 0
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        val = self.current
        self.current += 1
        return val

counter = Counter(3)
for num in counter:  # uses __iter__ and __next__ behind the scenes
    print(num)

''' in for loop, It automatically performs the following steps:
Step-by-Step Expansion
Calls iter() on the iterable:
iterator = iter(counter)  # this calls counter.__iter__()
This checks if counter is iterable.

It expects counter to have a method called __iter__() that returns an iterator.

In our Counter class, __iter__() returns self, because the object itself is the iterator.

Uses the iterator in a loop:
while True:
    try:
        num = next(iterator)  # calls iterator.__next__()
        # body of the loop
        print(num)
    except StopIteration:
        break
The loop calls next(iterator) repeatedly, which triggers the __next__() method.

When __next__() raises a StopIteration, the loop ends.
'''
