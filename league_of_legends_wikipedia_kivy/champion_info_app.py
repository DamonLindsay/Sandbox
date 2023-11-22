"""
Champion Info App Class
"""

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.progressbar import ProgressBar
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
        title_label = self.root.ids.title_label
        url_label = self.root.ids.url_label

        if champion_input.text:
            champion_name = champion_input.text
            try:
                page = wikipedia.page(champion_name)
                champion_info = wikipedia.summary(champion_name)
                info_label.text = champion_info
                title_label.text = f"Title: {page.title}"
                url_label.text = f"URL: {page.url}"
            except wikipedia.exceptions.DisambiguationError as e:
                # If there are multiple matches, display the first one
                self.show_popup("Disambiguation Error",
                                f"Multiple matches found.  Displaying the first one: {e.options[0]}")
                champion_info = wikipedia.summary(e.options[0])
                info_label.text = champion_info
                title_label.text = ""
                url_label.text = ""
            except wikipedia.exceptions.PageError:
                self.show_popup("Page Error", "Champion not found on Wikipedia.")
                info_label.text = ""
                title_label.text = ""
                url_label.text = ""
        else:
            info_label.text = "Please enter a champion name."
            info_label.text = ""
            title_label.text = ""
            url_label.text = ""

    def show_popup(self, title, content):
        """Show a popup with a given title and content."""
        popup = Popup(title=title, content=Label(text=content), size_hint=(None, None), size=(400, 200))
        popup.open()

    def clear_info(self):
        """Clear champion information."""
        self.root.ids.info_label.text = ""
        self.root.ids.url_label.text = ""
        self.root.ids.title_label.text = ""
        self.root.ids.champion_input.text = ""


if __name__ == '__main__':
    ChampionInfoApp().run()
