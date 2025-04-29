'''
promotes loose coupling by keeping objects from referring to each other explicitly. 
Instead, they communicate through a mediator object.
'''

class ChatRoomMediator:
    def show_message(self, user, message):
        raise NotImplementedError

from datetime import datetime
class ChatRoom(ChatRoomMediator):
    def show_message(self, user, message):
        time = datetime.now().strftime("%H:%M:%S")
        print(f"[{time}] {user.name}: {message}")

class User:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    def send(self, message):
        self.mediator.show_message(self, message)

if __name__ == "__main__":
    chatroom = ChatRoom()

    alice = User("Alice", chatroom)
    bob = User("Bob", chatroom)

    alice.send("Hi Bob!")
    bob.send("Hey Alice, what's up?")

class Mediator:
    def notify(self, sender, event):
        pass

class FormMediator(Mediator):
    def __init__(self):
        self.username = None
        self.checkbox = None
        self.submit_button = None

    def notify(self, sender, event):
        if event == "input_changed" or event == "checkbox_toggled":
            if self.username.text and self.checkbox.checked:
                self.submit_button.enable()
            else:
                self.submit_button.disable()

class TextBox:
    def __init__(self, mediator):
        self.mediator = mediator
        self.text = ""

    def input(self, text):
        self.text = text
        self.mediator.notify(self, "input_changed")

class CheckBox:
    def __init__(self, mediator):
        self.mediator = mediator
        self.checked = False

    def toggle(self):
        self.checked = not self.checked
        self.mediator.notify(self, "checkbox_toggled")

class Button:
    def __init__(self):
        self.enabled = False

    def enable(self):
        self.enabled = True
        print("Submit Button ENABLED")

    def disable(self):
        self.enabled = False
        print("Submit Button DISABLED")

mediator = FormMediator()

username_box = TextBox(mediator)
agree_terms = CheckBox(mediator)
submit = Button()

mediator.username = username_box
mediator.checkbox = agree_terms
mediator.submit_button = submit

# Simulate user input
username_box.input("Sriharsha")  # Not enough yet
agree_terms.toggle()             # Now it should enable the button
agree_terms.toggle()             # Disables again

