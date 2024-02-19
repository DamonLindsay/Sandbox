"""
Champion Stats App
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.button import Button


class ChampionStatsApp(App):
    def __init__(self):
        super().__init__()
        self.level_label = ""
        self.selected_champion = "Ezreal"
        self.champions = {
            "Ezreal": {
                "Health": {"base": 500, "growth": 80},
                "Attack Damage": {"base": 60, "growth": 2.5},
                "Attack Speed": {"base": 0.625, "growth": 0.02},
                "Armor": {"base": 22, "growth": 2.5},
                "Magic Resist": {"base": 30, "growth": 0.5}
            },
            "ChampionTemplate": {
                "Health": {"base": 600, "growth": 90},
                "Attack Damage": {"base": 55, "growth": 3.0},
                "Attack Speed": {"base": 0.7, "growth": 0.03},
                "Armor": {"base": 25, "growth": 2.0},
                "Magic Resist": {"base": 35, "growth": 1.0},
            }
        }

    def build(self):
        """Build the main layout of the application."""
        self.selected_champion = "Ezreal"  # Initialize selected_champion

        layout = BoxLayout(orientation="vertical", padding=10)

        self.level_label = Label(text="Level: 1")
        layout.add_widget(self.level_label)

        for stat, values in self.champions["Ezreal"].items():
            label = Label(text=f"{stat}: {values['base']}")
            layout.add_widget(label)

        level_slider = Slider(min=1, max=18, value=1)
        level_slider.bind(value=self.on_level_change)
        layout.add_widget(level_slider)

        champion_buttons_layout = BoxLayout(orientation="horizontal")
        for champion_name in self.champions.keys():
            champion_button = Button(text=champion_name, on_press=self.on_champion_button_press)
            champion_buttons_layout.add_widget(champion_button)

        layout.add_widget(champion_buttons_layout)

        return layout

    def on_level_change(self, instance, value):
        """Handle the change in the slider level."""
        self.level_label.text = f"Level: {int(value)}"
        self.update_stats(self.selected_champion, int(value))

    def on_champion_button_press(self, instance):
        """Handle the press of a champion selection button."""
        self.selected_champion = instance.text

        # Check if the widget exists before accessing it
        if "level_slider" in self.root.ids:
            self.update_stats(self.selected_champion, int(self.root.ids.level_slider.value))
        else:
            print("Error: level_slider not found.")

    def update_stats(self, champion, level):
        """Update the displayed stats based on the selected champion and level."""
        for stat, values in self.champions[champion].items():
            base_stat = values["base"] + values["growth"] * (level - 1)
            self.root.ids[stat.lower() + "_label"].text = f"{stat}: {base_stat}"


if __name__ == '__main__':
    ChampionStatsApp().run()
