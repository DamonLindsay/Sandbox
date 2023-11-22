"""
Champion Info App Class
"""

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.app import App
import wikipedia


class ChampionInfoLayout(BoxLayout):
    """Custom layout for the Champion Information App."""


class ChampionInfoApp(App):
    """Main Application class for the Champion Information App."""

    def build(self):
        """Build and return the root widget."""
        return ChampionInfoLayout()

    def search_champion(self):
        """Search for champion information and update the UI."""
        champion_input = self.root.ids.champion_input
        info_label = self.root.ids.info_label

        if champion_input.text:
            champion_name = champion_input.text
            champion_info = self.get_champion_info(champion_name)
            info_label.text = champion_info
        else:
            info_label.text = "Please enter a champion name."

    def get_champion_info(self, champion_name):
        """Get information about the champion from Wikipedia."""
        try:
            champion_info = wikipedia.summary(champion_name, sentences=2)
            return champion_info
        except wikipedia.exceptions.DisambiguationError as e:
            # If there are multiple matches, display the first one
            return wikipedia.summary(e.options[0], sentences=2)
        except wikipedia.exceptions.PageError:
            return "Champion not found on Wikipedia."
