'''
lets you pass requests along a chain of handlers. 
When a request comes in, each handler decides either to process it or to pass it along to the next handler in the chain.
'''
from abc import ABC, abstractmethod

# Abstract Handler
class Handler(ABC):
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler  # Allow chaining

    @abstractmethod
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

# Concrete Handlers
class AuthHandler(Handler):
    def handle(self, request):
        if request.get("user") == "admin":
            print("AuthHandler: User authenticated")
            return super().handle(request)
        else:
            print("AuthHandler: Unauthorized user")
            return "Unauthorized"

class LoggingHandler(Handler):
    def handle(self, request):
        print("LoggingHandler: Logging request")
        return super().handle(request)

class BusinessLogicHandler(Handler):
    def handle(self, request):
        print("BusinessLogicHandler: Processing business logic")
        return "Request Processed"

# Client code
if __name__ == "__main__":
    # Create handlers
    auth = AuthHandler()
    logger = LoggingHandler()
    logic = BusinessLogicHandler()

    # Chain them
    auth.set_next(logger).set_next(logic)

    # Make a request
    request = {"user": "admin", "action": "update_record"}
    result = auth.handle(request)
    print("Result:", result)


'''
length = LengthValidator()
email = EmailValidator()
success = SuccessHandler()
length.set_next(email).set_next(success)

print(length.handle({"name": "Al", "email": "a@b.com"}))  # Fails on Length
print(length.handle({"name": "Alex", "email": "alex.com"}))  # Fails on Email
print(length.handle({"name": "Alex", "email": "alex@xyz.com"}))  # Pass
'''