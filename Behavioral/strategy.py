'''
enables selecting an algorithm's behavior at runtime.
when you have multiple ways of performing a task 
and want to choose the best one dynamically without modifying the client code.
'''

from abc import ABC, abstractmethod

# Strategy Interface
class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass

# Concrete Strategies
class QuickSort(SortStrategy):
    def sort(self, data):
        print("Using QuickSort")
        return sorted(data)  # using Python's built-in (which is Timsort for simplicity)

class BubbleSort(SortStrategy):
    def sort(self, data):
        print("Using BubbleSort")
        data = data[:]
        for i in range(len(data)):
            for j in range(0, len(data)-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
        return data

# Context
class SortContext:
    def __init__(self, strategy: SortStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: SortStrategy):
        self._strategy = strategy

    def sort_data(self, data):
        return self._strategy.sort(data)

# Usage
data = [5, 2, 9, 1]
context = SortContext(QuickSort())
print(context.sort_data(data))  # QuickSort

context.set_strategy(BubbleSort())
print(context.sort_data(data))  # BubbleSort
