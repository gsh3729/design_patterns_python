'''
turns a request into a standalone object containing all information about the request. 
to parameterize methods with different requests, delay or queue a request's execution, and support undoable operations.
'''

from abc import ABC, abstractmethod

# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Receiver
class Light:
    def turn_on(self):
        print("Light is ON")
    
    def turn_off(self):
        print("Light is OFF")

# Concrete Commands
class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light
    
    def execute(self):
        self.light.turn_on()

class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light
    
    def execute(self):
        self.light.turn_off()

# Invoker
class RemoteControl:
    def __init__(self):
        self.command = None
    
    def set_command(self, command: Command):
        self.command = command
    
    def press_button(self):
        self.command.execute()

# Client code
if __name__ == "__main__":
    light = Light()
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)

    remote = RemoteControl()
    
    remote.set_command(light_on)
    remote.press_button()  # Output: Light is ON

    remote.set_command(light_off)
    remote.press_button()  # Output: Light is OFF

'''
Parameterize Methods with Different Requests
remote.set_command(light_on)
remote.press_button()

Delay or Queue a Request's Execution
import time

command_queue = [LightOnCommand(light), LightOffCommand(light)]

for cmd in command_queue:
    time.sleep(1)
    cmd.execute()

Support Undoable Operations
useful in text editors, drawing applications, game state handling, etc.
'''

class Command(ABC):
    @abstractmethod
    def execute(self): pass

    @abstractmethod
    def undo(self): pass

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

    def undo(self):
        self.light.turn_off()

# Usage
remote.set_command(light_on)
remote.press_button()  # Light ON
remote.command.undo()  # Light OFF
