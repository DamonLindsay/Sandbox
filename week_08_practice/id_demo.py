import random
from kivy.app import App
from kivy.lang import Builder


class IDDemo(App):
    def build(self):
        self.title = "Demoing the id attribute"
        self.root = Builder.load_file('id_demo.kv')
        return self.root

    def handle_pressed(self):
        if random.randint(1, 10) <= 5:
            self.root.ids.my_label.text = "ouch!!"
            self.root.ids.another_button.text = "Button 1 Pressed"
        else:
            self.root.ids.my_label.text = "stop that!!"
            self.root.ids.another_button.text = "Button 2 Pressed"


# Create and start the App running
IDDemo().run()
