'''
allows an object to change its behavior when its internal state changes. 
when an object must change its behavior depending on its state at runtime, making the code more maintainable and readable.
'''

from abc import ABC, abstractmethod

# State Interface
class State(ABC):
    @abstractmethod
    def publish(self, document):
        pass

    @abstractmethod
    def edit(self, document):
        pass


# Concrete States
class DraftState(State):
    def publish(self, document):
        print("Moving document to Moderation.")
        document.set_state(ModerationState())

    def edit(self, document):
        print("Editing the document in Draft state.")


class ModerationState(State):
    def publish(self, document):
        print("Publishing the document.")
        document.set_state(PublishedState())

    def edit(self, document):
        print("Cannot edit document in Moderation state.")


class PublishedState(State):
    def publish(self, document):
        print("Document is already published.")

    def edit(self, document):
        print("Cannot edit a published document.")


# Context
class Document:
    def __init__(self):
        self._state = DraftState()

    def set_state(self, state):
        print(f"State changed to {state.__class__.__name__}")
        self._state = state

    def publish(self):
        self._state.publish(self)

    def edit(self):
        self._state.edit(self)

# Usage
doc = Document()
doc.edit()
doc.publish()
doc.edit()
doc.publish()
doc.edit()
