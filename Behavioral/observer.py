'''
an object (the subject) maintains a list of its dependents (observers) 
and notifies them automatically of any state changes, 
usually by calling one of their methods.
'''

from abc import ABC, abstractmethod

# Observer base class
class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass

# Concrete Observer
class EmailClient(Observer):
    def update(self, message):
        print(f"[Email] New message: {message}")

class SMSClient(Observer):
    def update(self, message):
        print(f"[SMS] New message: {message}")

# Subject class
class NotificationCenter:
    def __init__(self):
        self._observers = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self, message: str):
        for observer in self._observers:
            observer.update(message)

# Usage
if __name__ == "__main__":
    notifier = NotificationCenter()
    
    email_client = EmailClient()
    sms_client = SMSClient()

    notifier.attach(email_client)
    notifier.attach(sms_client)

    notifier.notify("New product launch!")

    notifier.detach(sms_client)

    notifier.notify("Price drop alert!")
