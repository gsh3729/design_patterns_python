'''
allows capturing and externalizing an object’s internal state so that it can be restored later
commonly used for implementing undo/rollback functionality
'''

# Memento
class Memento:
    def __init__(self, state: str):
        self._state = state

    def get_saved_state(self) -> str:
        return self._state


# Originator
class TextEditor:
    def __init__(self):
        self._content = ""

    def write(self, text: str):
        self._content += text

    def save(self) -> Memento:
        return Memento(self._content)

    def restore(self, memento: Memento):
        self._content = memento.get_saved_state()

    def get_content(self) -> str:
        return self._content


# Caretaker
class History:
    def __init__(self):
        self._mementos = []

    def save(self, memento: Memento):
        self._mementos.append(memento)

    def undo(self) -> Memento:
        if self._mementos:
            return self._mementos.pop()
        return None


# Usage
editor = TextEditor()
history = History()

editor.write("Hello, ")
history.save(editor.save())  # Save state

editor.write("world!")
history.save(editor.save())  # Save state

print(editor.get_content())  # Hello, world!

editor.restore(history.undo())  # Undo to previous
print(editor.get_content())  # Hello, 

editor.restore(history.undo())  # Undo again
print(editor.get_content())  # (empty)
