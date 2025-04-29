# Abstract Products
class Button:
    def render(self):
        pass

class Checkbox:
    def render(self):
        pass

# Concrete Products - Windows
class WindowsButton(Button):
    def render(self):
        return "Render a button in Windows style"

class WindowsCheckbox(Checkbox):
    def render(self):
        return "Render a checkbox in Windows style"

# Concrete Products - Mac
class MacButton(Button):
    def render(self):
        return "Render a button in Mac style"

class MacCheckbox(Checkbox):
    def render(self):
        return "Render a checkbox in Mac style"

# Abstract Factory
class GUIFactory:
    def create_button(self) -> Button:
        pass

    def create_checkbox(self) -> Checkbox:
        pass

# Concrete Factory - Windows
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

# Concrete Factory - Mac
class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()

# Client
def render_ui(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.render())
    print(checkbox.render())

# Example usage
if __name__ == "__main__":
    os_type = "Windows"  # could be dynamically detected
    factory = WindowsFactory() if os_type == "Windows" else MacFactory()
    render_ui(factory)


'''
provides an interface for creating families of related or dependent objects without specifying their concrete classes
'''
