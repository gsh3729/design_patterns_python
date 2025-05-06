Iterator: The Iterator pattern provides a way to access elements of an aggregate object (like a collection) without exposing its underlying representation.

Observer: In the Observer pattern, an object (the subject) maintains a list of its dependent observers and notifies them of state changes, usually by calling one of their methods.

Strategy: This pattern allows defining a family of algorithms and making them interchangeable. It lets the algorithm be selected at runtime, promoting flexibility.

Command: The Command pattern encapsulates a request as an object, thereby allowing for parameterization of clients with queues, requests, and operations.

State: The State pattern allows an object to alter its behavior when its internal state changes. The object will appear to change its class.

Template Method: The Template Method pattern defines the skeleton of an algorithm in a method, deferring some steps to subclasses. It lets subclasses redefine certain steps of the algorithm without changing its structure.

Visitor: The Visitor pattern allows new operations to be added to existing object structures without modifying their classes.

Mediator: This pattern reduces the complexity of communication between objects by centralizing the communication in a mediator object. Objects do not communicate directly but through the mediator.

Memento: The Memento pattern allows the state of an object to be captured and restored without exposing its internal structure.

Chain of Responsibility: This pattern allows passing a request along a chain of handlers, where each handler either processes the request or passes it along to the next handler in the chain.