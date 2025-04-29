def timer(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Executed in {time.time() - start}s")
        return result
    return wrapper

class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        import time
        start = time.time()
        result = self.func(*args, **kwargs)
        print(f"Executed in {time.time() - start}s")
        return result

@Timer
def slow_function():
    import time
    time.sleep(2)
    print("Finished sleeping!")

# Now call the function
slow_function()

''' 
Finished sleeping!
Executed in 2.002345085144043s
'''

'''
to add new behavior (functionality) to an object dynamically at runtime without altering the original object’s code.
Problem it solves:
"I want to modify or extend an object's behavior without rewriting its class or making thousands of subclasses."
How it solves it:
"Wrap the original object inside another object (decorator) that adds the extra behavior before/after forwarding calls to the original object."
Core Mechanism:
The decorator holds a reference to the original object.
When the decorated object’s method is called, the decorator:
(Optionally) does something extra before.
Calls the original object’s method.
(Optionally) does something extra after.
'''

'''
Suppose you have a BasicCoffee:
- Basic Coffee: cost() = 5
Now you want to dynamically add:
Milk (+1.5)
Sugar (+0.5)

But you don't want to create:
MilkCoffee
SugarCoffee
MilkAndSugarCoffee
VanillaMilkSugarCoffee
etc. (this would explode into 100 classes!)

Instead, you wrap the BasicCoffee inside a MilkDecorator, then wrap again inside a SugarDecorator.
Each wrapper adds its own behavior!
'''

# Component Interface
class Coffee:
    def cost(self):
        pass

# Concrete Component
class BasicCoffee(Coffee):
    def cost(self):
        return 5

# Decorator
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

# Concrete Decorators
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return super().cost() + 1.5

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return super().cost() + 0.5

coffee = BasicCoffee()
coffee = MilkDecorator(coffee)
coffee = SugarDecorator(coffee)
print(coffee.cost())  # 7.0
