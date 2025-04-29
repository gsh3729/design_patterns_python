'''to minimize memory usage by sharing as much data as possible with similar objects
It's useful when many objects are created that share common properties.

Intrinsic State: Shared data that's invariant across objects.
Extrinsic State: Context-specific data passed in at runtime.
Flyweight Factory: Manages and reuses flyweight objects.
'''

class Character:
    def __init__(self, char):
        self.char = char  # Intrinsic state

    def display(self, font_size):
        # Extrinsic state is passed during method call
        print(f"Character: {self.char} with font size {font_size}")


class CharacterFactory:
    _characters = {}

    @classmethod
    def get_character(cls, char):
        if char not in cls._characters:
            cls._characters[char] = Character(char)
        return cls._characters[char]


# Usage
if __name__ == "__main__":
    factory = CharacterFactory()

    text = "hello"
    for c in text:
        char_obj = factory.get_character(c)
        char_obj.display(font_size=12)

    # Check memory optimization
    print(factory._characters)


'''
font_size is extrinsic.

It's not stored inside the object.

Instead, it's passed in when we want to display the character.

You might display 'h' at size 12 in one place, and at size 18 in another.
'''