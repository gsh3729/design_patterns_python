'''
decouples an abstraction from its implementation, so the two can vary independently.

when you want to avoid a permanent binding between an abstraction and its implementation 
and when both the abstractions and implementations can have multiple variants.

Separate the abstraction (Remote) from the implementation (Device).
The abstraction: what the user interacts with (e.g., RemoteControl)
The implementation: the specific device being controlled (e.g., TV, Radio)
➡️ So, one abstraction can work with any implementation, and both can grow independently.
'''

# Implementor
class Device:
    def is_enabled(self): pass
    def enable(self): pass
    def disable(self): pass
    def set_volume(self, volume): pass

# ConcreteImplementors
class TV(Device):
    def __init__(self):
        self._on = False
        self._volume = 10

    def is_enabled(self): return self._on
    def enable(self): self._on = True
    def disable(self): self._on = False
    def set_volume(self, volume): self._volume = volume

class Radio(Device):
    def __init__(self):
        self._on = False
        self._volume = 10

    def is_enabled(self): return self._on
    def enable(self): self._on = True
    def disable(self): self._on = False
    def set_volume(self, volume): self._volume = volume

# Abstraction
class RemoteControl:
    def __init__(self, device: Device):
        self.device = device

    def toggle_power(self):
        if self.device.is_enabled():
            self.device.disable()
        else:
            self.device.enable()

    def volume_up(self):
        self.device.set_volume(20)

# Refined Abstraction
class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        self.device.set_volume(0)

# Client Code
tv = TV()
remote = AdvancedRemoteControl(tv)
remote.toggle_power()
remote.mute()
