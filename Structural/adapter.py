'''
You have an existing class, but its interface (method names, behaviors) does not match what your client code expects.

Solution: Instead of modifying the existing class (which might be impossible, especially if it's external or legacy code), create a new Adapter class.

🟡 Adapter Class:

Internally holds (wraps) an instance of the old class.

Externally offers the new, correct interface.

Translates calls from the new interface to the old one.

👉 Main logic: "Don't change the old class. Wrap it and make it behave correctly."
'''

# Your app expects new shape classes to have a draw() method.
class Shape:
    def draw(self):
        pass

# But you also have a legacy Rectangle class from an old library:
class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class LegacyRectangle:
    def render(self):
        print("Rendering a rectangle (old method)")

class RectangleAdapter(Shape):
    def __init__(self, legacy_rectangle):
        self.legacy_rectangle = legacy_rectangle

    def draw(self):
        # Adapting render() -> draw()
        self.legacy_rectangle.render()

shapes = [
    Circle(),
    RectangleAdapter(LegacyRectangle())
]

for shape in shapes:
    shape.draw()

# legacy 
class FahrenheitThermometer:
    def get_temperature(self):
        return 98.6
    
# target interface
class CelsiusThermometer:
    def get_temperature(self):
        pass

class AdapterThermometer(CelsiusThermometer):
    def __init__(self, legacy_thermometer):
        self.legacy_thermometer = legacy_thermometer

    def get_temperature(self):
        fahrenheit = self.legacy_thermometer.get_temperature()
        return (fahrenheit - 32) * 5.0 / 9.0

legacy = FahrenheitThermometer()
adapter = AdapterThermometer(legacy)

print(f"Temperature in Celsius: {adapter.get_temperature():.2f}")
