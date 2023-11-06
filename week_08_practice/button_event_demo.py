from kivy.app import App
from kivy.lang import Builder


class ButtonEventDemo(App):
    def build(self):
        self.title = "Button Event Demo"
        self.root = Builder.load_file('button_event.kv')
        return self.root

    def handle_button_press(self, button):
        # The parameter passed is the button object.
        # We can then access its attributes, like text, pos, font_name, width...
        # But we can not directly access its id if specified in the kv file (due to the way Kivy is designed)
        print("Button text: '{}', pos: {}".format(button.text, button.pos))

    def handle_release(self, button):
        print("Hello")

    def handle_release_dont(self):
        print("Released the don't button")


ButtonEventDemo().run()
