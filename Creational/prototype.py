'''
clone objects instead of creating new ones from scratch, which can be more efficient, especially when object creation is costly.

When object creation is expensive (e.g., involves database access or network calls).

When there are many potential configurations of an object.
'''
class Prototype:
    def clone(self):
        raise NotImplementedError("Subclasses must implement clone().")

class User(Prototype):
    def __init__(self, name, email, password, preferences):
        self.name = name
        self.email = email
        self.password = password  # sensitive, don't copy
        self.preferences = preferences

    def clone(self):
        # Only copy non-sensitive data
        return User(
            name=self.name,
            email=self.email,
            password=None,  # or mask it
            preferences=self.preferences.copy()
        )

    def __str__(self):
        return f"User(name={self.name}, email={self.email}, password={self.password}, prefs={self.preferences})"

class Product(Prototype):
    def __init__(self, id, title, price, inventory, metadata):
        self.id = id
        self.title = title
        self.price = price
        self.inventory = inventory
        self.metadata = metadata

    def clone(self):
        # Only copy ID, title, and price; ignore live inventory and metadata
        return Product(
            id=self.id,
            title=self.title,
            price=self.price,
            inventory=None,
            metadata=None
        )

    def __str__(self):
        return f"Product(id={self.id}, title={self.title}, price={self.price})"

# --- Usage ---
user1 = User("Harsha", "harsha@example.com", "supersecret", {"theme": "dark"})
user2 = user1.clone()

product1 = Product(101, "iPhone", 999.99, 50, {"color": "black", "warranty": "1 year"})
product2 = product1.clone()

print(user1)
print(user2)
print(product1)
print(product2)


import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)

class Person(Prototype):
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills

    def __str__(self):
        return f"{self.name}, Skills: {self.skills}"

# Original object
original = Person("Alice", ["Python", "ML"])

# Cloning
clone1 = original.clone()
clone1.name = "Bob"
clone1.skills.append("Distributed Systems")

print(original)  # Alice, Skills: ['Python', 'ML']
print(clone1)    # Bob, Skills: ['Python', 'ML', 'Distributed Systems']
