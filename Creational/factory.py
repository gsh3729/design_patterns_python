from abc import ABC, abstractmethod

# Product Interface
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# Concrete Products
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Creator
class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self) -> Animal:
        pass

# Concrete Creators
class DogFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Dog()

class CatFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Cat()

# Client Code
def get_pet(factory: AnimalFactory):
    animal = factory.create_animal()
    print(animal.speak())

get_pet(DogFactory())  # Output: Woof!
get_pet(CatFactory())  # Output: Meow!

''' 
Factory: delegate the instantiation of objects to subclasses
animal = Dog()
Hard to extend: What if later you want to use Cat instead? You have to change every place that uses Dog().
✅ Factory Method Solves This By:
Defining a common interface (Animal)

Abstracting the instantiation logic into a method (create_animal)

Delegating the choice of class to subclasses (DogFactory, CatFactory)

Now your client code depends only on the interface, not on the concrete implementation.
'''