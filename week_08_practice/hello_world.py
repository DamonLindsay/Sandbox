from kivy.app import App
from kivy.app import Widget


class HelloWorld(App):  # Class (new type)
    def build(self):  # Method (function)
        self.root = Widget()  # 'self' - Reference to this instance
        return self.root


HelloWorld().run()  # 'HelloWorld() - Create new object of type HelloWorld.
# '.run()' - Call method 'run' of new object (Kivy defines this method)
