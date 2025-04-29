'''
lets you separate algorithms from the objects on which they operate. 
when you have a structure of objects and you want to perform operations on these objects without changing their classes.
'''

from abc import ABC, abstractmethod
import json

# ---------- Element Interface ----------
class Item(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

# ---------- Concrete Elements ----------
class Book(Item):
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def accept(self, visitor):
        visitor.visit_book(self)

class DVD(Item):
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def accept(self, visitor):
        visitor.visit_dvd(self)

# ---------- Visitor Interface ----------
class Visitor(ABC):
    @abstractmethod
    def visit_book(self, book):
        pass

    @abstractmethod
    def visit_dvd(self, dvd):
        pass

# ---------- Concrete Visitors ----------

class PriceCalculator(Visitor):
    def __init__(self):
        self.total = 0

    def visit_book(self, book):
        self.total += book.price

    def visit_dvd(self, dvd):
        self.total += dvd.price

class DetailPrinter(Visitor):
    def visit_book(self, book):
        print(f"Book: '{book.title}', Price: ${book.price}")

    def visit_dvd(self, dvd):
        print(f"DVD: '{dvd.title}', Price: ${dvd.price}")

class JsonExporter(Visitor):
    def __init__(self):
        self.items = []

    def visit_book(self, book):
        self.items.append({"type": "Book", "title": book.title, "price": book.price})

    def visit_dvd(self, dvd):
        self.items.append({"type": "DVD", "title": dvd.title, "price": dvd.price})

    def export(self):
        return json.dumps(self.items, indent=2)

# ---------- Client Code ----------
items = [
    Book("The Pragmatic Programmer", 30),
    DVD("Inception", 20),
    Book("Clean Code", 25)
]

# Price Calculation
calculator = PriceCalculator()
for item in items:
    item.accept(calculator)
print(f"Total Price: ${calculator.total}\n")

# Detail Printing
printer = DetailPrinter()
for item in items:
    item.accept(printer)
print()

# JSON Export
exporter = JsonExporter()
for item in items:
    item.accept(exporter)
print("Exported JSON:")
print(exporter.export())

'''
Slightly verbose in Python due to lack of method overloading.
void visit(Book book);
void visit(DVD dvd);

you can just call:
visitor.visit(book)
'''